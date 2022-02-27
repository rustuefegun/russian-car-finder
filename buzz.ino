int led = 5;
#include <Servo.h>

Servo motor;
int value;
int angle;

char data;
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  motor.attach(6);


}

void loop() {
  
  if(Serial.available()){
  data = Serial.read();
  Serial.println(data);
  
  if (data == 'o'){
    Serial.println("led şuan yanıyor.");
    digitalWrite(led,HIGH);
  }
  if (data == 'f'){
    Serial.println("led şuan yanmıyor.");
    digitalWrite(led,LOW);
  }
  if(data== 's'){
    Serial.println("servo 180 derece konumuna getirildi.");
    motor.write(180);
  }
  if(data== 'r'){
    Serial.println("servo 0 derece konumuna getirildi.");
    motor.write(0);
  }
  }
}
