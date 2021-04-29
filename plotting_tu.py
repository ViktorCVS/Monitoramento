import matplotlib.pyplot as plt  #Importing library to plot our graph
from drawnow import *            #Importing library to draw the graph in real time
import serial                    #Importing library to get data from serial port

temp = [] #Temperature array
umi = []  #Humidity array

cnt = 0

arduino = serial.Serial("COM3",9600)
plt.ion()

def figura():
    plt.ylim(25,35)
    plt.title("Temperatura e umidade relativa do meu quarto")
    plt.grid(True)
    plt.ylabel("Temperatura (°C)")
    plt.xlabel("Segundos transcorridos")
    plt.plot(temp,"ro-",label="Temperatura")
    plt.legend(loc='upper left')
    plt2=plt.twinx()
    plt.ylim(50,90)
    plt.ylabel("Umidade relativa (%)")
    plt2.plot(umi,'b^-',label="Umidade Relativa")
    plt.legend(loc='upper right')

while True:
    while (arduino.inWaiting()==0):
        pass
    arduino_s = arduino.readline().decode("utf-8") 
    arduino_s = arduino_s[:-2]
    dataarray = arduino_s.split(",")
    temp.append(float(dataarray[0]))
    umi.append(float(dataarray[1]))
    drawnow(figura)
    plt.pause(.000001)
    cnt += 1
    if(cnt>60):
        temp.pop(0)
        umi.pop(0)
    

