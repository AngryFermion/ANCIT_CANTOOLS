import can
import can.interfaces.pcan
import udsoncan
import isotp
from udsoncan.connections import IsoTPSocketConnection
from udsoncan.connections import PythonIsoTpConnection
from udsoncan.client import Client
from udsoncan.exceptions import *
from udsoncan.services import *
import Commons.common as UDS_ID
import FOP.hexop as fp
import time as tym
import CAN.HW_init as can
import logger.screenLog as screen_log

TESTING_ON = 0
CONSOLE_PRINT = 1

def TestMessage(CAN_INST):

    print("Testing UDS on CAN with Extended Diagnostic Session Request.....\n\n\n\n\n ")

    with Client(CAN_INST,  request_timeout=2) as client:
        try:
            client.change_session(DiagnosticSessionControl.Session.extendedDiagnosticSession)
            
        except NegativeResponseException as e:
            print('Server refused our request for service %s with code "%s" (0x%02x)' % (e.response.service.get_name(), e.response.code_name, e.response.code))

        except InvalidResponseException as e:
            print('Server sent an invalid payload : %s' % e.response.original_payload)

def AncitTransferExit(client):
    print("Requesting transfer exit")
    try:
        client.request_transfer_exit()
        print("Transfer Exit complete")
    except NegativeResponseException as e:

        print('Server refused our request for service %s with code "%s" (0x%02x)' % (e.response.service.get_name(), e.response.code_name, e.response.code))

    except InvalidResponseException as e:
        print('Server sent an invalid payload : %s' % e.response.original_payload)
    
def AncitEcuReset(client):
    client.ecu_reset(0x01)
    print("ECU Reset Complete")


def AncitTransferData(client,filepath,start_addr,end_addr):

    print("Dowloading hex file into target flash...")
    try:
        total_block = 1
        block = 1
        address = start_addr
        transfer_data = 1
        progress = 0
        progress_total = (end_addr - start_addr)/128
        if CONSOLE_PRINT == 1:
            print("block size:",hex(UDS_ID.MEMORY_BLOCK_SIZE))
            
        while(transfer_data == 1):

            address = UDS_ID.APP_START_ADDRESS_K312 + (total_block - 1)*(128)
            
            progress = (total_block/progress_total)*100
            print("{}%".format(round(progress,1)),"Flashing Complete")
            if((total_block*128)< UDS_ID.MEMORY_BLOCK_SIZE):
                if CONSOLE_PRINT == 0:
                    print("Data:",fp.ReturnBytes(address,128,filepath))
                    print("Address:",hex(address))
                    print("Block:",block)
                client.transfer_data(block,fp.ReturnBytes(address,128,filepath))
            else:
                if CONSOLE_PRINT == 0:
                    print("Data:",fp.ReturnBytes(address,(UDS_ID.MEMORY_BLOCK_SIZE - (total_block - 1)*128),filepath))
                    print("Address:",hex(address))
                    print("Block:",block)
                client.transfer_data(block,fp.ReturnBytes(address,(UDS_ID.MEMORY_BLOCK_SIZE - (total_block - 1)*128),filepath))
                transfer_data = 0
            block = block + 1
            total_block = total_block + 1
            if block == 256:
                block = 0

        print("Transfer Data Complete")
    except NegativeResponseException as e:

        print('Server refused our request for service %s with code "%s" (0x%02x)' % (e.response.service.get_name(), e.response.code_name, e.response.code))

    except InvalidResponseException as e:

        print('Server sent an invalid payload : %s' % e.response.original_payload)


def AncitRequestDownload(client,application_start_address,length):
    UDS_ID.MEMORY_BLOCK_SIZE = length + 1
    try:
        print('Requesting Download....\n')
        client.request_download(SetMemoryLocation(application_start_address))
       

    except NegativeResponseException as e:

        print('Server refused our request for service %s with code "%s" (0x%02x)' % (e.response.service.get_name(), e.response.code_name, e.response.code))

    except InvalidResponseException as e:

        print('Server sent an invalid payload : %s' % e.response.original_payload)


def SetMemoryLocation(address):
    
    memLoc = udsoncan.MemoryLocation(address,UDS_ID.MEMORY_BLOCK_SIZE,UDS_ID.ADDRESS_FORMAT,UDS_ID.MEMORY_BLOCK_FORMAT)
    return memLoc




def StartUdsFlashing(file_path, can_inst,service,bus,log_obj):

    global logg

    logg = log_obj
    
    # Prints the application hex file details

    print('Starting UDS flashing sequence...\n')
    application_start_address = fp.ReturnStartAddress(file_path)
    print("Start Address: {}".format(hex(application_start_address)))
    application_end_address = fp.ReturnEndAddress(file_path)
    print("End Address: {}".format(hex(application_end_address)))
    print("Length:{}",hex(fp.ReturnEndAddress(file_path) - fp.ReturnStartAddress(file_path)))

    

    if TESTING_ON == 1:

        print("Testing")
        
    
    else:

        # Set the P2 timeout to 3 seconds
        config = dict(udsoncan.configs.default_client_config)
        config['use_server_timing'] = False
        config['p2_timeout'] = 3
        config['p2_star_timeout'] = 3
        
        
        # while 1:
       
        if service == 0:
            with Client(can_inst,  request_timeout=10,config=config) as client:
        
                try:
                    
                    client.change_session(DiagnosticSessionControl.Session.programmingSession)
                    print("Programming session Request complete.\n")

                    screen_log.log_message(log_area=logg,message="Programming session Request complete.")
                    
                    client.start_routine(UDS_ID.ERASE_ROUTINE_ID)
                    
                    print("Erase Routine complete.\n")

                    
                    # API to request download

                    AncitRequestDownload(client,application_start_address,application_end_address - application_start_address)
                    
                    # API to Start transfering data
                    AncitTransferData(client,file_path,application_start_address,application_end_address)
                    tym.sleep(.5)

                    # Transfer exit
                    AncitTransferExit(client)

                    # ECU Reset
                    AncitEcuReset(client)
                    
                    
                    
                except NegativeResponseException as e:
                    print('Server refused our request for service %s with code "%s" (0x%02x)' % (e.response.service.get_name(), e.response.code_name, e.response.code))

                except InvalidResponseException as e:
                    print('Server sent an invalid payload : %s' % e.response.original_payload)

                except TimeoutException as e:
                    
                    StartUdsFlashing(file_path,can_inst,0,bus)
                
          
        
    
    