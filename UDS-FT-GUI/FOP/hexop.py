from intelhex import IntelHex
import sys

MAX_BYTES = 272#16
START_ADDRESS = 0x0000C000

def ReturnStartAddress(path):
    ih = IntelHex(path)
    return ih.minaddr()

def ReturnEndAddress(path):
    ih = IntelHex(path)
    return ih.maxaddr()

def ReturnBytes(startaddress,num_of_bytes,path):

    ih = IntelHex(path)
    

    
    
    ret_data = b''#[]
    if num_of_bytes > MAX_BYTES:
        sys.exit("[Hex file read ERROR]- number of bytes exceeded")

    file_index = 0
    while file_index < num_of_bytes:
        # print("Data:",(ih[startaddress + file_index]))
        # ret_data.append(ih[startaddress + file_index])
        if(ih[startaddress + file_index]>=0):
            ret_data += int.to_bytes((ih[startaddress + file_index]),1,'big',signed=False)
        else:
            return ret_data
        # print("ret data:",ret_data)
        file_index = file_index + 1
    # print("file index:",file_index)
    return ret_data

def ReadHexFile():
    

    # Print the data
    data = ReturnBytes(START_ADDRESS,MAX_BYTES)
    print("Data at address : {}".format(data))