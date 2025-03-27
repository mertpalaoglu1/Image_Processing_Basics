import cv2

img = cv2.imread('image1.jpg')

while True: #her an göstermesi için while'da
    cv2.imshow('AykutPencereAdi',img) 
    #Eğer en az 1 ms beklediysek VE çıkış butonuna (ESC) bastıysak çık demek   
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
