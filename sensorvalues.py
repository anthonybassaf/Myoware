import serial
import time
import csv

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='/r')
        print('Your turn')
        time.sleep(1)
        t -= 1
    print("Time's up")
countdown(5)

try:
    arduino = serial.Serial("COM4", 9600, timeout=1)
except:
    print("Please check the port")

# Initializing variables
data = []
max_read = []

while countdown != 0:
    data.append(str(arduino.readline()))
    max_read = max(data)

print(max_read)