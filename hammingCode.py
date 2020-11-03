import numpy as np
from functools import reduce


class hammingCode:
    def __init__(self, data):
        self.data = data
        # self.code = createCode()

    def createCode(self):
        if (isinstance(self.data, (list, tuple, np.ndarray))):
            pass

        if (isinstance(self.data, str)):
            self.code = "".join(format(i, 'b')
                                for i in bytearray(self.data, "utf8"))
            # each character will be represented using 7
            print(self.code)
            print(len(self.code))

        size = len(self.data)
        i = 1
        while (i**2 < size):
            i = i*2
        pos = (reduce (lambda x, y: x^y , [i for i, bit in enumerate(self.data) if bit]))
        binaryRep = format(pos, 'b')
        print ("num : {} , Binary : {} ".format(pos, binaryRep))
        print(len(binaryRep))
        if (len(binaryRep) < i):
            s = ""
            for j in range(0, i-len(binaryRep)):
                print("0")

    def checkSize(self):
        return 1

    def findError(self):
        return 1
