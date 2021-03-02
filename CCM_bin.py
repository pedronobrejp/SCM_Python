import cv2
img = cv2.imread('/Users/joaonobre/Desktop/INPE/Proposta/Python/CCM/Entrada_CCM_24012017/Figura01.png',2)

ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("Binary Image",bw_img)
cv2.imwrite('/Users/joaonobre/Desktop/INPE/Proposta/Python/CCM/Entrada_CCM_24012017/Figura01.png',bw_img)