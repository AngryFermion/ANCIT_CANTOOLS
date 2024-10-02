import time
import logger.screenLog as log
def run_test(obj_log):
    i = 50
    while(i>0):
        i = i-1
        log.log_message(log_area=obj_log,message="Running test blocker\n")
        print("Running test blocker\n")
        time.sleep(1)