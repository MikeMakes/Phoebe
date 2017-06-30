#include <Servo.h>

unsigned long readULongFromBytes() {
  union u_tag {
    byte b[4];
    unsigned long ulval;
  } u;
  u.b[0] = Serial.read();
  u.b[1] = Serial.read();
  u.b[2] = Serial.read();
  u.b[3] = Serial.read();
  return u.ulval;
}

int readInt() {
  int mil,cent,dec,uni;
  mil = Serial.read();
  mil=mil*1000;
  cent=Serial.read();
  cent=cent*100;
  dec = Serial.read();
  dec=dec*10;
  uni= Serial.read();
  return (mil+cent+dec+uni);
}

//unsigned long val = readULongFromBytes();

char control;
int valueR;
int valueL;

Servo leftESC, rightESC; //Create as much as Servoobject you want. You can controll 2 or more Servos at the same time

void setup() {

  leftESC.attach(9);  // attached to pin 9 
  rightESC.attach(10); //attached to pn 10
  
  Serial.begin(9600);    // start serial at 9600 baud
  
//First connect your ESC WITHOUT Arming. Then Open Serial and follo Instructions
  //leftESC.writeMicroseconds(value);
  //rightESC.writeMicroseconds(value);
  
  while(!Serial){
  }
}

void loop() {
 
  rightESC.writeMicroseconds(valueR);
  leftESC.writeMicroseconds(valueL);
  
   if(Serial.available()){
     control=Serial.read();
     Serial.println(control);
     if (control=='R'){
       Serial.println("You man are yeah in Right control.");
       do {
         valueR = 0;
         int i;
         for (i=0;i<4;i++){
           if (Serial.available()>0)
             valueR = valueR + (Serial.read()-48)*pow(10,i);
         }
         //valueR = Serial.parseInt();
        } while (valueR < 1000);
       
       Serial.println("Este es el valor: ");
       Serial.println(valueR);
       rightESC.writeMicroseconds(valueR);
     }
     else if (control=='L'){
       Serial.println("You madafaca are yeah in Left control. ");
       do {
         valueL=0;
         valueL = readULongFromBytes();
         valueL = int(valueR);
        } while (valueL < 1000 && valueL > 2000);
      Serial.println("Este es el valor: ");
      Serial.println(valueL);
      leftESC.writeMicroseconds(valueL);
     }
   }
}
