#define RED 8   
#define GREEN 12 

void setup() {
  Serial.begin(9600); 
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
}

void loop() {
  
  if (Serial.available() > 0) {
    char result = Serial.read(); 

    if (result == '1') { 
      digitalWrite(GREEN, HIGH);
      digitalWrite(RED, LOW);
      delay(2000); 
      digitalWrite(GREEN, LOW);
    } else if (result == '0') { 
      digitalWrite(RED, HIGH);
      digitalWrite(GREEN, LOW);
      delay(2000);
      digitalWrite(RED, LOW);
    }
  }
}
