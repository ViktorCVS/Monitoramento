#include <dht.h>

#define    dht_pin    8   //pino de sinal do dht11 ligado no digital 5

dht   my_dht;   //objeto para o sensor

int    temperatura = 0x00,   //armazena a temperatura em inteiro
       umidade     = 0x00;   //armazena a umidade em inteiro
       
void setup() { 

 Serial.begin(9600);
 
}

void loop() {

 my_dht.read11(dht_pin);

 temperatura = my_dht.temperature;
 umidade     = my_dht.humidity;

 Serial.print(my_dht.temperature);
 Serial.print(",");
 Serial.println(my_dht.humidity);
 delay(1000);
 
 
}
