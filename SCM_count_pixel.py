import cv2
import numpy as np
from glob import glob

img_mask = '/Users/joaonobre/Documents/INPE/Proposta/Python/CCM/Entradas_CCM/teste02.png'
img_names = glob(img_mask)

for fn in img_names:
	print('Processando %s...' % fn,)
	img = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
	n_white_pix = np.sum(img == 255)
	print('Numero de Pixels:', n_white_pix, 'Area (km**2):', n_white_pix*16)
