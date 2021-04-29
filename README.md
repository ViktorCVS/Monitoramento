# Monitoring

My project is based in get data from a temperature/humidity  sensor DHT11 with 'Arduino UNO' and plot a living graph with the data with Python.

I can divide this project in 3 steps:

 - [x] Assemble the circuit
 - [x] Program Arduino UNO
 - [x] Get data from python
 - [x] Plot the living graph

And those are the materials:

 - [x] Arduino UNO with USB cable for Arduino (or any other material that allow you to write a code in Arduino)
 - [x] DHT11 (Temperature/Humidity sensor)
 - [x] Protoboard (Optional)
 - [x] Wires/Jumpers

Arduino Libraries:

 - [x] dht.h (I uploaded it here)

Python Libraries (you can install them with 'pip install'):

 - [x] Matplotlib
 - [x] drawnow
 - [x] pyserial
 
## Assembling the circuit

DHT11 Sensor:

<img src="https://user-images.githubusercontent.com/69547580/116623279-64c8ed00-a91c-11eb-8b35-ca221810669f.jpg" width="600" height="600">

Arduino UNO:

<img src="https://user-images.githubusercontent.com/69547580/116623277-64305680-a91c-11eb-89d9-973fbdeeacd7.jpg" width="600" height="600">

Squematic:

<img src="https://user-images.githubusercontent.com/69547580/116623645-f0427e00-a91c-11eb-9579-1b6a2539f217.jpg" width="825" height="450">

Assembled circuit:

<img src="https://user-images.githubusercontent.com/69547580/116624159-d05f8a00-a91d-11eb-8bee-ee63a4899e72.jpg" width="750" height="600">

We can see that I put the '-' terminal of DHT11 at ground, middle terminal at VCC +5V (Arduino) and 'S' terminal for data at pin '8'.

## Results

### Arduino Results

![dataarduino](https://user-images.githubusercontent.com/69547580/116628913-8202b900-a926-11eb-88bb-d3059646a79c.jpg)

The serial port works fine.

### Python 'getting_data.py' Results

![datapython1](https://user-images.githubusercontent.com/69547580/116628996-aeb6d080-a926-11eb-8aa4-12227c23e472.jpg)

We get data from COM3 with sucess!

### Python 'plotting_tu.py' Results









