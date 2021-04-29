# Monitoring

My project is based in get data from a temperature/umidity sensor DHT11 with 'Arduino UNO' and plot a living graph with the data with Python.

I can divide this project in 3 steps:

 - [x] Assemble the circuit
 - [x] Program Arduino UNO
 - [x] Get data from python
 - [x] Plot the living graph

And those are the materials:

 - [x] Arduino UNO with USB cable for Arduino (or any other material that allow you to write a code in Arduino)
 - [x] DHT11 (Temperature/Umidity sensor)
 - [x] Protoboard (Optional)
 - [x] Wires/Jumpers
 
## Assembling the circuit

DHT11 Sensor:

<img src="https://user-images.githubusercontent.com/69547580/116623279-64c8ed00-a91c-11eb-8b35-ca221810669f.jpg" width="600" height="600">

Arduino UNO:

<img src="https://user-images.githubusercontent.com/69547580/116623277-64305680-a91c-11eb-89d9-973fbdeeacd7.jpg" width="600" height="600">

Squematic:

<img src="https://user-images.githubusercontent.com/69547580/116623645-f0427e00-a91c-11eb-9579-1b6a2539f217.jpg" width="825" height="450">

Assembled circuit:

<img src="https://user-images.githubusercontent.com/69547580/116624159-d05f8a00-a91d-11eb-8bee-ee63a4899e72.jpg" width="750" height="600">

We can see that i put the '-' terminal of DHT11 at ground, middle terminal at VCC +5V (Arduino) and 'S' terminal for data at pin '8'.

## Results

The second, third and fourth step can be seen at code arduino_sensor.ino, getting_data.py and plotting_tu.py. Now i'm gonna apresent the results.









