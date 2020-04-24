import face_recognition

#load images into numpy array
image_of_person_1 = face_recognition.load_image_file("person_1.jpg")
image_of_person_2 = face_recognition.load_image_file("person_2.jpg")
image_of_person_3 = face_recognition.load_image_file("person_3.jpg")

#get the face encodings of each person.
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]
person_2_face_encoding = face_recognition.face_encodings(image_of_person_2)[0]
person_3_face_encoding = face_recognition.face_encodings(image_of_person_3)[0]

#create list of all known face encodings
known_face_encodings = [
    person_1_face_encoding,
    person_2_face_encoding,
    person_3_face_encoding
]

# load the image to check
unknown_image = face_recognition.load_image_file("unknown_8.jpg")

# get face encodings for people in the picture
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

#loop over in case of multiple faces
for unknown_face_encoding in unknown_face_encodings:

    #test if unknown face matches
    results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, tolerance=0.6)

    name = "Unknown"

    if results[0]:
        name = "person 1"
    elif results[1]:
        name = "person 2"
    elif results[2]:
        name = "person 3"
    print(f"found {name} in the photo")
