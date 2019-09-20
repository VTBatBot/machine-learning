int analogPin1 = A3;
int outvalue1 = 0;
int A[1000];
int B[1000];
int C[1000];


#include <SPI.h>
#include <SD.h>
#include <stdio.h>

File myFile;



void setup() {

pinMode(13, OUTPUT);
pinMode(analogPin1,INPUT);

//Measuring data into array A
for (int i=1;i<1000;i++){
A[i]=analogRead(analogPin1);
}

//SD card initialization and print
SD.begin(SDCARD_SS_PIN);
SD.remove("A.txt");
myFile = SD.open("A.txt", FILE_WRITE);

for (int i=1;i<1000;i++){
myFile.println(A[i]);
}
myFile.close();


//Delay 10 seconds before taking new data

for(int i=1;i<5;i++){
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second

}
}






void loop() {

//reset Arrays
  int C[1000];
  int A[1000];
  int B[1000];

//measure new data
for (int i=1;i<=1000;i++){
A[i]=analogRead(analogPin1);
}

//import old data to array B
myFile = SD.open("A.txt");
for (int i=1;i<=1000;i++){
B[i]=myFile.read();
}
myFile.close();

//Delete text file
SD.remove("A.txt");


//Compare new vs old data for higher value into array C

for (int i=1;i<=1000;i++){
  if (A[i]>= B[i]) {
    C[i]=A[i];} 
 else {
    C[i] = B[i]; }
  }

  
  
//export Array C
SD.begin(SDCARD_SS_PIN);
myFile = SD.open("A.txt", FILE_WRITE);
for (int i=1;i<1000;i++){
myFile.println(C[i]);
}
myFile.close();

//Delay loop 10 seconds

for(int i=1;i<5;i++){
  digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);              // wait for a second
}

}
