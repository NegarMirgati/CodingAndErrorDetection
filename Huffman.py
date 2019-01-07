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
    
def create_tree(frequencies): 
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

def createCodes(root) :
    code = root.getCode()
    children = root.getChildren()
    if(children[0] != None):
        children[0][1].setCode(code + "0")
        createCodes(children[0][1])
    if(children[1] != None):
        children[1][1].setCode(code + "1")
        createCodes(children[1][1])

def createDicts(root, dict_encode, dict_decode) :
    if(len(root.getStr()) == 1): 
        print(root.getStr(), root.getCode())
        dict_encode[root.getStr()] = root.getCode()
        dict_decode[root.getCode()] = root.getStr()

    children = root.getChildren()
    if(children[0] != None):
        createDicts(children[0][1], dict_encode, dict_decode)
    if(children[1] != None):
        createDicts(children[1][1], dict_encode, dict_decode)

def encode(input, dict):
    output = ''
    for i in range(0, len(input)) :
        output = output + dict[input[i]]
    return output
        
def decode(input, dict):
    found = False
    code = ''
    ans = ''
    i = 0
    while(i <= len(input)- 1): 
        code = ''
        found = False
        while(found == False):
            code = code + input[i]
            i = i + 1
            if(dict.has_key(code)):
                ans = ans + dict[code]
                found = True
    return ans

def main() :
    mat = scipy.io.loadmat('freq.mat')
    freqs = mat["freq"]
    freqsList = []

    for i in range(97, 123, 1) :
        j = i - 97
        node = HuffmanNode(None, None, chr(i), freqs[j][0])
        freqsList.append((freqs[j][0], node))

    tree = create_tree(freqsList)
    root = tree[0][1]
    root.setCode("")
    createCodes(root)
    dict_encode = {}
    dict_decode = {}
    createDicts(root, dict_encode, dict_decode)
    input = raw_input("Enter input : ")
    code = (encode(input, dict_encode))
    print('code= ', code)
    raw = decode(code, dict_decode)
    print('decode= ', raw)

if __name__== "__main__":
      main()




