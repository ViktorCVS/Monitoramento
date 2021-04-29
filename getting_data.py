import serial #Importing library to get data from serial

arduino = serial.Serial("COM3",9600) #Getting data from "COM3" port with 9600 Bald Rate (we set it in .ino code)

while True:
    
    #Infinity loop to get data in real time without a stop condition
    
    print(arduino.readline())  #printing in terminal the result
