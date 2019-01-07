class Convolutional :
    def moveOnMachine(self, state, input) :
        nextState = 0
        output = ""
        if(state == 0 and input == "0"): 
            nextState = 0
            output = "00"
        elif(state == 0 and input == "1"): 
            nextState = 2
            output = "11"
        elif(state == 1 and input == "0") : 
            nextState = 0
            output = "10"
        elif(state == 1 and input == "1") : 
            nextState = 2
            output = "01"
        elif(state == 2 and input == "0") : 
            nextState = 1
            output = "11"
        elif(state == 2 and input == "1") : 
            nextState = 3
            output = "00"
        elif(state == 3 and input == "0") :
            nextState = 1
            output = "01" 
        else: 
            nextState = 3
            output = "10" 
        return (nextState, output)
      

    def encode(self, input):
        i = 0
        state = 0
        ans = ''
        while(i < len(input)):
            state, output = self.moveOnMachine(state, input[i])
            ans = ans + output
            i = i + 1
        return ans

    def decode(self, input):
        currentPM = [None] * 4
        nextPM = [None] * 4
        currentPM[0] = 0
        code = [[0 for x in xrange(len(input)/2)] for y in xrange(4)]
        currentPM[1] = float("inf")
        currentPM[2] = float("inf")
        currentPM[3] = float("inf")

        i = 0
        while(i < len(input)) :
            str = input[i : i + 2]
            if(str == '00') :
                nextPM[0] = min(currentPM[0], currentPM[1] + 1)
                nextPM[1] = min(currentPM[2] + 2, currentPM[3] + 1)
                nextPM[2] = min(currentPM[0] + 2, currentPM[1] + 1)
                nextPM[3] = min(currentPM[2], currentPM[3] + 1)

            elif(str == '01') :
                nextPM[0] = min(currentPM[0] + 1, currentPM[1] + 2)
                nextPM[1] = min(currentPM[2] + 1, currentPM[3])
                nextPM[2] = min(currentPM[0] + 1, currentPM[1])
                nextPM[3] = min(currentPM[2] + 1, currentPM[3] + 2)
            elif(str == '10') :
                nextPM[0] =  min(currentPM[0] + 1, currentPM[1])
                nextPM[1] =  min(currentPM[2] + 1, currentPM[3] + 2)
                nextPM[2] =  min(currentPM[0] + 1, currentPM[1] + 2)
                nextPM[3] =  min(currentPM[2] + 1, currentPM[3])
            else:
                nextPM[0] = min(currentPM[0] + 2, currentPM[1] + 1)
                nextPM[1] = min(currentPM[2], currentPM[3] + 1)
                nextPM[2] = min(currentPM[0], currentPM[1] + 1)
                nextPM[3] = min(currentPM[2] + 2, currentPM[3] + 1)

            i = i + 2
            currentPM = nextPM
    
        print(currentPM)
        print(code)

def main() :
    c = Convolutional();
    input = raw_input("Enter input : ")
    code = c.encode(input)
    print('code= ', code)
    decoded = c.decode(code)
    print('decode = ', decoded)

if __name__== "__main__":
      main()