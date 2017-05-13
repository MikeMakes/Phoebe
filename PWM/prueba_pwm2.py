import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO  
from time import sleep  # cargamos la función sleep del módulo time 

# Probar a poner de nuevo "GPIO.setwarnings(False)" si no funciona asi #

GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM  
  
GPIO.setup(24, GPIO.OUT)  # Ponemos el pin GPIO nº24 como salida para el LED  
  
red = GPIO.PWM(24, 100)     # Creamos el objeto 'red' en el pin 24 a 100 Hz 
  
red.start(100)              # Iniciamos el objeto 'red' al 100% del ciclo de trabajo (completamente encendido)  
  
# A partir de ahora empezamos a modificar los valores del ciclo de trabajo
  
pause_time = 0.02           # Declaramos un lapso de tiempo para las pausas
  
try:                        # Abrimos un bloque 'Try...except KeyboardInterrupt'
    while True:             # Iniciamos un bucle 'while true'  
        for i in range(0,101):            # De i=0 hasta i=101 (101 porque el script se detiene al 100%)
            red.ChangeDutyCycle(i)      # LED #1 = i
            sleep(pause_time)             # Pequeña pausa para no saturar el procesador
            
        print("Ciclo completo")    # Imprime por pantalla: Ciclo completo

except KeyboardInterrupt:   # Se ha pulsado CTRL+C!!
    white.stop()            # Detenemos el objeto 'white'
    red.stop()              # Detenemos el objeto 'red'
    GPIO.cleanup()          # Limpiamos los pines GPIO y salimos