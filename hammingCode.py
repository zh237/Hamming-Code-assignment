import numpy as np
import math
from functools import reduce

"""
For error detection, redundant bits are added to the current information to create hamming-code.
The efficency increase with larger data, but remeber, hamming code can only detect up to 2 error and up to 1 error can be found and fixed.
(This is extended hamming-code(8,4) )
"""
class HammingCode:
    def __init__(self, message, forChecking):
        if (forChecking):
            self.binary = message
        else:
            self.data = message
  

    def toBinary(self):
        if (isinstance(self.data, np.ndarray)):
            self.binary = self.data.tolist()
            
        if (isinstance(list, tuple)):
            self.binary = self.data
        
        if (isinstance(self.data, str)):
            self.binary = "".join(format(i, 'b')
                                for i in bytearray(self.data, "utf8"))
            # each character will be represented using 7

    def createCode(self):
        # Block length : 2**r  where r >= 2
        message_len = len( self.binary )
        r = 1
        while (2**r < message_len + r + 1 ):
            r+=1
        print (r)
         
        self.binary.insert(0,0)
        for i in range(1, message_len + r + 1 ):
            if ( math.log(i,2) == math.ceil(math.log(i,2)) ):
                self.binary.insert(i,0)
        print (self.binary)
        print (len(self.binary))
        
        for i in range(0,r):
            x = 2**i
            for j in range(1,len(self.binary)):
                if ( ((j>>i)&1)==1  ):
                    if (x!=j):
                        self.binary[x] = self.binary[x]^self.binary[j]
        print (self.binary)
        print (len(self.binary))

    def findError(self):
        pos = (reduce (lambda x, y: x^y , [i for i, bit in enumerate(self.binary) if bit]))
        binaryRep = format(pos, 'b')
        print ("num : {} , Binary : {} ".format(pos, binaryRep))