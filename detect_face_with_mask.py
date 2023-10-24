# Importar la biblioteca OpenCV
import cv2
  
# Definir un objeto de captura de video
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capturar el video fotograma por fotograma
    ret, frame = vid.read()
  
    # Mostrar el fotograma resultante
    cv2.imshow('Fotograma', frame)
      
    # Salir de la ventana con la barra espaciadora
    key = cv2.waitKey(1)
    
    if key == 32:
        break
  
# Después del bucle, liberar al objeto de captura
vid.release()

# Destruir todas las ventanas
cv2.destroyAllWindows()
