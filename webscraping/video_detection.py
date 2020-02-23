import cv2
video = cv2.VideoCapture("video.avi")
face_c = cv2.CascadeClassifier("cars.xml")

while True:
    check, frame =video.read()
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_c.detectMultiScale(gray_img,
    scaleFactor=1.05,
    minNeighbors=5)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
    cv2.imshow("video",frame)
    key = cv2.waitKey(25)
    if(key == ord('q')):
        break
    # resized = cv2.resize(img,(int(img.shape[0]/3),int(img.shape[0]/3)))


cv2.destroyAllWindows
video.release()