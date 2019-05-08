#!/usr/bin/python3
import smbus
import math
import time  
import pyfirmata 
import datetime 
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
AngleDegX  = 0 
AngleDegY = 0 
AngleDegZ = 0 
time = datetime.datetime.now()
try:
  hardware = pyfirmata.ArduinoMega("/dev/ttyUSB0")
except: 
   print("connecting the backup protocol")
   try:
      hardware = pyfirmata.ArduinoMega("/dev/ttyUSB1")
   except:
      print("All hardware not connected")
XLservo = hardware.get_pin('d:8:s')
XRservo = hardware.get_pin('d:9:s') 
YUservo = hardware.get_pin('d:10:s')
YBservo = hardware.get_pin('d:11:s')

def read_byte(reg):
    return bus.read_byte_data(address, reg)

def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
 
bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect
 
# Aktivieren, um das Modul ansprechen zu koennen
bus.write_byte_data(address, power_mgmt_1, 0)
 
print("Gyroscope")
print("--------")
gyroskop_xout = read_word_2c(0x43)
gyroskop_yout = read_word_2c(0x45)
gyroskop_zout = read_word_2c(0x47)
def Servoanglecontrol(AngleY,Anglez): 
     XLservo.write(AngleY)
     XRservo.write(180-AngleY)  
     YUservo.write(Anglez)
     YBservo.write(180-Anglez)      
Blackdata = open("UUVreportData.txt","w+")
while True:
#   print("gyroskop_xout: ", ("%5d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 131))
 #  print("gyroskop_yout: ", ("%5d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 131))
  # print("gyroskop_zout: ", ("%5d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 131))
 
   print("UUV Gyroscope")
   print("---------------------")
 
   beschleunigung_xout = read_word_2c(0x3b)
   beschleunigung_yout = read_word_2c(0x3d)
   beschleunigung_zout = read_word_2c(0x3f)
 
   beschleunigung_xout_skaliert = beschleunigung_xout / 16384.0
   beschleunigung_yout_skaliert = beschleunigung_yout / 16384.0
   beschleunigung_zout_skaliert = beschleunigung_zout / 16384.0
   AngleDegX = math.degrees(beschleunigung_xout_skaliert)
   AngleDegY = math.degrees(beschleunigung_yout_skaliert)
   AngleDegZ = math.degrees(beschleunigung_zout_skaliert)
   print("AngleDegX",(AngleDegX))
   print("AngleDegY",(AngleDegY))
   print("AngleDegZ",(AngleDegZ))
   #GyroSense = str(AngleDegX) + "," + str(AngleDegY) + "," + str(AngleDegZ)
   Blackdata.write("\n"+str(time)+"Gyroscope data(x,y,z)"+"," +str(AngleDegX) +","+str(AngleDegY)+","+str(AngleDegZ))
   Servoanglecontrol(abs(AngleDegY),abs(AngleDegZ))
          
