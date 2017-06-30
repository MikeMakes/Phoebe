#include <Servo.h>

int rm = A0;
int lm = A1;
int valueR, valueL;
float valueRf, valueLf;

Servo leftESC, rightESC;

void setup() {

  leftESC.attach(9);  // attached to pin 9 
  rightESC.attach(10); //attached to pn 10
}

void loop(){
 valueR = analogRead(rm);
 valueL = analogRead(lm);
 
 valueRf=float(log(valueR)*100);
 valueLf=float(log(valueL)*100);
 
 valueR=map(valueR,0,255,1000,2000);
 valueL=map(valueL,0,255,1000,2000);
 
 rightESC.writeMicroseconds(valueR);
 leftESC.writeMicroseconds(valueL);

  
}
  
