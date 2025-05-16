FACE RECOGNITION ATTENDANCE SYSTEM
==================================

Description:
------------
This is a Python-based attendance system that uses face recognition to automatically mark attendance using a webcam. It detects faces in real-time, compares them with known faces, and saves the name and time of recognition into a CSV file.

Features:
---------
- Real-time face detection and recognition
- Marks attendance automatically
- Saves attendance with time to a CSV file
- Easy to add new people by saving their images

Requirements:
-------------
Install these Python libraries before running:

- opencv-python
- face_recognition
- numpy

Use pip:
pip install opencv-python face_recognition numpy

If you face issues installing face_recognition or dlib:
- Install cmake first
- Use Anaconda or precompiled wheels

How to Use:
-----------
1. Create a folder named "Images" in the same directory.
2. Add face images (like "Alice.jpg", "Bob.png") to the folder.
3. Run the Python script:
   python face.py
4. Sit in front of the webcam. If your face matches, attendance is recorded.
5. A CSV file named "Attendance.csv" will be created with names and timestamps.

How It Works:
-------------
- Encodes all known faces from the Images folder.
- Opens webcam and reads live video feed.
- Detects and encodes faces in the video.
- Matches live faces with known encodings.
- If a match is found, logs name and time into Attendance.csv.

Sample Attendance.csv:
-----------------------
Name,Time
Alice,09:21:43
Bob,09:22:15

Possible Improvements:
-----------------------
- Save attendance files by date (e.g., Attendance_2025-05-15.csv)
- Add GUI using Tkinter
- Deploy on Raspberry Pi
- Add liveness detection to prevent spoofing
- Export to Excel format

Author:
-------
Sainath Kotage
ECE 4th Sem
Guru Ghasidas University 
Email: kotagesai@gmail.com
GitHub: https://github.com/Sainathkotage

License:
--------
Free to use for educational and non-commercial projects.
