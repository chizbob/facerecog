import face_recognition

#load jpg into numpy array
image = face_recognition.load_image_file("person.jpg")

#generate face encodings (multi-step process)
face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0: #no faces detected
    print("no faces were found")

else:
    #grab the first face encoding
    first_face_encoding = face_encodings[0]
    print(first_face_encoding)
