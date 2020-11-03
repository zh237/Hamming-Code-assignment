import numpy as np
import math
from functools import reduce

"""
For error detection, redundant bits are added to the current information to create hamming-code.
The efficency increase with larger data, but remeber, hamming code can only detect up to 2 error and up to 1 error can be found and fixed.
( This is extended hamming-code(8,4) : Index 0 is used for detecting two bit errors )
"""
class HammingCode:
    def __init__(self, message, forChecking):
        
        if (forChecking):
            # input parameter will be used to create hamming code
            self.binary = message
        else:
            # input parameter will be checked.
            self.data = message
  

    def to_binary_list(self):
        if (isinstance(self.data, np.ndarray)):
            self.binary = self.data.tolist()
              
        elif (isinstance(self.data,list)):
            self.binary = self.data
        
        elif (isinstance(self.data, str)):
            binary_in_string = "".join(format(i, 'b')
                                for i in bytearray(self.data, "utf8"))
            templist = []
            for i in range(0,len(binary_in_string)):
                templist.append(int(binary_in_string[i]))
            self.binary = templist

    def createCode(self):
        self.to_binary_list()
    
        # Block length : 2**r  where r >= 2
        message_len = len( self.binary )
        r = 1
        while (2**r < message_len + r + 1 ):
            r+=1
         
        self.binary.insert(0,0)
        for i in range(1, message_len + r + 1 ):
            if ( math.log(i,2) == math.ceil(math.log(i,2)) ):
                self.binary.insert(i,0)
        
        for i in range(0,r):
            x = 2**i
            for j in range(1,len(self.binary)):
                if ( ((j>>i)&1)==1  ):
                    if (x!=j):
                        self.binary[x] = self.binary[x]^self.binary[j]

    def getCode(self):
        return self.binary

    def findError(self):
        pos = (reduce (lambda x, y: x^y , [i for i, bit in enumerate(self.binary) if bit]))
        binaryRep = format(pos, 'b')
        if (pos != 0):
            print ("Error : index num : {} , Binary : {} ".format(pos, binaryRep))
        else:
            print ("No error was detected !")