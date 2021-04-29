#include <dht.h> //importing dht11 library

#define    dht_pin    8   //Setting pin 8 to get data from the sensor

dht   my_dht;   //objeto para o sensor

int    temperatura = 0x00,   //Store temperature as an integer
       umidade     = 0x00;   //Store humidity as an integer
       
void setup() { 

 Serial.begin(9600); //Stating the serial output with 9600 Bald Rate
 
}

void loop() {

 my_dht.read11(dht_pin); //In loop, reading each time the values from the sensor

 Serial.print(my_dht.temperature); //Sending the temperature for serial
 Serial.print(","); //Separating values with ',' to be easier to get this data in Python
 Serial.println(my_dht.humidity); //Sending the humidity for serial
 delay(1000); //Get data from sensor each 1 second
 
 
}
