import PIL.Image
import PIL.ImageDraw
import face_recognition

# load jpg file to numpy array
image = face_recognition.load_image_file("people.jpg")

#find all the faces
face_locations = face_recognition.face_locations(image)

number_of_faces = len(face_locations)
print("i found {} faces in this photo".format(number_of_faces))

#load img into a python img library object, so that we can draw on top
pil_image = PIL.Image.fromarray(image)

for face_location in face_locations:
    top, left, bottom, right = face_location
    print("A face location: top: {}, left: {}, bottom: {}, right: {}".format(top, left, bottom, right))

    #draw a box around the faces
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="red")

#display the draw
pil_image.show()
