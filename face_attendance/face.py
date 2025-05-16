import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Step 1: Load images and extract names
path = 'Images'
images = []
classNames = []

if not os.path.exists(path):
    print(f"Folder '{path}' not found.")
    exit()

myList = [f for f in os.listdir(path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is not None:
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    else:
        print(f"Could not read image: {cl}")

# Encode faces
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(img)
        if encodes:
            encodeList.append(encodes[0])
        else:
            print("Face not found in one image.")
    return encodeList

encodeListKnown = findEncodings(images)
print("Encoding complete.")

# Mark attendance
import os

def markAttendance(name):
    filename = 'Attendance.csv'
    
    # Create the file if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write('Name,Time\n')  # header
    
    # Now safely open it for read and append
    with open(filename, 'r+') as f:
        myDataList = f.readlines()      
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            print(f"📝 Marked: {name} at {dtString}")


# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success or img is None:
        print("❌ Failed to read frame from webcam.")
        continue

    # Resize and convert frame
    imgSmall = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    #  Detect faces in frame
    facesCurrentFrame = face_recognition.face_locations(imgSmall)
    encodesCurrentFrame = face_recognition.face_encodings(imgSmall, facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            # Scale face location back to original size
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            markAttendance(name)

    cv2.imshow('Webcam - Face Recognition Attendance', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
