
import serial 
import time 
import pynmea2


Thruster = serial.Serial("/dev/serial0",9600)   # Thruster connection 
#infi 
#except: 
 # print("Thruster computer lost connection please reconnect ! ")
    # byte array for the Thruster comman 

MV = [0x4d,0,0x56,0x20]

EIGN2 = [0x45,0x49,0x4e,0x28,0x32,0x29,0x20]


EIGN3  = [0x45 ,0x49 ,0x47 ,0x4e ,0x28 ,0x33 ,0x29 ,0x20]


ITR2 = [0x49 ,0x54 ,0x52 ,0x28 ,0x30 ,0x2c ,0x33 ,0x2c ,0x31 ,0x35 ,0x2c ,0x31 ,0x2c ,0x32 ,0x30 ,0x29 ,0x20]



C10= [43 ,0x31 ,0x30 ,0x20]



GOTO10 = [0x20 ,0x20 ,0x47 ,0x4f ,0x54 ,0x4f ,0x31 ,0x30 ,0x20]



C20 = [0x43 ,0x32 ,0x30 ,0x20]



X = [0x20 ,0x20 ,0x58 ,0x20]



Gloop = [0x20 ,0x20 ,0x47 ,0x20]



ECHO_OFF = [0x45 , 0x43 , 0x48 , 0x4f , 0x5f , 0x4f , 0x46 , 0x46 , 0x20]  #echo off



EIGNW = [0x45 , 0x49 , 0x47 , 0x4e , 0x28 , 0x57 , 0x2c , 0x30 , 0x29 , 0x20] #EIGN(W,0)



ZS =[0x5a , 0x53 , 0x20 ]  #ZS   



ITR04001  = [0x49 , 0x54 , 0x52 , 0x28 , 0x30 , 0x2c , 0x34 , 0x2c , 0x30 , 0x2c , 0x30 , 0x2c , 0x31 , 0x29 , 0x20 ] #ITR(0,4,0,0,1)



ITRE = [0x49 , 0x54 , 0x52 , 0x45 , 0x20] #ITRE 



EITR0  = [0x45 , 0x49 , 0x54 , 0x52 , 0x28 , 0x30 , 0x29 , 0x20 ] #EITR(0)



OUT11 = [0x4f , 0x55 , 0x54 , 0x28 , 0x31 , 0x29 , 0x3d , 0x31 , 0x20] #OUT(1)=1 



ADT = [0x41 , 0x44 , 0x54 , 0x3d , 0x31 , 0x30 , 0x30 , 0x20 ] #ADT=100 



VT = [0x56 , 0x54 , 0x3d , 0x31 , 0x30 , 0x30 , 0x30 , 0x30 , 0x30 , 0x20 ] #VT=100000


VT_more =[0x56 , 0x54 , 0x3d , 0x31 , 0x30 , 0x30 , 0x30 , 0x30 , 0x30 , 0x30 , 0x20 ] #VT=100000



MP = [0x4d , 0x50, 0x20 ]  #MP



WHILE = [0x57 , 0x48 , 0x49 , 0x4c , 0x45 , 0x20 , 0x31 , 0x3e , 0x30 , 0x20] #WHILE 1>0 



O0 = [0x20 , 0x20 , 0x4f , 0x3d , 0x30 , 0x20]  #O=0



PT = [0x20 , 0x20 , 0x50 , 0x54 , 0x3d , 0x34 , 0x30 , 0x30 , 0x30 , 0x30] #PT=40000



G = [0x20 , 0x20 , 0x47] #  G



WHILEPA = [0x20 , 0x20 , 0x57 , 0x48 , 0x49 , 0x4c , 0x45 , 0x20 , 0x50 , 0x41 , 0x3c , 0x32 , 0x30 , 0x30 , 0x30 , 0x30 ] #WHILE PA<20000



LOOP = [0x20 , 0x20 , 0x4c , 0x4f , 0x4f , 0x50 ] #LOOP



OUT10 = [0x20 , 0x20 , 0x4f , 0x55 , 0x54 , 0x28 , 0x31 , 0x29 , 0x3d , 0x30] # OUT(1)=0



TMR0400 = [0x20 , 0x20 , 0x54 , 0x4d , 0x52 , 0x28 , 0x30 , 0x2c , 0x34 , 0x30 , 0x30]  #TMR(0,400)



TWAIT=[0x20 , 0x20 , 0x54 , 0x57 , 0x41 , 0x49 , 0x54 ] #TWAIT



WAIT =[0x20 , 0x20 , 0x57 , 0x41 , 0x49 , 0x54 , 0x3d , 0x31 , 0x30 , 0x30 , 0x30 ] #WAIT=1000



L00P = [0x4c , 0x4f , 0x4f , 0x50 , 0x20] #LOOP 



END = [0x45 , 0x4e , 0x44 , 0x20 ] #END


C1 = [0x43 , 0x31 , 0x20 ]



OUT_11 = [0x20 , 0x20 , 0x4f , 0x55 , 0x54 , 0x28 , 0x31 , 0x29 , 0x3d , 0x31 ] #OUT(1)=1



RETURNI = [0x52 , 0x45 , 0x54 , 0x55 , 0x52 , 0x4e , 0x49 , 0x20] #RETURNI



RPA = [0x50 , 0x52 , 0x49 , 0x4e , 0x54 , 0x28 , 0x22 , 0x50 , 0x6f , 0x73 , 0x69 , 0x74 , 0x69 , 0x6f , 0x6e , 0x3a , 0x20 , 0x22 , 0x2c , 0x52 , 0x50 , 0x41 , 0x2c , 0x23 , 0x31 , 0x33 , 0x29] 


WAIT_more = [0x20 , 0x20 , 0x57 , 0x41 , 0x49 , 0x54 , 0x3d , 0x31 , 0x30 , 0x30 , 0x30 , 0x30] #wait 1000

i = 0 
def  infi(): 
	for i in range(0,len(ECHO_off)): 

        	Thruster.write(ECHO_OFF [i])  

	for i in range(0,len(EIGN2)):
	     	Thruster.write(EIGN2 [i])

	for i in range(0,len(EIGN3)): 

         	Thruster.write(EIGN3 [i])  

	for i in range(0,len(ZS)):

		Thruster.write(ZS [i])

	for i in range(0,len(VT)): 

		Thruster.write(VT [i]) 

	for i in range (0, len(ADT)): 

		Thruster.write(ADT [i])

	for i in range (0, len(MV)): 
		Thruster.write(MV [i])  

	for i in range(0, len(ITR2)): 
		Thruster.write(ITR2 [i])  

	for i in range (0, len(EITR0)):
		Thruster.write(EITR0 [i])  

	for i in range (0, len(ITRE)):
		Thruster.write(ITRE [i])


	for i in range(0, len(G)):
		Thruster.write(G [i])  

	for i in range(0,len(C10)):
		Thruster.write(C10 [i])


	for i in range(0,len(GOTO10)):
		Thruster.write(GOTO10 [i])


	for i in range (0, len(END)):
		Thruster.write(END [i]) 

	for i in range(0, len(C20)):
		Thruster.write(C20 [i])

	for i in range (0, len(X)):
		Thruster.write(X [i])  


	for i in range (0, len(TWAIT)):
		Thruster.write(TWAIT [i])  


	for i in range(0, len(Gloop)):
		Thruster.write(Gloop [i])  

	for i in range(0, len(RETURNI)):
		Thruster.write(RETURNI [i])

infi
