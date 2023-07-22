import sys
sys.path.insert(1, './Screen')
sys.path.insert(1, './Battery')
import TelegraphDisplay
import INA219
import sys, tty, termios



#modes: 0-just type, 1-practice alpha, 2-practice digits, 3-practice alphanum, 4-practice symbols, 5-practice all
mode=1
userInput=""
streak=0
index=0
text=""
screen = TelegraphDisplay.Screen()
battery = INA219.INA219(addr=0x43)

lineLength=13


morseCode = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '&': '.-...', '\'': '.----.', '@': '.--.-.', '(': '-.--.-', ')': '-.--.', ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '%': '------..-.-----', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.', '\\': '-.-.-', '\b': '----', '\n': '.-.-', ' ': '..--'
    }
    
def getBatteryPct():
    bus_voltage = battery.getBusVoltage_V()
    pct = (bus_voltage - 3)/1.2*100
    if(pct > 99):pct = 99
    if(pct < 0):pct = 0
    return(pct)

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
            line1="hint: "+morseCode[text[index].upper()]
        else:
            line1="streak: "+str(streak)
    line1=line1.ljust(lineLength)
    line1=line1[0:-2]
    line1+=str(getBatteryPct())
    #line 2
    fromIndex=max(0,index-lineLength)
    toIndex=min(len(text)-1,index+lineLength)
    line2=text[fromIndex:toIndex]
    line2=line2.rjust(lineLength)
    #line3
    line3=" "*(lineLength/2)
    line3+="^"
    #lines to display
    print(line1+"\n"+line2+"\n"+line3)
    screen.writeLines(line1,line2,line3)


def updateVals():
    global index
    global text
    global streak
    if mode==0:
        if userInput=="\b":
            #backspace
            index-=1
            text=text[0:-1]
        else:
            index+=1
            text+=userInput
    else:
        if text[index].upper()==userInput.upper():
            streak+=1
            index+=1
        else:
            streak=0

# def getCharFromUser():
#     #TODO
#     global userInput
#     userInput=input(" in ")[0].upper()

def getCharFromUser():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    global userInput
    userInput=str(ch).upper()


def main():
    global text
    print("Running...")
    text=loadText()
    while True:
        updateDisplay()
        getCharFromUser()
        updateVals()
        print(userInput)
        if userInput.upper() == '\x03':
            #capture ctrl-c to exit
            exit()
       

if __name__ == "__main__":
    main()
