#include <Servo.h>
Servo servoInstance;
int ledPIN_1 = 11;
int ledPIN_2 = 10;
int ledPIN_3 = 9;
int ledPIN_4 = 8;


void setup() {
 servoInstance.attach(5);
 Serial.begin(115200);
 
  pinMode(ledPIN_1, OUTPUT);
  digitalWrite(ledPIN_1, LOW);

  pinMode(ledPIN_2, OUTPUT);
  digitalWrite(ledPIN_2, LOW);

  pinMode(ledPIN_3, OUTPUT);
  digitalWrite(ledPIN_3, LOW);

  pinMode(ledPIN_4, OUTPUT);
  digitalWrite(ledPIN_4, LOW);

}

void loop() {
  }

void serialEvent() {
  char inChar = (char)Serial.read();
   if (inChar == 'o') {
   
      servoInstance.write(90);
  
    }
   if (inChar == 'x') {
     
      servoInstance.write(0);
     
     }
   if(inChar == 'A'){
        digitalWrite(ledPIN_1, HIGH);
  }
  if(inChar == 'a'){
        digitalWrite(ledPIN_1, LOW);
   }
      if(inChar == 'B'){
        digitalWrite(ledPIN_2, HIGH);
  }
  if(inChar == 'b'){
        digitalWrite(ledPIN_2, LOW);
  }
     if(inChar == 'C'){
        digitalWrite(ledPIN_3, HIGH);
  }
  if(inChar == 'c'){
        digitalWrite(ledPIN_3, LOW);
  }
     if(inChar == 'D'){
        digitalWrite(ledPIN_4, HIGH);
  }
  if(inChar == 'd'){
        digitalWrite(ledPIN_4, LOW);
  }
   if(inChar == 'T'){
        digitalWrite(ledPIN_4, HIGH);
        digitalWrite(ledPIN_3, HIGH);
        digitalWrite(ledPIN_2, HIGH);
        digitalWrite(ledPIN_1, HIGH);
  }
  if(inChar == 't'){
        digitalWrite(ledPIN_4, LOW);
        digitalWrite(ledPIN_3, LOW);
        digitalWrite(ledPIN_2, LOW);
        digitalWrite(ledPIN_1, LOW);
  }
}
   


