// Define LED pin for demonstration
const int ledPin = 13;

// Variables to store received data
String incomingData = "";

void setup() {
  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);

  // Set LED pin as output
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  // Inform the user
  Serial.println("Arduino is ready!");
}

void loop() {
  // Check if data is available on the serial port
  if (Serial.available() > 0) {
    // Read the incoming string until a newline character
    incomingData = Serial.readStringUntil('\n');

    // Print received data to the serial monitor
    Serial.println("Received: " + incomingData);

    // Process the received data
    if (incomingData == "LED_ON") {
      digitalWrite(ledPin, HIGH);  // Turn LED on
      Serial.println("LED is ON");
    } else if (incomingData == "LED_OFF") {
      digitalWrite(ledPin, LOW);   // Turn LED off
      Serial.println("LED is OFF");
    } else {
      Serial.println("Unknown command: " + incomingData);
    }
  }

  // Optional: Add a small delay for stability
  delay(10);
}
