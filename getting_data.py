import serial

arduino = serial.Serial("COM3",9600)

while True:
    print(arduino.readline())
