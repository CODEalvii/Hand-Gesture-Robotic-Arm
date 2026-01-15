#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Define servo positions
#define SERVO_MIN 120 // Minimum pulse length count
#define SERVO_MAX 620 // Maximum pulse length count

void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(50); // Set frequency to 50 Hz
  Serial.println("Arduino Ready!");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read command in the format "0:1"
    int colonIndex = command.indexOf(':');
    if (colonIndex > 0) {
      int servoId = command.substring(0, colonIndex).toInt(); // Extract servo ID
      int action = command.substring(colonIndex + 1).toInt(); // Extract action (0 or 1)

      // Move the servo to the appropriate position
      if (servoId >= 0 && servoId < 16) {
        int position = (action == 1) ? SERVO_MAX : SERVO_MIN;
        pwm.setPWM(servoId, 0, position);
        Serial.println("Servo " + String(servoId) + " moved to " + (action == 1 ? "MAX" : "MIN"));
      }
    }
  }
}
