
import can
import udsoncan
import isotp
from udsoncan.connections import IsoTPSocketConnection
from udsoncan.connections import PythonIsoTpConnection
from udsoncan.client import Client
from udsoncan.exceptions import *
from udsoncan.services import *
import time

def CanInit():
    print('Initializing CAN Hardware..\n')

    

    isotp_params = {
    'stmin': 32,                            # Will request the sender to wait 32ms between consecutive frame. 0-127ms or 100-900ns with values from 0xF1-0xF9
    
    'blocksize': 16,                         # Request the sender to send 8 consecutives frames before sending a new flow control message
    'wftmax': 0,                            # Number of wait frame allowed before triggering an error
    'tx_data_length': 8,                    # Link layer (CAN layer) works with 8 byte payload (CAN 2.0)
    # Minimum length of CAN messages. When different from None, messages are padded to meet this length. Works with CAN 2.0 and CAN FD.
    'tx_data_min_length': 8,
    'tx_padding': 0,                        # Will pad all transmitted CAN messages with byte 0x00.
    'rx_flowcontrol_timeout': 5000,         # Triggers a timeout if a flow control is awaited for more than 1000 milliseconds
    'rx_consecutive_frame_timeout': 5000,   # Triggers a timeout if a consecutive frame is awaited for more than 1000 milliseconds
    #'squash_stmin_requirement': False,      # When sending, respect the stmin requirement of the receiver. If set to True, go as fast as possible.
    'max_frame_size': 4095,                 # Limit the size of receive frame.
    'can_fd': True,                        # Does not set the can_fd flag on the output CAN messages
    'bitrate_switch': False,                # Does not set the bitrate_switch flag on the output CAN messages
    'rate_limit_enable': False,             # Disable the rate limiter
    'rate_limit_max_bitrate': 1000000,      # Ignored when rate_limit_enable=False. Sets the max bitrate when rate_limit_enable=True
    'rate_limit_window_size': 0.2,          # Ignored when rate_limit_enable=False. Sets the averaging window size for bitrate calculation when rate_limit_enable=True
    'listen_mode': False,                   # Does not use the listen_mode which prevent transmission.
    }

    uds_config = udsoncan.configs.default_client_config.copy()
    
    bus = can.interface.Bus("PCAN_USBBUS1",interface="pcan",bitrate=500000)

    
    notifier = can.Notifier(bus, [can.Printer()])                                       # Add a debug listener that print all messages

    tp_addr = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=0x7E0, rxid=0x7E8) # Network layer addressing scheme
    
    stack = isotp.NotifierBasedCanStack(bus=bus, notifier=notifier, address=tp_addr, params=isotp_params)  # Network/Transport layer (IsoTP protocol). Register a new listenenr
    conn = PythonIsoTpConnection(stack) 
    
    
    return conn,bus