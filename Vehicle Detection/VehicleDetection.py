import cv2

cap=cv2.VideoCapture(r'cars.mp4')

car_cascade=cv2.CascadeClassifier(r'cars.xml')

while True:
	ret,frames=cap.read()

	gray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)

	cars=car_cascade.detectMultiScale(gray,1.1,1)

	for (x,y,w,h) in cars:
		cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
		font=cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frames,'Car',(x+6,y-6),font,0.5,(0,0,255),1)
		cv2.imshow('Car Detection',frames)
	if cv2.waitKey(33)==13:
		break


cap.realease()
cv2.destroyAllWindows()