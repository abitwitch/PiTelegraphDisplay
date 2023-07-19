import sys
sys.path.insert(1, './Screen')
import telegraph-display
#modes: 0-just type, 1-practice alpha, 2-practice digits, 3-practice alphanum, 4-practice symbols, 5-practice all
mode=0
userInput=""
streak=0
index=0
screen = telegraph-display.Screen()

lineLength=10


morseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '&': '.-...', '\'': '.----.', '@': '.--.-.', '(': '-.--.-', ')': '-.--.', ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '%': '------..-.-----', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.', '\\': '-.-.-', '\b': '----', '\n': '.-.-', ' ': '..--'
    }
    

def loadText():
    with open("Sample.txt", "r") as f:
        text=f.read()
    return(text)

def updateDisplay():
    #line 1
    if mode==0:
        line1=""
    else:
        if streak==0:
            #show hint
            line1="hint: +"morseCode[text[index]]
        else:
            line1="streak: "+str(streak)
    #line 2
    fromIndex=max(0,index-lineLength)
    toIndex=min(len(text)-1,index+lineLength)
    line2=text[fromIndex,toIndex]
    #lines to display
    screen.writeLines(line1,line2)


def updateVals():
    if mode==0:
        if userInput=="\b":
            #backspace
            index-=1
            text=text[0:-1]
        else:
            index+=1
            text+=userInput
    else:
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
        updateVals()
       

if __name__ == "__main__":
    main()
