import face_recognition
import cv2
import numpy as np

known_face_encodings = []
known_face_names = []

person1_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Soha.jpg")
person1_face_encoding = face_recognition.face_encodings(person1_image)[0]
known_face_encodings.append(person1_face_encoding)
known_face_names.append("Soha")

person2_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Harsha.jpg")
person2_face_encoding = face_recognition.face_encodings(person2_image)[0]
known_face_encodings.append(person2_face_encoding)
known_face_names.append("Harsha")

person3_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Vaishnavi.jpg")
person3_face_encoding = face_recognition.face_encodings(person3_image)[0]
known_face_encodings.append(person3_face_encoding)
known_face_names.append("Vaishnavi")

person4_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Gargi.jpg")
person4_face_encoding = face_recognition.face_encodings(person4_image)[0]
known_face_encodings.append(person4_face_encoding)
known_face_names.append("Gargi")

person5_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Gauri.jpg")
person5_face_encoding = face_recognition.face_encodings(person5_image)[0]
known_face_encodings.append(person5_face_encoding)
known_face_names.append("Gauri")

person6_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Elon Musk.jpg")
person6_face_encoding = face_recognition.face_encodings(person6_image)[0]
known_face_encodings.append(person6_face_encoding)
known_face_names.append("Elon Musk")

person7_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Jeff Bezoz.jpg")
person7_face_encoding = face_recognition.face_encodings(person7_image)[0]
known_face_encodings.append(person7_face_encoding)
known_face_names.append("Jeff Bezoz")

person8_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Messi.jpg")
person8_face_encoding = face_recognition.face_encodings(person8_image)[0]
known_face_encodings.append(person8_face_encoding)
known_face_names.append("Messi")

person9_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Ryan Reynolds.jpg")
person9_face_encoding = face_recognition.face_encodings(person9_image)[0]
known_face_encodings.append(person9_face_encoding)
known_face_names.append("Ryan Reynolds")

person10_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Sushama Maam.jpeg")
person10_face_encoding = face_recognition.face_encodings(person10_image)[0]
known_face_encodings.append(person10_face_encoding)
known_face_names.append("Sushama Ma'am")

person11_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Sunil sir.jpeg")
person11_face_encoding = face_recognition.face_encodings(person11_image)[0]
known_face_encodings.append(person11_face_encoding)
known_face_names.append("Sunil sir")

person12_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Mrudula maam.jpeg")
person12_face_encoding = face_recognition.face_encodings(person12_image)[0]
known_face_encodings.append(person12_face_encoding)
known_face_names.append("Mrudula Ma'am")

person13_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Vishal sir.jpeg")
person13_face_encoding = face_recognition.face_encodings(person13_image)[0]
known_face_encodings.append(person13_face_encoding)
known_face_names.append("Vishal sir")

person14_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Ratan Tata sir.jpeg")
person14_face_encoding = face_recognition.face_encodings(person14_image)[0]
known_face_encodings.append(person14_face_encoding)
known_face_names.append("Ratan Tata Sir")

person15_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Dad.jpg")
person15_face_encoding = face_recognition.face_encodings(person15_image)[0]
known_face_encodings.append(person15_face_encoding)
known_face_names.append("Dad")

person16_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Mom.jpg")
person16_face_encoding = face_recognition.face_encodings(person16_image)[0]
known_face_encodings.append(person16_face_encoding)
known_face_names.append("Mom")

person17_image = face_recognition.load_image_file("/Users/sohashaikh/Desktop/object detection open cv/Simran dii.jpg")
person17_face_encoding = face_recognition.face_encodings(person17_image)[0]
known_face_encodings.append(person17_face_encoding)
known_face_names.append("Simran dii ")




face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.75, (255, 255, 255), 1)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
