import cv2
import numpy as np

# Cargar una imagen
image = cv2.imread('tu_imagen.jpg')  # Reemplaza 'tu_imagen.jpg' con la ruta de tu imagen

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro Gaussiano para suavizar la imagen y reducir el ruido
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Aplicar el detector de bordes Canny
edges = cv2.Canny(blurred, 50, 150)  # Ajusta los umbrales según tus necesidades

# Realizar la segmentación (umbralización)
_, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# Muestra la imagen original, los bordes detectados y la imagen segmentada
cv2.imshow('Imagen Original', image)
cv2.imshow('Detección de Bordes (Canny)', edges)
cv2.imshow('Imagen Segmentada', thresholded)

cv2.waitKey(0)
cv2.destroyAllWindows()
