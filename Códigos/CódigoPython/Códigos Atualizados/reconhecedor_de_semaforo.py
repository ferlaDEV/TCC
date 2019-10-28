# -*- coding: utf-8 -*-


#Importando as bibliotecas utilizadas
import cv2
import numpy as np

#Pega a imagem da webcam
cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    try:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
        hsv2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv3 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red = np.array([3,100,69])
        upper_red = np.array([0,50,100])

        lower_green = np.array([70,150,100])
        upper_green = np.array([70,255,255])

        lower_yellow = np.array([20,130,100])
        upper_yellow = np.array([20,255,255])

        maskRed = cv2.inRange(hsv, lower_red, upper_red)
        maskGreen = cv2.inRange(hsv2, lower_green, upper_green)
        maskYellow = cv2.inRange(hsv3, lower_yellow, upper_yellow)
        # res = cv2.bitwise_and(frame,frame, mask= mask)

        x, y, w, h = cv2.boundingRect(maskGreen)
        if x!=0 and y!=0 and w!=0 and h!=0: print "verde!!!\n"
        x1, y1, w1, h1 = cv2.boundingRect(maskRed)
        if x1!=0 and y1!=0 and w1!=0 and h1!=0: print "vermelho!!!\n"
        x2, y2, w2, h2 = cv2.boundingRect(maskYellow)
        if x2!=0 and y2!=0 and w2!=0 and h2!=0: print "amarelo!!!\n"
 
        cv2.rectangle(frame, (x1, y1), (x1+w1, y1 + h1), (0, 0, 255), 3)
        cv2.circle(frame, (x1+w1/2, y1+h1/2), 5, (0, 0, 255), -1)

        cv2.rectangle(frame, (x, y), (x+w, y + h), (0, 255, 0), 3)
        cv2.circle(frame, (x+w/2, y+h/2), 5, (0, 255, 0), -1)

        cv2.rectangle(frame, (x2, y2), (x2+w2, y2 + h2), (0, 255, 255), 3)
        cv2.circle(frame, (x2+w2/2, y2+h2/2), 5, (0, 255, 255), -1)

        cv2.imshow('frame',frame)
        # cv2.imshow('mask',maskRed)
        # cv2.imshow('res',res)
    
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
            cv2.destroyAllWindows()
            cap.release()

    except:
        print("Imagem nao reconhecida!! Verifique se a webcam esta ligada e se o parametro cam esta setado corretamente!!")
        quit()