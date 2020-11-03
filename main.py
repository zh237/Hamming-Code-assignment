#import hammingCode
from hammingCode import HammingCode
import numpy as np
import math

array = np.random.randint(0,2,16)
code = HammingCode(array)
print(code.toBinary())
print(code.createCode())

testString = "zadwawfca"
cod2 = HammingCode(testString)
print(cod2.toBinary())
print(code.createCode())
