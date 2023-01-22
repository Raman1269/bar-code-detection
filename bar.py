## FOR STATIC IMAGE




# import cv2
# import numpy as np
# from pyzbar.pyzbar import  decode
# img=cv2.imread("Qrcode1.png")
# code= decode(img)
# print(code)

import cv2
import numpy as np
from pyzbar.pyzbar import  decode

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    ret,img=cap.read()
  
    for barcode in decode(img):
        print(barcode.rect)
        
        print(barcode.data)
   

        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,0),5)
        pts2=barcode.rect
        cv2.putText(img,str(barcode.data),(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    3,(255,0,0),2)

    cv2.imshow("image",img)
    cv2.waitKey(1)
