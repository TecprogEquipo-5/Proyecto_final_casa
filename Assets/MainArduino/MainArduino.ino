#include <Servo.h>
Servo servoInstance;
int ledPIN_1 = 11;
int ledPIN_2 = 10;
int ledPIN_3 = 9;
int ledPIN_4 = 8;
int fanPIN_1 = 13;

int sensorTemperaturePIN = A0;
int sensorValueTemp = 0;

int sensorMovePIN = A1;
int sensorValueMove = 0;





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

  pinMode(fanPIN_1, OUTPUT);
  digitalWrite(fanPIN_1, LOW);

}

void loop() {
  int sensorValueTemp = analogRead(sensorTemperaturePIN);
  int sensorValueMove = analogRead(sensorMovePIN);
  sendData(sensorValueTemp, sensorValueMove);
  delay(50);
  }

void sendData(int value_temp, int value_move) {
  Serial.print(value_temp);
  Serial.print(",");
  Serial.println(value_move);
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

  if(inChar == 'F'){
        digitalWrite(fanPIN_1, HIGH);
  }

  if(inChar == 'f'){
        digitalWrite(fanPIN_1, LOW);
  }
}

   


