import cv2
import numpy as np
from ultralytics import YOLO

def patch_image(img, results):
    boxes = results[0].boxes.xyxy
    for box in boxes:
        x1, y1, x2, y2 = box[0], box[1], box[2], box[3] 
        pt1 = (int(x1), int(y1))
        pt2 = (int(x2), int(y2))
        cv2.rectangle(img, pt1, pt2, (0, 0, 255), 5)
        id = results[0].boxes.cls[0].item() if len(results[0].boxes.cls) > 0 else -1
        if id !=-1:
            print(results[0].names[int(id)])
            cl = results[0].names[int(id)] # class name
            conf = results[0].boxes.conf[0].item() # confidence score
            cv2.putText(img, f'{cl} {conf:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,color= (0, 255, 0), thickness=3)
        else:
            print("nothing detected")
 

    return img

model = YOLO('best.pt')

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('FEED', frame)
    img = np.asarray(frame)
    results = model.predict(img)
    patched_img = patch_image(img, results)
    cv2.imshow('FEED', patched_img)
    id = results[0].boxes.cls[0].item() if len(results[0].boxes.cls) > 0 else -1
    if id !=-1:
        print(results[0].boxes)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()