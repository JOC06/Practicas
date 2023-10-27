import cv2

# Abre el archivo de video
cap = cv2.VideoCapture('tu_video.mp4')  # Reemplaza 'tu_video.mp4' con la ruta de tu archivo de video

# Lee el primer cuadro
ret, frame1 = cap.read()
prev_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    # Lee el siguiente cuadro
    ret, frame2 = cap.read()
    if not ret:
        break

    # Convierte el cuadro a escala de grises
    next_frame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calcula la diferencia absoluta entre los cuadros
    frame_diff = cv2.absdiff(prev_frame, next_frame)

    # Aplica un umbral a la diferencia
    _, threshold = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Encuentra y dibuja contornos alrededor de las áreas de movimiento
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 100:  # Ajusta este umbral según tus necesidades
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Muestra el cuadro con las detecciones
    cv2.imshow('Video con Detección de Movimiento', frame2)

    # Actualiza el cuadro anterior
    prev_frame = next_frame

    # Sale del bucle si se presiona la tecla 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Libera los recursos y cierra las ventanas
cap.release()
cv2.destroyAllWindows()
