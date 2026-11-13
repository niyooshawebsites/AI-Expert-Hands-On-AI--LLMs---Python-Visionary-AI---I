# Real time face detection
import cv2

# load the face the face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascades_frontalface_default.xml')

# access the webcam
cap = cv2.VideoCapture()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Can't access the camera")
        break

    gray = cv2.cvColor(frame, cv2.COLOR_BGR2GRAY)

    # detect the faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # draw rectangles
    for (x, y, w, h) in faces:
        cv2.reactangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # add label
        cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Count the number of faces
    cv2.putText(frame, f"Faces Detected: {len(faces)}", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # display the frame
    cv2.imshow("Realtime Face Detection", frame)

    # press 'q' to quit and exit
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break

# release the webcam
cap.release()
cv2.destroyAllWindows()