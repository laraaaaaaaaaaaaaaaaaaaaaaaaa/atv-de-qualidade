import cv2
import numpy as np
from keras.models import load_model


model = load_model('libras_model.h5')

x, y, w, h = 300, 100, 300, 300


cap = cv2.VideoCapture(0)

while True:
   
    ret, frame = cap.read()

    
    roi = frame[y:y+h, x:x+w]

    
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

   
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

  
    resized = cv2.resize(threshold, (50, 50))

   
    image_array = np.array(resized).reshape(-1, 50, 50, 1)

    
    image_array = image_array / 255.0

    
    prediction = model.predict(image_array)

    
    gesture = chr(prediction.argmax() + 65)

    
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

   
    cv2.putText(frame, gesture, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

   
    cv2.imshow('Video', frame)

    
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

