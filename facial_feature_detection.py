import PIL.Image
import PIL.ImageDraw
import face_recognition

#load jpg into a numpy array
image = face_recognition.load_image_file("people.jpg")

#find facial features
face_landmarks_list = face_recognition.face_landmarks(image)

number_of_faces = len(face_landmarks_list)
print("{} faces detected".format(number_of_faces))

#load the image into a python image library object, so that we can draw on it
pil_image = PIL.Image.fromarray(image)

#create PIL drawing object
draw = PIL.ImageDraw.Draw(pil_image)

#look the faces
for face_landmarks in face_landmarks_list:

    #loop over each facial feature(eye, nose, mouth, lips, etc)
    for name, list_of_points in face_landmarks.items():

        #print the location of each feature
        print("{} in this face has these points: {}".format(name, list_of_points))

        #trace out each facial feature
        draw.line(list_of_points, fill="red", width=2)

pil_image.show()
