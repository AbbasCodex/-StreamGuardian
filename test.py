import cv2
import urllib.request
import numpy as np
from time import sleep

count = 0
files = "img"
filee = ".jpg"

StreamIP = '192.168.0.20'
StreamPort = '8080'

# Attempt to open the stream with a timeout
try:
    stream = urllib.request.urlopen(f'http://{StreamIP}:{StreamPort}/?action=stream', timeout=10)
    print("Connected to the stream successfully.")
except Exception as e:
    print(f"Error: Could not connect to the stream - {e}")
    exit(1)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

bytes_data = b""
while True:
    try:
        bytes_data += stream.read(1024)
        a = bytes_data.find(b'\xff\xd8')
        b = bytes_data.find(b'\xff\xd9')
        
        if a != -1 and b != -1:
            jpg = bytes_data[a:b+2]
            bytes_data = bytes_data[b+2:]
            img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            
            if img is None:
                print("Warning: Received an empty frame.")
                continue
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(faces) > 0:
                count += 1
                filename = f"{files}{count}{filee}"
                print(f"✅ Faces detected: {filename}")
                cv2.imwrite(filename, img)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            sleep(0.5)
            
            cv2.imshow("Face Detection", img)
            if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
                break

    except Exception as e:
        print(f"Error during processing: {e}")
        break

cv2.destroyAllWindows()
print("Stream closed.")
