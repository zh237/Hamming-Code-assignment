
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
def testHammingCode(message, index_to_create_error):
    code = HammingCode(message, False) 
    code.encode()

    # since we have just created the code, there should not be any errors
    code.checkForError() 

    testcode = code.getCode()
    # create an error manually. 
    indexToChange = index_to_create_error #you can change this, and output will also change.
    if (testcode[indexToChange] == 1):
      testcode[indexToChange] = 0
    else:
      testcode[indexToChange] = 1
    
    code = HammingCode(testcode,True)

    # Should print the value of "indexToChange"
    code.checkForError()


###  Test case 1 :
array = np.random.randint(0,2,20)
testHammingCode(array,6)
"""
Should print :
No error was detected !
Error : index num : 6 , Binary : 110 
"""


###  Test case 2 :
testHammingCode("Testing hamming code",20)
"""
Should print :
No error was detected !
Error : index num : 20 , Binary : 10100  
"""