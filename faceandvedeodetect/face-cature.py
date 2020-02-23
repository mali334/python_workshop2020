import cv2

face_c = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("photo3.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_c.detectMultiScale(gray_img,
scaleFactor=2.1,
minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

print(type(faces))
print(faces)

resized = cv2.resize(img,(int(img.shape[0]/3),int(img.shape[0]/3)))

cv2.imshow("gray",resized)
cv2.waitKey(20000)
cv2.destroyAllWindows
