import random
from Huffman import HuffmanCoding
from Convolutional import Convolutional
import binascii

def noise(input):
    output = ''
    for i in range(0, len(input)):
        r = random.uniform(0, 1)
        if(r < 0.1):
            output += str(1 - int(input[i]))
        else:
            output += (input[i])
    return output

def main() :
    h = HuffmanCoding()
    c = Convolutional()
    input = raw_input("Enter input : ")
    input = input.replace(" ","")
    hEncoded = h.encode(input)
    print('huffman coded', hEncoded)
    cEncoded = c.encode(hEncoded)
    print('Convolutional encoded', cEncoded)
    inputWithNoise = noise(cEncoded)
    print('noise added', inputWithNoise)
    cDecoded = c.decode(inputWithNoise)
    print('convolutional decode', cDecoded)
    hDecoded = h.decode(cDecoded)
    print('huffman decode', hDecoded)
    print(hDecoded)

if __name__== "__main__":
      main()