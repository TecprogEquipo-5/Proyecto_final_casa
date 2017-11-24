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
    for(int i = 0; i<=90; i++)
    {
      servoInstance.write(i);
      delay(20);
    }
    }
   if (inChar == 'c') {
       for(int i = 90; i>=0; i--)
     {
      servoInstance.write(i);
      delay(20);
     }
   }
   }


