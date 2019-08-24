import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)

GPIO.output(17,GPIO.LOW)

  



       

def ai_anomaly_callback():

    GPIO.output(17,GPIO.HIGH)



if __name__ == "__main__":



    GPIO.output(17,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(17,GPIO.LOW)
  

  



    print("Communication between drone and pi started");

    

    import brainiumClient

    import threading

    

    brainiumClient.anomalyCallback = ai_anomaly_callback

    

    brainiumMqttThread = threading.Thread(target = brainiumClient.main)

    brainiumMqttThread.start()


