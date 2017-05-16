import RPi.GPIO as GPIO # Cargamos la libreria RPi.GPIO  
from time import sleep  # cargamos la función sleep del módulo time 

# Probar a poner de nuevo "GPIO.setwarnings(False)" si no funciona asi #

GPIO.setmode(GPIO.BCM)  # Ponemos la Raspberry en modo BCM  
  
GPIO.setup(24, GPIO.OUT)  # Ponemos el pin GPIO nº24 como salida para el LED  
  
red = GPIO.PWM(24, 480)     # Creamos el objeto 'red' en el pin 24 a 100 Hz 
  
def led(a):
	red.start(a)

led(1)              

# A partir de ahora empezamos a modificar los valores del ciclo de trabajo
  
except KeyboardInterrupt:   # Se ha pulsado CTRL+C!!
    red.stop()              # Detenemos el objeto 'red'
    GPIO.cleanup()          # Limpiamos los pines GPIO y salimos