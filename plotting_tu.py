import matplotlib.pyplot as plt  #Importing library to plot our graph
from drawnow import *            #Importing library to draw the graph in real time
import serial                    #Importing library to get data from serial port

temp = [] #Temperature array
umi = []  #Humidity array

cnt = 0 #Counter to avoid plot a huge array at the same time

arduino = serial.Serial("COM3",9600) #Getting data from 'COM3' port with 9600 Bald Rate

plt.ion() #Setting in matplotlib that we're gonna plot a living graph

def figure():
    
    #Function to plot the graph
    
    plt.ylim(25,35) #Temperature limits
    plt.title("Temperatura e umidade relativa do meu quarto") #Graph Title
    plt.grid(True) #Grid on
    plt.ylabel("Temperature (°C)") #Label at left y axis
    plt.xlabel("Passed seconds") #Label at x axis
    plt.plot(temp,"ro-",label="Temperature") #Plotting temperature
    plt.legend(loc='upper left') #Setting temperature label at upper left
    plt2=plt.twinx() #Adding a second plot
    plt.ylim(50,90) #Setting it's limits
    plt.ylabel("Humidity (%)") #Label at right y axis
    plt2.plot(umi,'b^-',label="Humidity") #Plotting humidity
    plt.legend(loc='upper right') #Setting humidity label at upper right

while True:
    
    #Infinite Loop to get our data in real time without stop condition
    
    while (arduino.inWaiting()==0):
        
        #Loop to do nothing when there's no data
        
        pass
    
    arduino_string = arduino.readline().decode("utf-8")  #Getting data as "b'xx.xx,yy.yy\r\n" and decoding it to "xx.xx,yy.yy"
    dataarray = arduino_string.split(",") #Separating data in a array, array[0] for temperature and array[1] for humidity (see .ino code, temperature first)
    temp.append(float(dataarray[0])) #Putting temperature data in a temperature array
    umi.append(float(dataarray[1]))  #Putting humidity data in a humidity array
    drawnow(figure) #Calling 'figure' function with drawnow
    plt.pause(.000001) #A small pause on plt
    cnt += 1  #Increasing counter
    if(cnt>60):
        
        #If we get more than 60 values in each array, delete the first element, to avoid plot all of them
        #It will be done everytime after cnt>60, so it will show us a graph from the last minute, since we get a data each second (.ino code)
        
        temp.pop(0)
        umi.pop(0)
    

