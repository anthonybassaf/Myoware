import serial
import random
import time

ser = serial.Serial('COM3', 9600, timeout = 1)
val = []

while 1:
    arduinoData = ser.readline().decode('ascii')
    arduinoData = arduinoData.replace("\r", "")
    arduinoData = arduinoData.replace("\n", "")
    if arduinoData != '' and int(float(arduinoData)) >= 140 and int(float(arduinoData)) <= 220:
        val.append(float(arduinoData))
        print(arduinoData)
    else:
        val.clear()


    


