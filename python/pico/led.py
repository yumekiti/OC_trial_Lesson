from machine import Pin
import time

pin = Pin(25, Pin.OUT)

# Lチカ
while True:
    pin.toggle()
    time.sleep_ms(1000)
