const int enableA =9;
const int enableB =10;
const int in1 =2;
const int in2 =3;
const int in3 =4;
const int in4 =5;
int motorSpeedA =0;
int motorSpeedB =0;


void setup(){
  pinMode(enableA, OUTPUT);
  pinMode(enableB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  Serial.begin(9600);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enableA, 0);
  analogWrite(enableB, 0);
}

void loop(){
  if(Serial.available() > 0){
    int receivedValue = Serial.parseInt();

  if (receivedValue == 255){
    analogWrite(enableA, 0);
    analogWrite(enableB, 0);
    Serial.println("Motor stopped");
    
    
  }  else{
    motorSpeedA= constrain(receivedValue, 0, 254);
    motorSpeedB= constrain(receivedValue, 0, 254);
    analogWrite(enableA, motorSpeedA);
    analogWrite(enableA, motorSpeedB);
    analogWrite(enableB, motorSpeedA);
    analogWrite(enableB, motorSpeedB);
    Serial.print("Motor Speed:");
    Serial.println(motorSpeedA);
    Serial.println(motorSpeedB);
  }
  }
}
