###########################################################

## Author:          V.H. Unnithan
## Org:             Ancit Consulting Pvt. Ltd.
## Project:         UDS Flashing tool
## Description:     Flashing tool for UDS bootloader based 
##                  on python library - UDS on CAN

## Version:         1.3

#############################################################

######### LIBRARIES ###################



#######################################
import serial 
import Console.UdsError as Error
import CAN.HW_init as can
import FileOp.fileop as fop
import UDS.uds_main as uds
import time
import sys as s
import ctypes

#######################################

DEBUG_ON = 1



print("\n-------------------------------------------------------------")
print('NASH ECU FLASH..\n')

# Initializing the CAN harware.
# Returns the can object after successful connection 
# with the hardware.
if(len(s.argv)>1):
        print("File Path:",s.argv[1])
        file_path = s.argv[1].replace('\\','/')
else:
    print("Path to hex file not found.")
    file_path =  input("Please provide hex file path:").replace('\\','/')
    print("File path:",file_path)
    print("cleaning file path")
    file_path = file_path.replace('"','')

    # Returns the CAN connection handle and the bus
    can_conn,bus = can.CanInit()
    

    

if DEBUG_ON == 1:
    print('Can connection:',can_conn)
    
    
if(can_conn):
        

    
    # Passing the file path, CAN connection handle to the API that starts the UDS 
    # flashing sequence.
    uds.StartUdsFlashing(file_path, can_conn,0,bus)
    
   

    print("Closing CAN channel...")

    can_conn.close()

    try:
        print("The program is now idle. Press Ctrl+C to exit.")
        while True:
            time.sleep(1)  # Sleep for 1 second, effectively doing nothing
    except KeyboardInterrupt:
        print("Exiting...")


