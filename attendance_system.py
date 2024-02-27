import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

def main():
    video_capture = cv2.VideoCapture(0)

    known_face_encodings, known_face_names = load_known_faces()

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")

    with open(current_date + '.csv', 'w+', newline='') as f:
        lnwriter = csv.writer(f)
        
        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Failed to capture frame")
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding, face_location in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            cv2.imshow("Attendance System", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video_capture.release()
    cv2.destroyAllWindows()

def load_known_faces():
    known_face_encodings = []
    known_face_names = []

    # Load known faces and encodings
    # Example:
    # ravi_image = face_recognition.load_image_file("photos/sanjana.jpg")
    # ravi_encoding = face_recognition.face_encodings(sanjana_image)[0]
    # known_face_encodings.append(ravi_encoding)
    # known_face_names.append("Ravi")

    return known_face_encodings, known_face_names

if __name__ == "__main__":
    main()
