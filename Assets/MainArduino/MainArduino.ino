#include <Servo.h>
Servo servoInstance;

void setup() {
 servoInstance.attach(5);
 Serial.begin(115200);

}

void loop() {
  serialEvent_servo();
  }

void serialEvent_servo() {
  char inChar = (char)Serial.read();
   if (inChar == 'o') {
   
      servoInstance.write(90);
  
    }
   if (inChar == 'c') {
     
      servoInstance.write(0);
     
     }
   }
   


