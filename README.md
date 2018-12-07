# speaking-thermometer
A thermometer that tells you the temperature. It waits for a keyboard press and then calculates the temperature from a NTC Thermistor. Then it tells it to you.

## Images
Coming soon....

## Wiring
![speaking-thermometer-wireing](https://files.michadenheijer.com/speaking-thermometer.png)

## Dependencies
- [keybord](https://pypi.org/project/keyboard/)
- [playsound](https://pypi.org/project/playsound/)

## How to install
Firstly, download all the files you need.
```
git clone https://github.com/michadenheijer/speaking-thermometer
```
Then go to the directory
```
cd speaking-thermometer
```
You can test the program by running
```
sudo python button.py
```
If you want to run it permanently, copy the systemd service to it's proper location and enable it.

## Text-To-Speech
- [texttomp3.online](https://www.texttomp3.online/)
- [IBM Watson](https://text-to-speech-demo.ng.bluemix.net/)
