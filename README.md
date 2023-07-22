# PiTelegraphDisplay
A small display unit for a keyboard input. It is specifically designed to pair with the PicoTelegraphKey Repo. Built using the Raspberry Pi Zero.


## Setup
1. Install a lite version of the Raspberry PI OS on a SD Card
0. On the PI
  1. `sudo raspi-config`
  2. choose: "Interfacing Options > SPI > Yes Open SPI Interface"
  3. choose: "Interfacing Options > I2C > Yes Open I2C Interface"
  4. Restart the PI
  5. `sudo apt-get update`
     `sudo apt-get install python3-pip`
     `sudo apt-get install python3-pil`
     `sudo apt-get install python3-numpy`
     `sudo pip3 install RPi.GPIO`
     `sudo pip3 install spidev`
     `sudo pip3 install Adafruit-PureIO`
2. Download this repo to the PI
  1. `sudo apt-get update`
  2. `sudo apt-get install git`
  3. `sudo pip3 install smbus`
  4. `git clone https://github.com/abitwitch/PiTelegraphDisplay.git`
3. Set `startup.sh` to run on startup
  1. `chmod +x startup.sh`
  2. `sudo nano /etc/rc.local`
  3. Add these lines to the end: 
    `cd /path/to/PiTelegraphDisplay`
    `sudo bash startup.sh`
4. TODO: opimize boot



## Modes
0. Menu 
  - help: . >     _ enter
1. Just type
2. Practice
  1. Alpha
  2. Numeric
  3. Symbols
  4. AlphaNumeric
  5. All



NEXT:
1. Menu
