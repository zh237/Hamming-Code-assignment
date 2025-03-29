
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from hammingcode.hammingCode import HammingCode
import numpy as np
import math


""" 
This file is used to show case the use of hammingCode. 
"""
def createHammingCode(message):
   code = HammingCode(message, False)
   code.encode()
   return code.getCode()
  
def addErrorToCode(code, index_to_create_error):
    # create an error manually. 
    indexToChange = index_to_create_error #you can change this, and output will also change.
    if (code[indexToChange] == 1):
      code[indexToChange] = 0
    else:
      code[indexToChange] = 1
    return code

def checkForError(received):

    n = len(received)
    r = 0
    while (2 ** r) <= n:
        r += 1

    error_pos = 0

    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, n + 1):
            if j & parity_pos:
                parity ^= received[j - 1]
        if parity != 0:
            error_pos += parity_pos

    return error_pos  # 0 means no error
###  Test case 1 :
#array = np.random.randint(0,2,20)

array = np.array([1,1,0,1])
code = createHammingCode(array)
print("original code : ", array)
print(f"Hamming code: {code[1:]}, parity bit: {code[0]}, extended hamming code: {code}")


#error_code = code
#code = addErrorToCode(code, 1)
#error_code = addErrorToCode(code,2)
#error_code = addErrorToCode(code, 1)

print("received code: ", code)

received_code =  HammingCode(code,True)
received_code.checkForError()

# Decode
recover_code = HammingCode(code[1:],True)
recover_code = recover_code.decode()
print("recovered code : ", recover_code)






