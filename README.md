Hand Gesture Controlled Robtic Hand 

This project uses OpenCV,CVZone, and Arduino to control five servo motors using hand gestures detected via webcam.

Each finger controls a specific servo motor in real-time using serial communication.


 Technologies Used
 Python
 OpenCV
 CVZone
 MediaPipe
 Arduino
 PCA9685 (16-Channel Servo Driver)
 SG90 9g Mini Servo Motors


 How It Works
1. Webcam detects hand using OpenCV + CVZone
2. Fingers are detected (open / closed)
3. Python sends serial commands to Arduino
4. Arduino controls servos via PCA9685 driver



Finger to Servo Mapping
| Finger  | Servo Channel 
| Thumb  | 0 |
| Index  | 1 |
| Middle | 2 |
| Ring   | 3 |
| Pinky  | 4 |


 Hardware Required
Arduino UNO / Nano
PCA9685 Servo Driver
5 × SG90 Servo Motors
External 5V Power Supply


 Setup Instructions

 Install Python dependencies
 Install Arduino IDE.
