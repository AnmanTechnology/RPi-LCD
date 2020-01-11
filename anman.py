import RPi.GPIO as GPIO
import time

print("Hello World")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(3, GPIO.OUT)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Setup")

count = 0
last_count = 0
def en_callback(channel):
    global count
    count += 1
    time.sleep(0.01)
    
GPIO.add_event_detect(13,GPIO.RISING)
GPIO.add_event_callback(13, en_callback)
try:
    while True:
        #prev_time = time.time()
        #curr_time = time.time()
        #delta_time = curr_time - prev_time
        #prev_time =curr_time
        #vel = (count - last_count) / delta_time
        #last_count = count

        print(count)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    




