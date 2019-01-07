def moveOnMachine(state, input) :
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
      

def encode(input):
    i = 0
    state = 0
    ans = ''
    while(i < len(input)):
        state, output = moveOnMachine(state, input[i])
        ans = ans + output
        i = i + 1
    return ans

def main() :
    input = raw_input("Enter input : ")
    code = encode(input)
    print('code= ', code)

if __name__== "__main__":
      main()