#import hammingCode
from hammingCode import hammingCode
import numpy as np

array = np.random.randint(0,2,16)

code = hammingCode(array)
print(code.createCode())

testString = "zadwawfca"
cod2 = hammingCode(testString)
print(cod2.createCode())
