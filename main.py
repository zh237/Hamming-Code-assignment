#import hammingCode
from hammingCode import HammingCode
import numpy as np
import math

# array = np.random.randint(0,2,20)
# code = HammingCode(array)
# print(code.toBinary())
# print(code.createCode())
# print (code.findError())

test_case = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1]
code = HammingCode(test_case,True)
code.findError()

# testString = "zadwawfca"
# cod2 = HammingCode(testString)
# print(cod2.toBinary())
# print(code.createCode())
