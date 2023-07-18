
#modes: 0-just type, 1-practice alpha, 2-practice digits, 3-practice alphanum, 4-practice symbols, 5-practice all
mode=0
userInput=""
streak=0
index=0

lineLength=10

def loadText():
    with open("Sample.txt", "r") as f:
        text=f.read()
    return(text)

def updateDisplay():
    #TODO

def checkInput():
    if text[index]==userInput:
        streak+=1
        index+=1
    else:
        streak=0

def main():
    print("Running...")
    text=loadText()
    while True:
        updateDisplay()
        getCharFromUser()
        if mode!=0:
            checkInput()

if __name__ == "__main__":
    main()
