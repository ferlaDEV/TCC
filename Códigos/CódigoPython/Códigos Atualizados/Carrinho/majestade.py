#Importacao de bibliotecas
import RPi.GPIO as GPIO
import time

#Setando como vamos referir o numero do pino utilizado
#Board pelo numero da placa exemplo pin18
#BCM pelo numero Broadcom SOC channel, exemplo GPIO24
GPIO.setmode(GPIO.BCM)

#Setando os pinos que serao utilizados

#Pinos do Motor DC
habilitar_pin_motor = 23
pin_motor_1 = 23
pin_motor_2 = 24

#Pinos Sensor Ultrassonico
pin_trigger = 18
pin_echo = 25

#Setar a direcao da GPIO

#Motor
GPIO.setup(habilitar_pin_motor, GPIO.OUT)
GPIO.setup(pin_motor_1, GPIO.OUT)
GPIO.setup(pin_motor_2, GPIO.OUT)

#Sensor Ultrassonico
GPIO.setup(pin_trigger, GPIO.OUT)
GPIO.setup(pin_echo, GPIO.IN)

#Setando a velocidade do motor
motor_pwm = GPIO.PWM(habilitar_pin_motor, 500)
motor_pwm.start(0)

#Definindo movimento do moto

def frente(kmh):          
    GPIO.output(pin_motor_1, True) 
    GPIO.output(pin_motor_2, False) 
    motor_pwm.ChangeDutyCycle(float(kmh))

def re(kmh):          
    GPIO.output(pin_motor_1, False) 
    GPIO.output(pin_motor_2, True) 
    motor_pwm.ChangeDutyCycle(float(kmh))

def parar():
    GPIO.output(pin_motor_1, False) 
    GPIO.output(pin_motor_2, False)
    motor_pwm.ChangeDutyCycle(0)

#Definindo o valor da distancia do sensor
def distancia():
    # set Trigger to HIGH
    GPIO.output(pin_trigger, True)
 
    #Setar o Trigger depois de 0.01ms para baixo
    time.sleep(0.00001)
    GPIO.output(pin_trigger, False)
 
    tempo_inicial = time.time()
    tempo_parada = time.time()
 
    #Salvar tempo_inicial
    while GPIO.input(pin_echo) == 0:
        tempo_inicial = time.time()
 
    #Salvar tempo_parada
    while GPIO.input(pin_echo) == 1:
        tempo_parada = time.time()
 
    #Diferenca de tempo entre tempo_inicial e tempo_parada
    tempo_decorrido = tempo_parada - tempo_inicial
    #Multiplica a velocidade sonica por (34300 cm/s)
    #e divide por 2 por que ela vai e volta
    distancia = (tempo_decorrido * 34000) / 2
 
    return distancia

if __name__ == '__main__':
    try:
        while True:
            frente(float(50))
            dist = distancia()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(0.1)
            if float(dist) <= 14:
                re(float(100))
                time.sleep(0.00001)
                parar()
                print("Objeto identificado")
                break
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()