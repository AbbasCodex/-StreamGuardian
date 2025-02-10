⚙ Requirements

🖥 Hardware
IP Camera (ESP32-CAM, Raspberry Pi Camera, or any MJPEG-supported camera)
Computer (Linux, Mac, or Windows)
Stable Network Connection
🛠 Software & Dependencies
Python 3.7+
OpenCV (cv2)
NumPy
🚀 Installation & Setup

Step 1: Install Dependencies
pip install opencv-python numpy
Step 2: Configure Your IP Camera
Find your camera’s stream URL and update the script:

StreamIP = '192.168.0.20'  # Replace with your camera's IP
StreamPort = '8080'  # Replace with your camera's Port
Step 3: Run the Script
Execute the script:

python test.py
Step 4: Check for Output
The camera feed will open with face detection boxes.
Detected faces will be saved as img1.jpg, img2.jpg, etc.
Press ESC to exit.
🔧 Troubleshooting

No Output / Stream Not Working?
✅ Check if the camera is reachable:

ping 192.168.0.20
✅ Test the URL in a browser:

http://192.168.0.20:8080/?action=stream
✅ Ensure the camera and computer are on the same WiFi/LAN.

ModuleNotFoundError: No module named ‘cv2’
Run:

pip install opencv-python
ImportError: libGL.so.1: cannot open shared object file
Fix for Linux:

sudo apt install libgl1 libglib2.0-0
🚀 Future Enhancements

🔹 Cloud Storage Integration (Save images to Google Drive / AWS S3)
🔹 Face Recognition (Instead of just detection)
🔹 Web Dashboard (View live stream remotely)

📌 Contributions
Feel free to fork, modify, and contribute! 💡
