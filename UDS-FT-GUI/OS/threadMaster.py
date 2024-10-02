import UDS_BL.test as uds_test
import UDS_BL.uds_main as uds
import threading
import CAN.HW_init as can
import logger.screenLog as log

def task():
    uds_test.run_test(log_obj)
    uds.StartUdsFlashing(file_path=file,bus=bus,can_inst=can_handle,service=0)

def startTask(obj_log,file_path):
    global log_obj,file,bus,can_handle
    file = file_path
    log_obj = obj_log

    # Initialized CAN hardware

    can_handle, bus = can.CanInit()


    # If hardware init unsuccessful exit with error
    
    if bus == "BUS_INIT_ERROR":
        log.log_message(log_area=log_obj,message="CAN initialization failed..\n")

    elif can_handle == "CAN_INIT_ERR":
        log.log_message(log_area=log_obj,message="CAN initialization failed..\n")


    # If hardware initialization successful
    # start UDS sequence

    else:
        print("Starting Task....\n")
        logging_thread = threading.Thread(target=task, daemon=True)  # Daemon thread will exit when the main program exits
        logging_thread.start()


    
    
    