import cv2
from cvzone.HandTrackingModule import HandDetector
import serial
import time

# Initialize the hand detector
detector = HandDetector(maxHands=1, detectionCon=0.8)

# Initialize serial communication
try:
    serial_comm = serial.Serial("COM3", 9600, timeout=1)  # Replace COM3 with your port
    time.sleep(2)  # Wait for the serial connection to stabilize
except Exception as e:
    print(f"Error initializing serial communication: {e}")
    serial_comm = None

# Start video capture
cap = cv2.VideoCapture(0)

# Servo IDs mapped to fingers
finger_to_servo = {
    "thumb": 0,
    "index": 1,
    "middle": 2,
    "ring": 3,
    "pinky": 4
}

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from camera.")
        continue

    hands = detector.findHands(img, draw=True)
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)  # Get a list of 1 (open) or 0 (closed)

        # Send commands for each finger
        if serial_comm:
            for i, is_open in enumerate(fingers):
                servo_id = finger_to_servo[list(finger_to_servo.keys())[i]]
                command = f"{servo_id}:{'1' if is_open else '0'}\n"  # Format: "0:1\n" (servo 0 open)
                serial_comm.write(command.encode())

    # Display the webcam feed
    cv2.imshow("Hand Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
if serial_comm:
    serial_comm.close() 
