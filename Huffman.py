from __future__ import division
import scipy.io
import numpy as np
import operator
from Queue import PriorityQueue

class HuffmanNode(object):
    def __init__(self, left = None, right = None, str = None, value = None):
        self.left = left
        self.right = right
        self.str = str
        self.value = value
        self.code = None

    def getChildren(self):
        return((self.left, self.right))

    def getStr(self):
        return self.str

    def getValue(self):
        return self.value
    
    def getCode(self):
        return self.code
    
    def setCode(self, code):
        self.code = code

class HuffmanCoding :    
    def __init__(self):
        mat = scipy.io.loadmat('freq.mat')
        freqs = mat["freq"]
        self.freqsList = []
        self.dict_encode = {}
        self.dict_decode = {}

        for i in range(97, 123, 1) :
            j = i - 97
            node = HuffmanNode(None, None, chr(i), freqs[j][0])
            self.freqsList.append((freqs[j][0], node))
        
        tree = self.create_tree(self.freqsList)
        root = tree[0][1]
        root.setCode("")
        self.createCodes(root)
        self.createDicts(root)
        

    def create_tree(self, frequencies): 
        while len(frequencies) > 1:       
            indexl, valuel = min(enumerate(frequencies), key=operator.itemgetter(1))
            frequencies = frequencies[:indexl] + frequencies[indexl+1 :]
            indexr, valuer = min(enumerate(frequencies), key=operator.itemgetter(1))
            frequencies = frequencies[:indexr] + frequencies[indexr+1 :]
            value = valuel[0] + valuer[0]
            str = valuel[1].getStr() + valuer[1].getStr()
            node = HuffmanNode(valuel, valuer, str, value)
            frequencies.append((value, node))

        return frequencies  

    def createCodes(self, root) :
        code = root.getCode()
        children = root.getChildren()
        if(children[0] != None):
            children[0][1].setCode(code + "0")
            self.createCodes(children[0][1])
        if(children[1] != None):
            children[1][1].setCode(code + "1")
            self.createCodes(children[1][1])

    def createDicts(self, root) :
        if(len(root.getStr()) == 1): 
            self.dict_encode[root.getStr()] = root.getCode()
            self.dict_decode[root.getCode()] = root.getStr()

        children = root.getChildren()
        if(children[0] != None):
            self.createDicts(children[0][1])
        if(children[1] != None):
            self.createDicts(children[1][1])

    def encode(self, input):
        output = ''
        for i in range(0, len(input)) :
            output = output + self.dict_encode[input[i]]
        return output
        
    def decode(self, input):
        found = False
        code = ''
        ans = ''
        i = 0
        while(i <= len(input)- 1): 
            code = ''
            found = False
            while(found == False):
                if(i >= len(input)) :
                    return "ERROR : Character out of English Alphabet"
                code = code + input[i]
                i = i + 1
                if(self.dict_decode.has_key(code)):
                    ans = ans + self.dict_decode[code]
                    found = True
        return ans


def main() :
    h = HuffmanCoding() 
    input = raw_input("Enter input : ")
    code = h.encode(input)
    print('code= ', code)
    raw = h.decode(code)
    print('decode= ', raw)

if __name__== "__main__":
      main()




