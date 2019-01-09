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
    

    def constructPath(self, path, index):
        code = ""
        length = len(path[0])
        thisState = index
        for i in range(length-1, -1, -1):
            if(thisState == 0):
                code = code + "0"
            elif(thisState == 1):
                code = code + "0"
            elif(thisState == 2):
                code = code + "1"
            else :
                code = code + "1"
            if(i == -1) :
                thisState = 0
            else : 
                thisState = path[thisState][i]

        return(code[::-1])

    def decode(self, input):
        currentPM = [None] * 4
        nextPM = [None] * 4
        path = [[0 for x in xrange(len(input)/2)] for y in xrange(4)]
        currentPM[0] = 0
        currentPM[1] = float("inf")
        currentPM[2] = float("inf")
        currentPM[3] = float("inf")

        i = 0
        while(i < len(input)) :
            str = input[i : i + 2]
            if(str == '00') :
                if(currentPM[0] < currentPM[1] + 1):
                    nextPM[0] = currentPM[0]
                    path[0][i/2] = 0
                else :
                    nextPM[0] = currentPM[1] + 1
                    path[0][i/2] = 1

                if(currentPM[2] + 2 < currentPM[3] + 1) :
                    nextPM[1] = currentPM[2] + 2
                    path[1][i/2] = 2
                else:
                    nextPM[1] = currentPM[3] + 1
                    path[1][i/2] = 3

                if(currentPM[0] + 2 < currentPM[1] + 1):
                    nextPM[2] = currentPM[0] + 2
                    path[2][i/2] = 0
                else :
                    nextPM[2] = currentPM[1] + 1
                    path[2][i/2] = 1

                if(currentPM[2] < currentPM[3] + 1):
                    nextPM[3] = currentPM[2] 
                    path[3][i/2] = 2
                else :
                    nextPM[3] = currentPM[3] + 1
                    path[3][i/2] = 3
            ###############################

            elif(str == '01') :
                if(currentPM[0] + 1 <  currentPM[1] + 2):
                    nextPM[0] = currentPM[0] + 1 
                    path[0][i/2] = 0
                else:
                    nextPM[0] = currentPM[1] + 2
                    path[0][i/2] = 1

                if(currentPM[2] + 1 < currentPM[3]):
                    nextPM[1] = currentPM[2] + 1
                    path[1][i/2] = 2
                else:
                    nextPM[1] = currentPM[3]
                    path[1][i/2] = 3
                
                if(currentPM[0] + 1 < currentPM[1]):
                    nextPM[2] = currentPM[0] + 1
                    path[2][i/2] = 0
                else :
                    nextPM[2] = currentPM[1]
                    path[2][i/2] = 1

                if(currentPM[2] + 1 < currentPM[3] + 2):
                    nextPM[3] = currentPM[2] + 1
                    path[3][i/2] = 2
                else :
                    nextPM[3] = currentPM[3] + 2
                    path[3][i/2] = 3
            ###############################    

            elif(str == '10') :
                if (currentPM[0] + 1 < currentPM[1]):
                    nextPM[0] = currentPM[0] + 1 
                    path[0][i/2] = 0
                else:
                    nextPM[0] = currentPM[1]
                    path[0][i/2] = 1       

                if(currentPM[2] + 1 < currentPM[3] + 2):
                    nextPM[1] = currentPM[2] + 1
                    path[1][i/2] = 2
                else:
                    nextPM[1] = currentPM[3] + 2
                    path[1][i/2] = 3

                if(currentPM[0] + 1 < currentPM[1] + 2):
                    nextPM[2] = currentPM[0] + 1
                    path[2][i/2] = 0
                else :
                    nextPM[2] = currentPM[1] + 2
                    path[2][i/2] = 1

                if(currentPM[2] + 1 < currentPM[3]):
                    nextPM[3] = currentPM[2] + 1
                    path[3][i/2] = 2
                else :
                    nextPM[3] = currentPM[3]
                    path[3][i/2] = 3
            #########################################
            elif(str == "11"):
                if(currentPM[0] + 2 < currentPM[1] + 1) :
                    nextPM[0] = currentPM[0] + 2 
                    path[0][i/2] = 0
                else:
                    nextPM[0] = currentPM[1] + 1
                    path[0][i/2] = 1

                if(currentPM[2] < currentPM[3] + 1):
                    nextPM[1] = currentPM[2]
                    path[1][i/2] = 2
                else:
                    nextPM[1] = currentPM[3] + 1
                    path[1][i/2] = 3

                if(currentPM[0] < currentPM[1] + 1):
                    nextPM[2] = currentPM[0]
                    path[2][i/2] = 0
                else :
                    nextPM[2] = currentPM[1] + 1
                    path[2][i/2] = 1

                if(currentPM[2] + 2 < currentPM[3] + 1):
                    nextPM[3] = currentPM[2] + 2
                    path[3][i/2] = 2
                else :
                    nextPM[3] = currentPM[3] + 1
                    path[3][i/2] = 3
            
            i = i + 2
            currentPM = nextPM[:]

        index = currentPM.index(min(currentPM))
        print('min error = ', min(currentPM))
        return (self.constructPath(path, index))


def main() :
    c = Convolutional();
    input = raw_input("Enter input : ")
    code = c.encode(input)
    print('code= ', code)
    decoded = c.decode(code)
    print('decode = ', decoded)

if __name__== "__main__":
      main()