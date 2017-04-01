#!/usr/bin/env python
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.UART as UART
import serial
import smbus
import time
import math
import decimal
from threading import Thread
import os
import sys
import Adafruit_BBIO.ADC as ADC
#import threading 
#import datetime
import multitasking
import random
import signal

ADC.setup()

def aadc():
	print "depan",ADC.read("P9_40")#depan
	print "deki",ADC.read("P9_38")#kide
	print "belka",ADC.read("P9_36")#belakangkiri

bus = smbus.SMBus(2)
address = 0x1e##kaki
#SERIALPORT = "/dev/ttyUSB1"
SERIALPORT = "/dev/ttyUSB0"
BAUDRATE = 1000000

INST_WRITE = 3
AX_WRITE = 131

ax = serial.Serial(SERIALPORT,BAUDRATE)
rf = serial.Serial(port ="/dev/ttyUSB0",baudrate=1000000)

parameter = range(400)
transfer = range(400)
parameter1 = range(6)
transfer1 = range(12)

clpwm = 0
crpwm = 0
signal.signal(signal.SIGINT, multitasking.killall)
@multitasking.task
def packet_kirim(perintah,parameterlength,n):
	transfer[0]=0xFF
	transfer[1]=0xFF
	transfer[2]=0XFE
	transfer[3]=((parameterlength+1)*n+4)
	transfer[4]=perintah
	transfer[5]=30
	transfer[6]=parameterlength
	for i in range(1,91):
		transfer[i+6] = parameter[i]
	check=0
	for o in range(2,97):
		check += (transfer[o])
	
	transfer[97]= 255 -((check) % 256)

	for p in range(0,98):
		ax.write(chr(transfer[p]))


l1=5.2
l2=6

def invers_kinematik1 (x,y,z):

    	global tetha11
    	global tetha21
    	global tetha31
    	F=((x*x)+(y*y)+(z*z)-(l1**2)-(l2**2))
    	E= (2*l1*l2)
    	A=F/E
    	B=math.sqrt(math.fabs(1-(A*A)))
    	tetha31=math.atan2(-B,A)
    	buff_1=(l2*math.cos(tetha31))+l1
    	buff_2=math.sqrt((x*x)+(y*y))
    	buff_3=l2*math.sin(tetha31)
    	C=(z*buff_1)-(buff_2*buff_3)
    	D=(buff_1*buff_2)+(z*buff_3)
    	tetha21=math.atan2(math.fabs(C),D)
    	tetha11=math.atan2(x,y)    

def invers_kinematik2 (x,y,z):

    	global tetha12
    	global tetha22
    	global tetha32
    	F=((x*x)+(y*y)+(z*z)-(l1**2)-(l2**2))
    	E= (2*l1*l2)
    	A=F/E
    	B=math.sqrt(math.fabs(1-(A*A)))
    	tetha32=math.atan2(-B,A)
    	buff_1=(l2*math.cos(tetha32))+l1
    	buff_2=math.sqrt((x*x)+(y*y))
    	buff_3=l2*math.sin(tetha32)
    	C=(z*buff_1)-(buff_2*buff_3)
    	D=(buff_1*buff_2)+(z*buff_3)
    	tetha22=math.atan2(math.fabs(C),D)
    	tetha12=math.atan2(x,y)    

def invers_kinematik3 (x,y,z):

    	global tetha13
    	global tetha23
    	global tetha33
    	F=((x*x)+(y*y)+(z*z)-(l1**2)-(l2**2))
    	E= (2*l1*l2)
    	A=F/E
    	B=math.sqrt(math.fabs(1-(A*A)))
    	tetha33=math.atan2(-B,A)
    	buff_1=(l2*math.cos(tetha33))+l1
    	buff_2=math.sqrt((x*x)+(y*y))
    	buff_3=l2*math.sin(tetha33)
    	C=(z*buff_1)-(buff_2*buff_3)
    	D=(buff_1*buff_2)+(z*buff_3)
    	tetha23=math.atan2(math.fabs(C),D)
    	tetha13=math.atan2(x,y)    

def invers_kinematik4 (x,y,z):

    	global tetha14
    	global tetha24
    	global tetha34
    	F=((x*x)+(y*y)+(z*z)-(l1**2)-(l2**2))
    	E= (2*l1*l2)
    	A=F/E
    	B=math.sqrt(math.fabs(1-(A*A)))
    	tetha34=math.atan2(-B,A)
    	buff_1=(l2*math.cos(tetha34))+l1
    	buff_2=math.sqrt((x*x)+(y*y))
    	buff_3=l2*math.sin(tetha34)
    	C=(z*buff_1)-(buff_2*buff_3)
    	D=(buff_1*buff_2)+(z*buff_3)
    	tetha24=math.atan2(math.fabs(C),D)
    	tetha14=math.atan2(x,y)   

def invers_kinematik5 (x,y,z):

    	global tetha15
    	global tetha25
    	global tetha35
    	F=((x*x)+(y*y)+(z*z)-(l1**2)-(l2**2))
    	E= (2*l1*l2)
    	A=F/E
    	B=math.sqrt(math.fabs(1-(A*A)))
    	tetha35=math.atan2(-B,A)
    	buff_1=(l2*math.cos(tetha35))+l1
    	buff_2=math.sqrt((x*x)+(y*y))
    	buff_3=l2*math.sin(tetha35)
    	C=(z*buff_1)-(buff_2*buff_3)
    	D=(buff_1*buff_2)+(z*buff_3)
    	tetha25=math.atan2(math.fabs(C),D)
    	tetha15=math.atan2(x,y)
    
def invers_kinematik6 (x,y,z):

    	global tetha16
    	global tetha26
    	global tetha36
   	F=((x*x)+(y*y)+(z*z)-(l1**2)-(l2**2))
    	E= (2*l1*l2)
    	A=F/E
    	B=math.sqrt(math.fabs(1-(A*A)))
    	tetha36=math.atan2(-B,A)
    	buff_1=(l2*math.cos(tetha36))+l1
    	buff_2=math.sqrt((x*x)+(y*y))
    	buff_3=l2*math.sin(tetha36)
    	C=(z*buff_1)-(buff_2*buff_3)
    	D=(buff_1*buff_2)+(z*buff_3)
    	tetha26=math.atan2(math.fabs(C),D)
	tetha16=math.atan2(x,y)

def rad_to_deg1():
	global degree_11
	global degree_21
	global degree_31
	satu1 =  tetha11*57.2957795
	dua1 =  tetha21*57.2957795
	tiga1 =  tetha31*57.2957795
	degree_11 = int(satu1)
	degree_21 = int(dua1)
	degree_31 = int(tiga1)
    
def rad_to_deg2():
	global degree_12
	global degree_22
	global degree_32
	satu2 =  tetha12*57.2957795
	dua2 =  tetha22*57.2957795
	tiga2 =  tetha32*57.2957795
	degree_12 = int(satu2)
	degree_22 = int(dua2)
	degree_32 = int(tiga2)

def rad_to_deg3():
	global degree_13
	global degree_23
	global degree_33
	satu3 =  tetha13*57.2957795
	dua3 =  tetha23*57.2957795
	tiga3 =  tetha33*57.2957795
	degree_13 = int(satu3)
	degree_23 = int(dua3)
	degree_33 = int(tiga3)

def rad_to_deg4():
	global degree_14
	global degree_24
	global degree_34
	satu4 =  tetha14*57.2957795
	dua4 =  tetha24*57.2957795
	tiga4 =  tetha34*57.2957795
	degree_14 = int(satu4)
	degree_24 = int(dua4)
	degree_34 = int(tiga4)

def rad_to_deg5():
	global degree_15
	global degree_25
	global degree_35
	satu5 =  tetha15*57.2957795
	dua5 =  tetha25*57.2957795
	tiga5 =  tetha35*57.2957795
	degree_15 = int(satu5)
	degree_25 = int(dua5)
	degree_35 = int(tiga5)

def rad_to_deg6():
	global degree_16
	global degree_26
	global degree_36
	satu6 =  tetha16*57.2957795
	dua6 =  tetha26*57.2957795
	tiga6 =  tetha36*57.2957795
	degree_16 = int(satu6)
	degree_26 = int(dua6)
	degree_36 = int(tiga6)

def kanan1(): 
	global outdeg11
	global outdeg21
	global outdeg31
	sp_deg1=175
	sp_deg2=197
	sp_deg3=284
	outdeg11=(degree_11+sp_deg1)
	outdeg21=(degree_21-sp_deg2)*(-1)
	outdeg31=(degree_31+sp_deg3)

def kanan2(): 
	global outdeg12
	global outdeg22
	global outdeg32
	sp_deg1=150
	sp_deg2=197
	sp_deg3=284
	outdeg12=(degree_12+sp_deg1)
	outdeg22=(degree_22-sp_deg2)*(-1)
	outdeg32=(degree_32+sp_deg3)
	
def kanan3(): 
	global outdeg13
	global outdeg23
	global outdeg33
	sp_deg1=125
	sp_deg2=197
	sp_deg3=284
	outdeg13=(degree_13+sp_deg1)
	outdeg23=(degree_23-sp_deg2)*(-1)
	outdeg33=(degree_33+sp_deg3)
	
def kiri1():
	global outdeg14
	global outdeg24
	global outdeg34	
	sp_deg4=125
	sp_deg5=103
	sp_deg6=16
	outdeg14=(degree_14-sp_deg4)*(-1)
	outdeg24=(degree_24+sp_deg5)
	outdeg34=(degree_34-sp_deg6)*(-1)
	
def kiri2():
	global outdeg15
	global outdeg25
	global outdeg35	
	sp_deg4=150
	sp_deg5=103
	sp_deg6=16
	outdeg15=(degree_15-sp_deg4)*(-1)
	outdeg25=(degree_25+sp_deg5)
	outdeg35=(degree_35-sp_deg6)*(-1)

def kiri3():
	global outdeg16
	global outdeg26
	global outdeg36	
	sp_deg4=175
	sp_deg5=103
	sp_deg6=16
	outdeg16=(degree_16-sp_deg4)*(-1)
	outdeg26=(degree_26+sp_deg5)
	outdeg36=(degree_36-sp_deg6)*(-1)

var_z1=0
var_y1=0
var_x1=0
var_z2=0
var_y2=0
var_x2=0
var_z3=0
var_y3=0
var_x3=0
var_z4=0
var_y4=0
var_x4=0
var_z5=0

var_y5=0
var_x5=0
var_z6=0
var_y6=0
var_x6=0

def sinus_pattern1(A,B,C,D,alpa,phasa,direksi):
 	global var_x1
	global var_y1
	global var_z1
	global sudut
	if direksi == 0:
		var_y1 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x1 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if(sudut>=0) and (sudut<90):
                      	  		var_z1=-D  
                    		elif (sudut>=90) and (sudut<270):
                       			var_z1=((C*math.sin((sudut-90)*0.0174532925))-D)
              			elif (sudut>=270) and (sudut<360):
                       			var_z1=-D

                elif phasa == 1:
                    		var_x1 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                 		if (sudut>=0) and (sudut<90):
                      			var_z1=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z1=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z1=(((-C)*math.sin((sudut-90)*0.0174532925))-D)  
	elif direksi == 1:
		var_y1 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B
        	if phasa == 0: 
                    		var_x1 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if (sudut>=0) and (sudut<90):
                       			var_z1=-D 
                    		elif (sudut>=90) and (sudut<270):
                       			var_z1=((C*math.sin((sudut-90)*0.0174532925))-D)
				elif (sudut>=270) and (sudut<360):
                        		var_z1=-D
        
            	elif phasa == 1 :
                    		var_x1 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		if (sudut>=0) and (sudut<90):
                        		var_z1=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z1=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z1=(((-C)*math.sin((sudut-90)*0.0174532925))-D) 

def sinus_pattern2(A,B,C,D,alpa,phasa,direksi):
 	global var_x2
	global var_y2
	global var_z2
	global sudut
	if direksi == 0:
		var_y2 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x2 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if(sudut>=0) and (sudut<90):
                      	  		var_z2=-D  
                    		elif (sudut>=90) and (sudut<270):
                       			var_z2=((C*math.sin((sudut-90)*0.0174532925))-D)
              			elif (sudut>=270) and (sudut<360):
                       			var_z2=-D

                elif phasa == 1:
                    		var_x2 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                 		if (sudut>=0) and (sudut<90):
                      			var_z2=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z2=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z2=(((-C)*math.sin((sudut-90)*0.0174532925))-D)  
	
	elif direksi == 1:
		var_y2 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x2 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if (sudut>=0) and (sudut<90):
                       			var_z2=-D 
                    		elif (sudut>=90) and (sudut<270):
                       			var_z2=((C*math.sin((sudut-90)*0.0174532925))-D)
				elif (sudut>=270) and (sudut<360):
                        		var_z2=-D
        
            	elif phasa == 1 :
                    		var_x2 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		if (sudut>=0) and (sudut<90):
                        		var_z2=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z2=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z2=(((-C)*math.sin((sudut-90)*0.0174532925))-D) 
                        		
def sinus_pattern3(A,B,C,D,alpa,phasa,direksi):
 	global var_x3
	global var_y3
	global var_z3
	global sudut
	if direksi == 0:
		var_y3 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x3 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if(sudut>=0) and (sudut<90):
                      	  		var_z3=-D  
                    		elif (sudut>=90) and (sudut<270):
                       			var_z3=((C*math.sin((sudut-90)*0.0174532925))-D)
              			elif (sudut>=270) and (sudut<360):
                       			var_z3=-D

                elif phasa == 1:
                    		var_x3 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                 		if (sudut>=0) and (sudut<90):
                      			var_z3=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z3=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z3=(((-C)*math.sin((sudut-90)*0.0174532925))-D)  
	
	elif direksi == 1:
		var_y3 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x3 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if (sudut>=0) and (sudut<90):
                       			var_z3=-D 
                    		elif (sudut>=90) and (sudut<270):
                       			var_z3=((C*math.sin((sudut-90)*0.0174532925))-D)
				elif (sudut>=270) and (sudut<360):
                        		var_z3=-D
        
            	elif phasa == 1 :
                    		var_x3 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		if (sudut>=0) and (sudut<90):
                        		var_z3=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z3=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z3=(((-C)*math.sin((sudut-90)*0.0174532925))-D) 
                        		
def sinus_pattern4(A,B,C,D,alpa,phasa,direksi):
 	global var_x4
	global var_y4
	global var_z4
	global sudut
	if direksi == 0:
		var_y4 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x4 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if(sudut>=0) and (sudut<90):
                      	  		var_z4=-D  
                    		elif (sudut>=90) and (sudut<270):
                       			var_z4=((C*math.sin((sudut-90)*0.0174532925))-D)
              			elif (sudut>=270) and (sudut<360):
                       			var_z4=-D

                elif phasa == 1:
                    		var_x4 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                 		if (sudut>=0) and (sudut<90):
                      			var_z4=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z4=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z4=(((-C)*math.sin((sudut-90)*0.0174532925))-D)  
	
	elif direksi == 1:
		var_y4 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x4 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if (sudut>=0) and (sudut<90):
                       			var_z4=-D 
                    		elif (sudut>=90) and (sudut<270):
                       			var_z4=((C*math.sin((sudut-90)*0.0174532925))-D)
				elif (sudut>=270) and (sudut<360):
                        		var_z4=-D
        
            	elif phasa == 1 :
                    		var_x4 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		if (sudut>=0) and (sudut<90):
                        		var_z4=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z4=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z4=(((-C)*math.sin((sudut-90)*0.0174532925))-D) 

def sinus_pattern5(A,B,C,D,alpa,phasa,direksi):
 	global var_x5
	global var_y5
	global var_z5
	global sudut
	if direksi == 0:
		var_y5 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x5 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if(sudut>=0) and (sudut<90):
                      	  		var_z5=-D  
                    		elif (sudut>=90) and (sudut<270):
                       			var_z5=((C*math.sin((sudut-90)*0.0174532925))-D)
              			elif (sudut>=270) and (sudut<360):
                       			var_z5=-D

                elif phasa == 1:
                    		var_x5 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                 		if (sudut>=0) and (sudut<90):
                      			var_z5=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z5=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z5=(((-C)*math.sin((sudut-90)*0.0174532925))-D)  
	
	elif direksi == 1:
		var_y5 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x5 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if (sudut>=0) and (sudut<90):
                       			var_z5=-D 
                    		elif (sudut>=90) and (sudut<270):
                       			var_z5=((C*math.sin((sudut-90)*0.0174532925))-D)
				elif (sudut>=270) and (sudut<360):
                        		var_z5=-D
        
            	elif phasa == 1 :
                    		var_x5 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		if (sudut>=0) and (sudut<90):
                        		var_z5=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z5=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z5=(((-C)*math.sin((sudut-90)*0.0174532925))-D) 
                   
def sinus_pattern6(A,B,C,D,alpa,phasa,direksi):
 	global var_x6
	global var_y6
	global var_z6
	global sudut
	if direksi == 0:
		var_y6 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x6 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if(sudut>=0) and (sudut<90):
                      	  		var_z6=-D  
                    		elif (sudut>=90) and (sudut<270):
                       			var_z6=((C*math.sin((sudut-90)*0.0174532925))-D)
              			elif (sudut>=270) and (sudut<360):
                       			var_z6=-D

                elif phasa == 1:
                    		var_x6 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                 		if (sudut>=0) and (sudut<90):
                      			var_z6=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z6=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z6=(((-C)*math.sin((sudut-90)*0.0174532925))-D)  
	
	elif direksi == 1:
		var_y6 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x6 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		if (sudut>=0) and (sudut<90):
                       			var_z6=-D 
                    		elif (sudut>=90) and (sudut<270):
                       			var_z6=((C*math.sin((sudut-90)*0.0174532925))-D)
				elif (sudut>=270) and (sudut<360):
                        		var_z6=-D
        
            	elif phasa == 1 :
                    		var_x6 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		if (sudut>=0) and (sudut<90):
                        		var_z6=((-C*math.sin((sudut-90)*0.0174532925))-D)  
                    		elif (sudut>=90) and (sudut<270):
                        		var_z6=-D
                    		elif (sudut>=270) and (sudut<360):
                        		var_z6=(((-C)*math.sin((sudut-90)*0.0174532925))-D) 


##################################################### Sinus Iseng #######################################################
def iseng_sinus_pattern1(A,B,C,D,alpa,phasa,direksi):
 	global var_x1
	global var_y1
	global var_z1
	global sudut
	if direksi == 0:
		var_y1 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x1 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z1=-D

                elif phasa == 1:
                    		var_x1 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
				var_z1=-D
 
	elif direksi == 1:
		var_y1 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x1 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z1=-D
        
            	elif phasa == 1 :
                    		var_x1 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		var_z1=-D

def iseng_sinus_pattern2(A,B,C,D,alpa,phasa,direksi):
 	global var_x2
	global var_y2
	global var_z2
	global sudut
	if direksi == 0:
		var_y2 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x2 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z2=-D

                elif phasa == 1:
                    		var_x2 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
				var_z2=-D
	
	elif direksi == 1:
		var_y2 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x2 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z2=-D
        
            	elif phasa == 1 :
                    		var_x2 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		var_z2=-D
                        		
def iseng_sinus_pattern3(A,B,C,D,alpa,phasa,direksi):
 	global var_x3
	global var_y3
	global var_z3
	global sudut
	if direksi == 0:
		var_y3 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x3 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z3=-D  
                    		
                elif phasa == 1:
                    		var_x3 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
				var_z3=-D
	
	elif direksi == 1:
		var_y3 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x3 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z3=-D
        
            	elif phasa == 1 :
                    		var_x3 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		var_z3=-D
                        		
def iseng_sinus_pattern4(A,B,C,D,alpa,phasa,direksi):
 	global var_x4
	global var_y4
	global var_z4
	global sudut
	if direksi == 0:
		var_y4 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x4 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z4=-D

                elif phasa == 1:
                    		var_x4 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
				var_z4=-D
	
	elif direksi == 1:
		var_y4 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x4 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z4=-D
        
            	elif phasa == 1 :
                    		var_x4 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		var_z4=-D

def iseng_sinus_pattern5(A,B,C,D,alpa,phasa,direksi):
 	global var_x5
	global var_y5
	global var_z5
	global sudut
	if direksi == 0:
		var_y5 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x5 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z5=-D

                elif phasa == 1:
                    		var_x5 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
				var_z5=-D 
	
	elif direksi == 1:
		var_y5 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x5 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z5=-D
        
            	elif phasa == 1 :
                    		var_x5 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		var_z5=-D
                   
def iseng_sinus_pattern6(A,B,C,D,alpa,phasa,direksi):
 	global var_x6
	global var_y6
	global var_z6
	global sudut
	if direksi == 0:
		var_y6 = ((-0.5)*(A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B   
            	if phasa == 0:  
                    		var_x6 = (-0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z6=-D

                elif phasa == 1:
                    		var_x6 = (0.5)*(A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
				var_z6=-D 
	
	elif direksi == 1:
		var_y6 = ((-0.5)*(-A)*math.sin((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)) + B    
        	if phasa == 0: 
                    		var_x6 = (-0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925)
                    		var_z6=-D
        
            	elif phasa == 1 :
                    		var_x6 = (0.5)*(-A)*math.cos((90-alpa)*0.0174532925)*math.sin(sudut*0.0174532925);
                    		var_z6=-D

def translate1 (z1):
	global H1
	global L1
	global deci1
	global desi1
	desi1 = (z1/300.0)*1023
	deci1 = int(desi1)
	H1 = (deci1/256)
	L1 = (deci1-(H1*256))

def translate2 (z2):
	global H2
	global L2
	global deci2
	global desi2
	desi2 = (z2/300.0)*1023
	deci2 = int(desi2)
	H2 = (deci2/256)
	L2 = (deci2-(H2*256))

def translate3 (z3):
	global H3
	global L3
	global deci3
	global desi3
	desi3 = (z3/300.0)*1023
	deci3 = int(desi3)
	H3 = (deci3/256)
	L3 = (deci3-(H3*256))
	
def translate4 (z4):
	global H4
	global L4
	global deci4
	global desi4
	desi4 = (z4/300.0)*1023
	deci4 = int(desi4)
	H4 = (deci4/256)
	L4 = (deci4-(H4*256))

def translate5 (z5):
	global H5
	global L5
	global deci5
	global desi5
	desi5 = (z5/300.0)*1023
	deci5 = int(desi5)
	H5 = (deci5/256)
	L5 = (deci5-(H5*256))

def translate6 (z6):
	global H6
	global L6
	global deci6
	global desi6
	desi6 = (z6/300.0)*1023
	deci6 = int(desi6)
	H6 = (deci6/256)
	L6 = (deci6-(H6*256))
	
def translate7 (z7):
	global H7
	global L7
	global deci7
	global desi7
	desi7 = (z7/300.0)*1023
	deci7 = int(desi7)
	H7 = (deci7/256)
	L7 = (deci7-(H7*256))

def translate8 (z8):
	global H8
	global L8
	global deci8
	global desi8
	desi8 = (z8/300.0)*1023
	deci8 = int(desi8)
	H8 = (deci8/256)
	L8 = (deci8-(H8*256))

def translate9 (z9):
	global H9
	global L9
	global deci9
	global desi9
	desi9 = (z9/300.0)*1023
	deci9 = int(desi9)
	H9 = (deci9/256)
	L9 = (deci9-(H9*256))
	
def translatea (za):
	global Ha
	global La
	global decia
	global desia
	desia = (za/300.0)*1023
	decia = int(desia)
	Ha = (decia/256)
	La = (decia-(Ha*256))

def translateb (zb):
	global Hb
	global Lb
	global decib
	global desib
	desib = (zb/300.0)*1023
	decib = int(desib)
	Hb = (decib/256)
	Lb = (decib-(Hb*256))

def translatec (zc):
	global Hc
	global Lc
	global decic
	global desic
	desic = (zc/300.0)*1023
	decic = int(desic)
	Hc = (decic/256)
	Lc = (decic-(Hc*256))
	
def translated (zd):
	global Hd
	global Ld
	global decid
	global desid
	desid = (zd/300.0)*1023
	decid = int(desid)
	Hd = (decid/256)
	Ld = (decid-(Hd*256))

def translatee (ze):
	global He
	global Le
	global decie
	global desie
	desie = (ze/300.0)*1023
	decie = int(desie)
	He = (decie/256)
	Le = (decie-(He*256))

def translatef (zf):
	global Hf
	global Lf
	global decif
	global desif
	desif = (zf/300.0)*1023
	decif = int(desif)
	Hf = (decif/256)
	Lf = (decif-(Hf*256))
	
def translateg (zg):
	global Hg
	global Lg
	global decig
	global desig
	desig = (zg/300.0)*1023
	decig = int(desig)
	Hg = (decig/256)
	Lg = (decig-(Hg*256))

def translateh (zh):
	global Hh
	global Lh
	global decih
	global desih
	desih = (zh/300.0)*1023
	decih = int(desih)
	Hh = (decih/256)
	Lh = (decih-(Hh*256))

def translatei (zi):
	global Hi
	global Li
	global decii
	global desii
	desii = (zi/300.0)*1023
	decii = int(desii)
	Hi = (decii/256)
	Li = (decii-(Hi*256))

############################ GERAKAN PID ###################################33
def kanan_1(A,alpa,direksi):

	sinus_pattern1(A, 5, 2.5, 3,alpa, 0, direksi)
	invers_kinematik1(var_x1,var_y1,var_z1)
	rad_to_deg1()
	kanan1()
	translate1(outdeg11)
	translate2(outdeg21-3)#+4
	translate3(outdeg31)#+3

	parameter[1] = 1
	parameter[2] = L1
	parameter[3] = H1
	parameter[4] = 0x88
	parameter[5] = 0x01

	parameter[6] = 2 
	parameter[7] = L2 
	parameter[8] = H2 
	parameter[9] = 0x88 
	parameter[10] = 0x01 

	parameter[11] = 3 
	parameter[12] = L3 
	parameter[13] = H3 
	parameter[14] = 0x88
	parameter[15] = 0x01 

def kanan_2(A,alpa,direksi):
	
	sinus_pattern2(A, 5, 2.5, 3,alpa, 1, direksi)
	invers_kinematik2(var_x2,var_y2,var_z2) 
	rad_to_deg2()
	kanan2()
	translate4(outdeg12)
	translate5(outdeg22+6)#+5
	translate6(outdeg32)#-1
	
	parameter[16] = 4
	parameter[17] = L4 
	parameter[18] = H4 
	parameter[19] = 0x88 
	parameter[20] = 0x01 

	parameter[21] = 5 
	parameter[22] = L5 
	parameter[23] = H5 
	parameter[24] = 0x88 
	parameter[25] = 0x01 

	parameter[26] = 6 
	parameter[27] = L6 
	parameter[28] = H6 
	parameter[29] = 0x88
	parameter[30] = 0x01 

def kanan_3(A,alpa,direksi):

	sinus_pattern3(A, 5, 3, 3,alpa, 0, direksi)#D2.5#c3
	invers_kinematik3(var_x3,var_y3,var_z3) 
	rad_to_deg3()
	kanan3()
	translate7(outdeg13)
	translate8(outdeg23+2)#+1
	translate9(outdeg33)
	
	parameter[31] = 7 
	parameter[32] = L7 
	parameter[33] = H7 
	parameter[34] = 0x88 
	parameter[35] = 0x01 

	parameter[36] = 8 
	parameter[37] = L8 
	parameter[38] = H8 
	parameter[39] = 0x88 
	parameter[40] = 0x01 

	parameter[41] = 9 
	parameter[42] = L9 
	parameter[43] = H9 
	parameter[44] = 0x88 
	parameter[45] = 0x01 

def kiri_1(A,alpa,direksi):

	sinus_pattern4(A, 5, 2.5, 3,alpa, 1, direksi)#D3.5
	invers_kinematik4(var_x4,var_y4,var_z4)
	rad_to_deg4()
	kiri1()	
	translatea(outdeg14)#+2 
	translateb(outdeg24)#-2
	translatec(outdeg34)#-2
	
	parameter[46] = 10 
	parameter[47] = La 
	parameter[48] = Ha 
	parameter[49] = 0x88
	parameter[50] = 0x01 

	parameter[51] = 11 
	parameter[52] = Lb 
	parameter[53] = Hb
	parameter[54] = 0x88 
	parameter[55] = 0x01 

	parameter[56] = 12 
	parameter[57] = Lc 
	parameter[58] = Hc 
	parameter[59] = 0x88 
	parameter[60] = 0x01 
	
def kiri_2(A,alpa,direksi):

	sinus_pattern5(A, 5, 2.5, 3,alpa, 0, direksi)
	invers_kinematik5(var_x5,var_y5,var_z5)
	rad_to_deg5()
	kiri2()
	translated(outdeg15)
	translatee(outdeg25-6)#-5#-1
	translatef(outdeg35)#-1
	
	parameter[61] = 13 
	parameter[62] = Ld 
	parameter[63] = Hd 
	parameter[64] = 0x88 
	parameter[65] = 0x01 

	parameter[66] = 14 
	parameter[67] = Le 
	parameter[68] = He 
	parameter[69] = 0x88 
	parameter[70] = 0x01

	parameter[71] = 15 
	parameter[72] = Lf 
	parameter[73] = Hf 
	parameter[74] = 0x88
	parameter[75] = 0x01 

def kiri_3(A,alpa,direksi):

	sinus_pattern6(A, 5, 3, 3,alpa, 1, direksi) #c3
	invers_kinematik6(var_x6,var_y6,var_z6) 
	rad_to_deg6()
	kiri3()
	translateg(outdeg16)
	translateh(outdeg26-2)#-2
	translatei(outdeg36-1) 
	
	parameter[76] = 16 
	parameter[77] = Lg 
	parameter[78] = Hg 
	parameter[79] = 0x88
	parameter[80] = 0x01

	parameter[81] = 17 
	parameter[82] = Lh 
	parameter[83] = Hh 
	parameter[84] = 0x88 
	parameter[85] = 0x01 

	parameter[86] = 18 
	parameter[87] = Li 
	parameter[88] = Hi 
	parameter[89] = 0x88 
	parameter[90] = 0x01

#################  INVERS KINEMATIK ###########################
def Kanan_depan(x,y,z):

	invers_kinematik1(x,y,-z)
	rad_to_deg1()
	kanan1()
	translate1(outdeg11)
	translate2(outdeg21)
	translate3(outdeg31)

	parameter[1] = 1 
	parameter[2] = L1 
	parameter[3] = H1 
	parameter[4] = 0x00 
	parameter[5] = 0x02 

	parameter[6] = 2 
	parameter[7] = L2 
	parameter[8] = H2 
	parameter[9] = 0x00 
	parameter[10] = 0x02 

	parameter[11] = 3 
	parameter[12] = L3 
	parameter[13] = H3 
	parameter[14] = 0x00
	parameter[15] = 0x02 

def Kanan_tengah(x,y,z):

	invers_kinematik2(x,y,-z)
	rad_to_deg2()
	kanan2()
	translate4(outdeg12)
	translate5(outdeg22)
	translate6(outdeg32)
	
	parameter[16] = 4 
	parameter[17] = L4 
	parameter[18] = H4 
	parameter[19] = 0x00 
	parameter[20] = 0x02 

	parameter[21] = 5 
	parameter[22] = L5 
	parameter[23] = H5 
	parameter[24] = 0x00 
	parameter[25] = 0x02 

	parameter[26] = 6 
	parameter[27] = L6 
	parameter[28] = H6 
	parameter[29] = 0x00
	parameter[30] = 0x02 

def Kanan_belakang(x,y,z):

	invers_kinematik3(x,y,-z)
	rad_to_deg3()
	kanan3()
	translate7(outdeg13)
	translate8(outdeg23)
	translate9(outdeg33)

	parameter[31] = 7 
	parameter[32] = L7 
	parameter[33] = H7 
	parameter[34] = 0x00 
	parameter[35] = 0x02 

	parameter[36] = 8 
	parameter[37] = L8 
	parameter[38] = H8 
	parameter[39] = 0x00 
	parameter[40] = 0x02 

	parameter[41] = 9 
	parameter[42] = L9 
	parameter[43] = H9 
	parameter[44] = 0x00 
	parameter[45] = 0x02 

def Kiri_depan(x,y,z):

	invers_kinematik4(x,y,-z)
	rad_to_deg4()
	kiri1()
	translatea(outdeg14)
	translateb(outdeg24)
	translatec(outdeg34)

	parameter[46] = 10 
	parameter[47] = La 
	parameter[48] = Ha 
	parameter[49] = 0x00 
	parameter[50] = 0x02 

	parameter[51] = 11 
	parameter[52] = Lb 
	parameter[53] = Hb
	parameter[54] = 0x00 
	parameter[55] = 0x02 

	parameter[56] = 12 
	parameter[57] = Lc 
	parameter[58] = Hc 
	parameter[59] = 0x00 
	parameter[60] = 0x02 
	
def Kiri_tengah(x,y,z):

	invers_kinematik5(x,y,-z)
	rad_to_deg5()
	kiri2()
	translated(outdeg15)
	translatee(outdeg25)
	translatef(outdeg35)
	
	parameter[61] = 13 
	parameter[62] = Ld 
	parameter[63] = Hd 
	parameter[64] = 0x00 
	parameter[65] = 0x02 

	parameter[66] = 14 
	parameter[67] = Le 
	parameter[68] = He 
	parameter[69] = 0x00 
	parameter[70] = 0x02

	parameter[71] = 15 
	parameter[72] = Lf 
	parameter[73] = Hf 
	parameter[74] = 0x00 
	parameter[75] = 0x02 

def Kiri_belakang(x,y,z):

	invers_kinematik6(x,y,-z)
	rad_to_deg6()
	kiri3()
	translateg(outdeg16)
	translateh(outdeg26)
	translatei(outdeg36)

	parameter[76] = 16 
	parameter[77] = Lg 
	parameter[78] = Hg 
	parameter[79] = 0x00 
	parameter[80] = 0x02 

	parameter[81] = 17 
	parameter[82] = Lh 
	parameter[83] = Hh 
	parameter[84] = 0x00 
	parameter[85] = 0x02 

	parameter[86] = 18 
	parameter[87] = Li 
	parameter[88] = Hi 
	parameter[89] = 0x00 
	parameter[90] = 0x02 



############################ GERAKAN KEPITING ###################################33

def kepiting_kanan_1(A,alpa,direksi):
	
	sinus_pattern1(A, 5, 2, 3.5,alpa, 0, direksi)
	invers_kinematik1(var_x1,var_y1,var_z1) 
	rad_to_deg1()
	kanan1()
	translate1(outdeg11) 
	translate2(outdeg21+4)
	translate3(outdeg31+3)
	
	parameter[1] = 1 
	parameter[2] = L1 
	parameter[3] = H1 
	parameter[4] = 0x88
	parameter[5] = 0x01

	parameter[6] = 2 
	parameter[7] = L2 
	parameter[8] = H2 
	parameter[9] = 0x88 
	parameter[10] = 0x01 

	parameter[11] = 3 
	parameter[12] = L3 
	parameter[13] = H3 
	parameter[14] = 0x88
	parameter[15] = 0x01 

def kepiting_kanan_2(A,alpa,direksi):
	
	sinus_pattern2(A, 5, 2, 3.5,alpa, 1, direksi)
	invers_kinematik2(var_x2,var_y2,var_z2) 

	rad_to_deg2()
	kanan2()
	translate4(outdeg12)
	translate5(outdeg22+5)
	translate6(outdeg32-1)
	
	parameter[16] = 4
	parameter[17] = L4 
	parameter[18] = H4 
	parameter[19] = 0x88 
	parameter[20] = 0x01 

	parameter[21] = 5 
	parameter[22] = L5 
	parameter[23] = H5 
	parameter[24] = 0x88 
	parameter[25] = 0x01 

	parameter[26] = 6 
	parameter[27] = L6 
	parameter[28] = H6 
	parameter[29] = 0x88
	parameter[30] = 0x01 


def kepiting_kanan_3(A,alpa,direksi):

	sinus_pattern3(A, 5, 2, 3.5,alpa, 0, direksi)
	invers_kinematik3(var_x3,var_y3,var_z3) 
	rad_to_deg3()
	kanan3()
	translate7(outdeg13)
	translate8(outdeg23+1)
	translate9(outdeg33)
	
	parameter[31] = 7 
	parameter[32] = L7 
	parameter[33] = H7 
	parameter[34] = 0x88 
	parameter[35] = 0x01 

	parameter[36] = 8 
	parameter[37] = L8 
	parameter[38] = H8 
	parameter[39] = 0x88 
	parameter[40] = 0x01 

	parameter[41] = 9 
	parameter[42] = L9 
	parameter[43] = H9 
	parameter[44] = 0x88 
	parameter[45] = 0x01 

def kepiting_kiri_1(A,alpa,direksi):

	sinus_pattern4(A, 5, 2, 3.5,alpa, 1, direksi)
	invers_kinematik4(var_x4,var_y4,var_z4)
	rad_to_deg4()
	kiri1()	
	translatea(outdeg14) 
	translateb(outdeg24)
	translatec(outdeg34)
	
	parameter[46] = 10 
	parameter[47] = La 
	parameter[48] = Ha 
	parameter[49] = 0x88 
	parameter[50] = 0x01 

	parameter[51] = 11 
	parameter[52] = Lb 
	parameter[53] = Hb
	parameter[54] = 0x88 
	parameter[55] = 0x01 

	parameter[56] = 12 
	parameter[57] = Lc 
	parameter[58] = Hc 
	parameter[59] = 0x88 
	parameter[60] = 0x01 
	
def kepiting_kiri_2(A,alpa,direksi):

	sinus_pattern5(A, 5, 2, 3.5,alpa, 0, direksi)
	invers_kinematik5(var_x5,var_y5,var_z5)
	rad_to_deg5()
	kiri2()
	translated(outdeg15)
	translatee(outdeg25-5) #+1
	translatef(outdeg35)
	
	parameter[61] = 13 
	parameter[62] = Ld 
	parameter[63] = Hd 
	parameter[64] = 0x88 
	parameter[65] = 0x01 

	parameter[66] = 14 
	parameter[67] = Le 
	parameter[68] = He 
	parameter[69] = 0x88 
	parameter[70] = 0x01

	parameter[71] = 15 
	parameter[72] = Lf 
	parameter[73] = Hf 
	parameter[74] = 0x88 
	parameter[75] = 0x01 

def kepiting_kiri_3(A,alpa,direksi):

	sinus_pattern6(A, 5, 2, 3.5,alpa, 1, direksi)
	invers_kinematik6(var_x6,var_y6,var_z6) 
	rad_to_deg6()
	kiri3()
	translateg(outdeg16)
	translateh(outdeg26-2)
	translatei(outdeg36-1) 
	
	parameter[76] = 16 
	parameter[77] = Lg 
	parameter[78] = Hg 
	parameter[79] = 0x88
	parameter[80] = 0x01 

	parameter[81] = 17 
	parameter[82] = Lh 
	parameter[83] = Hh 
	parameter[84] = 0x88 
	parameter[85] = 0x01 

	parameter[86] = 18 
	parameter[87] = Li 
	parameter[88] = Hi 
	parameter[89] = 0x88 
	parameter[90] = 0x01

############################ GERAKAN PUTAR ###################################33

def putar_kanan_1(A,alpa,direksi):
	
	sinus_pattern1(A, 5, 2.5, 3,alpa, 0, direksi)
	invers_kinematik1(var_x1,var_y1,var_z1) 
	rad_to_deg1()
	kanan1()
	translate1(outdeg11)#-25 #-20
	translate2(outdeg21-3) #+2      #-3
	translate3(outdeg31) #+2
#	print "sudut kanan1: ", outdeg11,", ", outdeg21,", ", outdeg31
	parameter[1] = 1 
	parameter[2] = L1 
	parameter[3] = H1 
	parameter[4] = 0x88
	parameter[5] = 0x01

	parameter[6] = 2 
	parameter[7] = L2 
	parameter[8] = H2 
	parameter[9] = 0x88 
	parameter[10] = 0x01 

	parameter[11] = 3 
	parameter[12] = L3 
	parameter[13] = H3 
	parameter[14] = 0x88
	parameter[15] = 0x01 

def putar_kanan_2(A,alpa,direksi):
	
	sinus_pattern2(A, 5, 2.5, 3,alpa, 1, direksi)
	invers_kinematik2(var_x2,var_y2,var_z2) 

	rad_to_deg2()
	kanan2()
	translate4(outdeg12)
	translate5(outdeg22+6)#+1
	translate6(outdeg32)#-1 #-5
#	print "sudut kanan2: ", outdeg12, ", ", outdeg22, ", ", outdeg32
	parameter[16] = 4
	parameter[17] = L4 
	parameter[18] = H4 
	parameter[19] = 0x88 
	parameter[20] = 0x01 

	parameter[21] = 5 
	parameter[22] = L5 
	parameter[23] = H5 
	parameter[24] = 0x88 
	parameter[25] = 0x01 

	parameter[26] = 6 
	parameter[27] = L6 
	parameter[28] = H6 
	parameter[29] = 0x88
	parameter[30] = 0x01 


def putar_kanan_3(A,alpa,direksi):

	sinus_pattern3(A, 5, 3, 3,alpa, 0, direksi)
	invers_kinematik3(var_x3,var_y3,var_z3) 
	rad_to_deg3()
	kanan3()
	translate7(outdeg13)#+25
	translate8(outdeg23+2)#-2#-0 servo 2 keatas#+4#+2
	translate9(outdeg33)#-2#+2
#	print "sudut kanan3: ", outdeg13, ", ", outdeg23, ", ", outdeg33	
	parameter[31] = 7 
	parameter[32] = L7 
	parameter[33] = H7 
	parameter[34] = 0x88 
	parameter[35] = 0x01 

	parameter[36] = 8 
	parameter[37] = L8 
	parameter[38] = H8 
	parameter[39] = 0x88 
	parameter[40] = 0x01 

	parameter[41] = 9 
	parameter[42] = L9 
	parameter[43] = H9 
	parameter[44] = 0x88 
	parameter[45] = 0x01 

def putar_kiri_1(A,alpa,direksi):

	sinus_pattern4(A, 5, 2.5, 3,alpa, 1, direksi)
	invers_kinematik4(var_x4,var_y4,var_z4)
	rad_to_deg4()
	kiri1()	
	translatea(outdeg14)#-25 
	translateb(outdeg24)#+6#-2
	translatec(outdeg34)#+6#-2
#	print "sudut kiri1: ", outdeg14, ", ", outdeg24, ", ", outdeg34
	parameter[46] = 10 
	parameter[47] = La 
	parameter[48] = Ha 
	parameter[49] = 0x88 
	parameter[50] = 0x01 

	parameter[51] = 11 
	parameter[52] = Lb 
	parameter[53] = Hb
	parameter[54] = 0x88 
	parameter[55] = 0x01 

	parameter[56] = 12 
	parameter[57] = Lc 
	parameter[58] = Hc 
	parameter[59] = 0x88 
	parameter[60] = 0x01 
	
def putar_kiri_2(A,alpa,direksi):

	sinus_pattern5(A, 5, 2.5, 3,alpa, 0, direksi)
	invers_kinematik5(var_x5,var_y5,var_z5)
	rad_to_deg5()
	kiri2()
	translated(outdeg15)
	translatee(outdeg25-6)#-1 #+1#-1 #-2
	translatef(outdeg35)#+1 #+5    #-1
#	print "sudut kiri2: ", outdeg15, ", ", outdeg25, ", ", outdeg35 	
	parameter[61] = 13 
	parameter[62] = Ld 
	parameter[63] = Hd 
	parameter[64] = 0x88 
	parameter[65] = 0x01 

	parameter[66] = 14 
	parameter[67] = Le 
	parameter[68] = He 
	parameter[69] = 0x88 
	parameter[70] = 0x01

	parameter[71] = 15 
	parameter[72] = Lf 
	parameter[73] = Hf 
	parameter[74] = 0x88 
	parameter[75] = 0x01 

def putar_kiri_3(A,alpa,direksi):

	sinus_pattern6(A, 5, 3, 3,alpa, 1, direksi)
	invers_kinematik6(var_x6,var_y6,var_z6) 
	rad_to_deg6()
	kiri3()
	translateg(outdeg16)#-25
	translateh(outdeg26-2)#+2 #-2   #-1
	translatei(outdeg36-1) 
#	print "sudut kiri3: ", outdeg16, ", ", outdeg26, ", ", outdeg36
	parameter[76] = 16 
	parameter[77] = Lg 
	parameter[78] = Hg 
	parameter[79] = 0x88
	parameter[80] = 0x01 

	parameter[81] = 17 
	parameter[82] = Lh 
	parameter[83] = Hh 
	parameter[84] = 0x88 
	parameter[85] = 0x01 

	parameter[86] = 18 
	parameter[87] = Li 
	parameter[88] = Hi 
	parameter[89] = 0x88 
	parameter[90] = 0x01

############################# Gerakkan Iseng ###################################

def iseng_kanan_1(A,alpa,direksi):
	
	iseng_sinus_pattern1(A,5, 2.5, 3,alpa, 0, direksi)
	invers_kinematik1(var_x1,var_y1,var_z1) 
	rad_to_deg1()
	kanan1()
	translate1(outdeg11) 
	translate2(outdeg21+2)
	translate3(outdeg31+2)
	
	parameter[1] = 1 
	parameter[2] = L1 
	parameter[3] = H1 
	parameter[4] = 0x88
	parameter[5] = 0x01

	parameter[6] = 2 
	parameter[7] = L2 
	parameter[8] = H2 
	parameter[9] = 0x88 
	parameter[10] = 0x01 

	parameter[11] = 3 
	parameter[12] = L3 
	parameter[13] = H3 
	parameter[14] = 0x88
	parameter[15] = 0x01 

def iseng_kanan_2(A,alpa,direksi):
	
	iseng_sinus_pattern2(A, 4.5, 2, 3.5,alpa, 1, direksi)
	invers_kinematik2(var_x2,var_y2,var_z2) 

	rad_to_deg2()
	kanan2()
	translate4(outdeg12)
	translate5(outdeg22-1)
	translate6(outdeg32-1)
	
	parameter[16] = 4
	parameter[17] = L4 
	parameter[18] = H4 
	parameter[19] = 0x88 
	parameter[20] = 0x01 

	parameter[21] = 5 
	parameter[22] = L5 
	parameter[23] = H5 
	parameter[24] = 0x88 
	parameter[25] = 0x01 

	parameter[26] = 6 
	parameter[27] = L6 
	parameter[28] = H6 
	parameter[29] = 0x88
	parameter[30] = 0x01 


def iseng_kanan_3(A,alpa,direksi):

	iseng_sinus_pattern3(A, 4.5, 2, 3.5,alpa, 0, direksi)
	invers_kinematik3(var_x3,var_y3,var_z3) 
	rad_to_deg3()
	kanan3()
	translate7(outdeg13)
	translate8(outdeg23-2)
	translate9(outdeg33-2)
	
	parameter[31] = 7 
	parameter[32] = L7 
	parameter[33] = H7 
	parameter[34] = 0x88 
	parameter[35] = 0x01 

	parameter[36] = 8 
	parameter[37] = L8 
	parameter[38] = H8 
	parameter[39] = 0x88 
	parameter[40] = 0x01 

	parameter[41] = 9 
	parameter[42] = L9 
	parameter[43] = H9 
	parameter[44] = 0x88 
	parameter[45] = 0x01 

def iseng_kiri_1(A,alpa,direksi):

	iseng_sinus_pattern4(A, 4.5, 2, 3.5,alpa, 1, direksi)
	invers_kinematik4(var_x4,var_y4,var_z4)
	rad_to_deg4()
	kiri1()	
	translatea(outdeg14) 
	translateb(outdeg24+5)
	translatec(outdeg34+5)
	
	parameter[46] = 10 
	parameter[47] = La 
	parameter[48] = Ha 
	parameter[49] = 0x88 
	parameter[50] = 0x01 

	parameter[51] = 11 
	parameter[52] = Lb 
	parameter[53] = Hb
	parameter[54] = 0x88 
	parameter[55] = 0x01 

	parameter[56] = 12 
	parameter[57] = Lc 
	parameter[58] = Hc 
	parameter[59] = 0x88 
	parameter[60] = 0x01 
	
def iseng_kiri_2(A,alpa,direksi):

	iseng_sinus_pattern5(A, 4.5, 2, 3.5,alpa, 0, direksi)
	invers_kinematik5(var_x5,var_y5,var_z5)
	rad_to_deg5()
	kiri2()
	translated(outdeg15)
	translatee(outdeg25-3) #+1
	translatef(outdeg35-1)
	
	parameter[61] = 13 
	parameter[62] = Ld 
	parameter[63] = Hd 
	parameter[64] = 0x88 
	parameter[65] = 0x01 

	parameter[66] = 14 
	parameter[67] = Le 
	parameter[68] = He 
	parameter[69] = 0x88 
	parameter[70] = 0x01

	parameter[71] = 15 
	parameter[72] = Lf 
	parameter[73] = Hf 
	parameter[74] = 0x88 
	parameter[75] = 0x01 

def iseng_kiri_3(A,alpa,direksi):

	iseng_sinus_pattern6(A, 4.5, 2, 3.5,alpa, 1, direksi)
	invers_kinematik6(var_x6,var_y6,var_z6) 
	rad_to_deg6()
	kiri3()
	translateg(outdeg16)
	translateh(outdeg26+2)
	translatei(outdeg36) 
	
	parameter[76] = 16 
	parameter[77] = Lg 
	parameter[78] = Hg 
	parameter[79] = 0x88
	parameter[80] = 0x01 

	parameter[81] = 17 
	parameter[82] = Lh 
	parameter[83] = Hh 
	parameter[84] = 0x88 
	parameter[85] = 0x01 

	parameter[86] = 18 
	parameter[87] = Li 
	parameter[88] = Hi 
	parameter[89] = 0x88 
	parameter[90] = 0x01
	
def belokkiri():
		kanan_1(6,90,1)
		kanan_2(2,90,1)
		kanan_3(6,90,1)
		kiri_1(1,30,1)#30
		kiri_2(0,90,1)
		kiri_3(2,130,1)
		packet_kirim(AX_WRITE,4,18)
		print "belokkiri"
		
def belokkanan():
		kanan_1(1,130,1)
		kanan_2(0,90,1)
		kanan_3(3.5,30,1)
		kiri_1(6,90,1)
		kiri_2(2,90,1)
		kiri_3(6,90,1)
		packet_kirim(AX_WRITE,4,18)
		print"belokkanan"

def belokkkiri_invers():
		kanan_1(1,110,0)
		kanan_2(0,90,0)
		kanan_3(1,30,0)
		kiri_1(6,90,0)
		kiri_2(2,90,0)
		kiri_3(6,90,0)
		packet_kirim(AX_WRITE,4,18)
		print"belokkiri_invers"

def belokkanan_invers():
                kanan_1(6,90,0)
                kanan_2(2,90,0)
                kanan_3(6,90,0)
                kiri_1(1,30,0)
                kiri_2(0,90,0)
                kiri_3(1,110,0)
                packet_kirim(AX_WRITE,4,18)
                print"belokkiri_invers"

		
def putarkiri_sedang():
		putar_kanan_1(3, 90, 1)
		putar_kanan_2(3, 90, 1)
		putar_kanan_3(3, 90, 1)
		putar_kiri_1(3, 90, 0)
		putar_kiri_2(3, 90, 0)
		putar_kiri_3(3, 90, 0)
		packet_kirim(AX_WRITE,4,18)
		print"putarkirisedang"

def putarkiri_kecil():
		putar_kanan_1(1.5, 90, 1)
		putar_kanan_2(1.5, 90, 1)
		putar_kanan_3(1.5, 90, 1)
		putar_kiri_1(1.5, 90, 0)
		putar_kiri_2(1.5, 90, 0)
		putar_kiri_3(1.5, 90, 0)
		packet_kirim(AX_WRITE,4,18)
		print"putarkirikecil"

def mundur():
		kanan_1(4.5,300,1)
		kanan_2(4.5,90,0)
		kanan_3(4.5,60,0)
		kiri_1(4.5,60,0)
		kiri_2(4.5,90,0)
		kiri_3(4.5,300,1) 
   		packet_kirim(AX_WRITE,4,18)
		print "mundur"

def putarkanan_kecil():
		putar_kanan_1(1.5, 90, 0)
		putar_kanan_2(1.5, 90, 0)
		putar_kanan_3(1.5, 90, 0)
		putar_kiri_1(1.5, 90, 1)
		putar_kiri_2(1.5, 90, 1)
		putar_kiri_3(1.5, 90, 1)
		packet_kirim(AX_WRITE,4,18)
		print "putarkanankecil"

def putarkanan_sedang():

		putar_kanan_1(3, 90, 0)
		putar_kanan_2(3, 90, 0)
		putar_kanan_3(3, 90, 0)
		putar_kiri_1(3, 90, 1)
		putar_kiri_2(3, 90, 1)
		putar_kiri_3(3, 90, 1)
		packet_kirim(AX_WRITE,4,18)
		print "putarkanansedang"
def berdiri(x,y,z):
		Kanan_depan(x,y,z)
		Kanan_tengah(x,y,z)
		Kanan_belakang(x,y,z)
		Kiri_depan(x,y,z)
		Kiri_tengah(x,y,z)
		Kiri_belakang(x,y,z)
		packet_kirim(AX_WRITE,4,18)
		print "berdiri"
def maju():
	kanan_1(4.5,300,0)#135
	kanan_2(3.5,90,1)
	kanan_3(4.5,60,1)
	kiri_1(4.5,60,1)
	kiri_2(3.5,90,1)
	kiri_3(4.5,300,0)#300
	packet_kirim(AX_WRITE,4,18)
	print "maju"

def jalan(left,right):
	kanan_1(right,315,0)
	kanan_2(3.5,90,1)#3.5
	kanan_3(right,60,1)
	kiri_1(left,60,1)
	kiri_2(3.5,90,1)#3.5
	kiri_3(left,300,0)
	packet_kirim(AX_WRITE,4,18)

def tengok():
	iseng_kanan_1(4,90,1)
	iseng_kanan_2(4,90,0)
	iseng_kanan_3(4,90,1)
	iseng_kiri_1(4,90,1)
	iseng_kiri_2(4,90,0)
	iseng_kiri_3(4,90,1)
	packet_kirim(AX_WRITE,4,18)
	print "tengok"

def kepiting_kanan():
		kepiting_kanan_1(3,30,0)
		kepiting_kanan_2(2,180,0)
		kepiting_kanan_3(3,150,1)
		kepiting_kiri_1(3,150,1)
		kepiting_kiri_2(2,0,1)
		kepiting_kiri_3(3,30,0)
		packet_kirim(AX_WRITE,4,18)

def kepiting_kiri():
		kepiting_kanan_1(3,30,1)
		kepiting_kanan_2(2,180,1)
		kepiting_kanan_3(3,150,0)
		kepiting_kiri_1(3,150,0)
		kepiting_kiri_2(2,0,0)
		kepiting_kiri_3(3,30,1)
		packet_kirim(AX_WRITE,4,18)

#############================== GERAKAN KODE ====================###############
#==============================================================================#


#------------------inisialiasi---------------#

clpwm = 0
crpwm = 0

def get_velocity():
	
	global lpwm
	global rpwm
	lpwm = clpwm
	rpwm = crpwm
	
def diamCode():
	
	global clpwm
	global crpwm
	crpwm = -1
	clpwm = -1

def mundurCode():
	
	global crpwm
	global clpwm
	crpwm = -2
	clpwm = -2

def belokkananCode():
	
	global clpwm
	global crpwm
	clpwm = -3
	crpwm  = -3

def putarkanansedangCode():
	
	global clpwm
	global crpwm
	clpwm = -5
	crpwm = -5

def putarkanankecilCode():
	
	global clpwm
	global crpwm
	clpwm = -4
	crpwm = -4
	print "putarkanankecilCode"
def kepitingkananCode():
	
	global clpwm
	global crpwm
	clpwm = -6
	crpwm = -6	
	
def belokkiriCode():
	
	global clpwm
	global crpwm
	clpwm = -7
	crpwm  = -7
		
def putarkirisedangCode():
	
	global clpwm
	global crpwm
	clpwm = -9
	crpwm = -9

def putarkirikecilCode():
	
	global clpwm
	global crpwm
	clpwm = -8
	crpwm = -8

def kepitingkiriCode():
	
	global clpwm
	global crpwm
	clpwm = -10
	crpwm = -10

def majuCode():

	global clpwm
	global crpwm
	clpwm = -11
	crpwm = -11

def putarkanansedangspCode():

	global clpwm
	global crpwm
	clpwm = -12
	crpwm = -12

def putarkirisedangspCode():

	global clpwm
	global crpwm
	clpwm = -13
	crpwm = -13

def mundurlambatCode():

	global clpwm
	global crpwm
	clpwm = -14
	crpwm = -14

def kepitingkirispCode():

	global clpwm
	global crpwm
	clpwm = -15
	crpwm = -15

def tengokCode():

	global clpwm
	global crpwm
	clpwm = -16
	crpwm = -16

#@multitasking.task	
def gerak():
	global sudut
	sudut=0
	#print "sudut",sudut
	while (sudut<=360):
		sudut+=  22.5 #22.5 #20
		#print "sudut", sudut
		#print "lpwm",lpwm,"rpwm",rpwm
		if((sudut== 270) or (sudut== 360)):
				
			get_velocity()

		if ((rpwm == -1) and (lpwm == -1)):
				
			berdiri(0,4,2.7)
			#print "diam"
				
		elif ((rpwm == -2) and (lpwm == -2)):
			
			mundur()
			time.sleep(0.01)#0.01 #                   ini bang cand
			#print"mundur"
							
		elif ((rpwm == -3) and (lpwm == -3)):
		
			belokkanan()
			time.sleep(0.009)#amar(0.005)/zae(0.01)0.009===========================ini
		#	sudut+=5
			#print"belokkanan"

		elif ((lpwm == -4) and (rpwm == -4)):
	
			putarkanan_kecil()
			time.sleep(0.05)     #      ini bnag cand
			print"putarkanan_kecil"
										
		elif ((rpwm == -5) and (lpwm == -5)):
				
			putarkanan_sedang()
			time.sleep(0.009)            # ini bang cand
			print"putarkanan_sedang"	
		
		elif ((rpwm == -6) and (lpwm == -6)):
				
			kepiting_kanan()
			#time.sleep(0.004)
			#print"kepiting_kanan"

		elif ((rpwm == -7) and (lpwm == -7)):
				
			belokkiri()
			time.sleep(0.009)#0.01#0.009 #     ini bang cand
			#print"belokkiri"
																								
		elif ((lpwm == -8) and (rpwm == -8)):

			putarkiri_kecil()
			time.sleep(0.009) #ini bangcand #########################333
			#print"putarkiri_kecil"
		
		elif ((rpwm == -9) and (lpwm == -9)):
			
			putarkiri_sedang()
			time.sleep(0.009) #ini bangcand#############################
			print"putarkiri_sedang"

		elif ((rpwm == -10) and (lpwm == -10)):
				
			kepiting_kiri()
			#time.sleep(0.004)
			#print"kepiting_kiri"
					
		elif ((rpwm == -11) and (lpwm == -11)):

			maju()
			time.sleep(0.009)#0.003 ini #########################
			#print"maju"		

		elif ((rpwm == -12) and (lpwm == -12)):

			putarkanan_sedang()
			time.sleep(0.003) #ini bang cand ################33
			print "putar kanan spesial"

		elif ((rpwm == -13) and (lpwm == -13)):

			putarkiri_sedang()
			time.sleep(0.01)
			print "putar kiri spesial"

		elif ((rpwm == -14) and (lpwm == -14)):

			mundur()
			time.sleep(0.04)#         ini bang cand
			print "mundur code dipanggil"

		elif ((rpwm == -15) and (lpwm == -15)):

			kepiting_kiri()
			#time.sleep(0.004)

		elif ((rpwm == -16) and (lpwm == -16)):

			tengok()
			time.sleep(0.09)# ini bang cadn
			#print "goyang inul"

		else:
				
			jalan(lpwm,rpwm)
		#	time.sleep(0.0005)
			#print"jalan"

def ratasta():
	ultra_deka(0.03)
	ultra_deki(0.03)
	ultra_kanan(0.03)
	ultra_kiri(0.03)
	ultra_beki(0.03)
countnilai=0
#######################################################
def cek_start():	
	global passtart
	global countnilai
	global b6
	ultra_deka(0.03)
	ultra_deki(0.03)
		#print "sensdeka :",sensdeka4
		#print "sensdeki :",sensdeki4
	if ((b3>=20) or (b4>=20)):
		print "gada depan"
		ultra_deki(0.03)
	#	ultra_deka(0.03)
		while ((b3>20) or (countnilai<10)):
			putarkanansedangCode()
					#print "putar kanan"
			ultra_deki(0.03)
			ultra_deka(0.03)
			if (b3<=15):
				countnilai+=1
					#print "data kanan :",senskanan4,"countnilai :",countnilai
		#elif (b1<9):

			print "kanan deket"
	elif ((b3<20) or (b4<20)):
		print "ada depan"
		ultra_kanan(0.03)
		while((b6>9) or (countnilai<10)):
				#print "putar kiri"
			putarkirisedangCode()
				#ultra_beka(0.03)
			ultra_kanan(0.03)
			if (b6<=9):
				countnilai+=1
				#print "data beka :",sensbeka4,"beki :",sensbeki4,"countnilai :",countnilai
	diamCode()
	time.sleep(0.125)
	print "hampir siap jalan"						

#############################################mainprogram########
global start
global sound
misiapi=0
mulai=0
start=0
sound=0
countpu=0
done=0
def mainpro():
	global mulai
	global countpu
	global done
	if (done==1):
		diamCode()
	elif(mulai==0):
	#	tombol_start()                        #manipulasi tombol start dan stop pada 1 kill plug
		sound_act(20)
		print "masuk pengecekan tombol atau sound"
		if((start==0) and (sound==0)):   #kondisi stand by robot
			print "robot standby"
			diamCode()
		elif((start==1) or (sound==1)): #start menggunakan tombol atau sound
			print "pengubahan var_mulai, pengecekan kondisi start"
			cek_start()                   #berputar sampai kondisi ultra depan dan kanan dekat, lalu berputar balik
			#countkeluarhome=0
			#skipperataan=1
			while(countpu<50):#100
				Susur_Kananspesial()
				countpu=countpu+1
				print countpu
				#countkeluarhome+=1
				#print "susur spesial countkeluarhome:",countkeluarhome	
			mulai=1                       #agar tidak mengecek kembali tombol start atau sound

	elif(mulai==1):
		if((start==1) or (sound==1)): 
			arahjalan()

susurkiri=0
susurkanan=0
garisbalik1=0
garisbalik2=0
garpul=0
def arahjalan():
	global misiapi
	global countgaris
	global asal
	global jalanmisi
	global asal
	global garisapi
	global susurkiri
	global susurkanan
	global garisbalik1
	global garisbalik2
	global garpul
#	if(api==1):
#		Susur_Kiri()
	if(misiapi==0):
		if(api==0):
			print "anak sehat"
			Susur_Kanan()
		elif(api==1):
			print"susurkirispesialmisiapi0adaapi "
			Susur_Kirispesial()
	elif(misiapi==1):
		if(garpul==0):
			print "garpul=0 misiapi=1"
			Susur_Kananspesial2()
		elif(garpul==1):
			print"garpul=1 misiapi=1 dan sudah keluar ruangan api"
			if(garisapi<=3):#tadinya 4 sebelum garpul
				Susur_Kiri()
				susurkiri=1
				susurkanan=0
				garisbalik1=1
				garisbalik2=0
				print "susur kiri mainpro balik"
			else:
				Susur_Kanan()
				susurkanan=1
				susurkiri=0
				garisbalik1=0
				garisbalik2=1	
				print "susur kanan mainpro balik"		
#################################################################### Multithreading gerak dasar#######################################################################
######################################################################################################################################################################

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)   # You must do this before anything else
        self.daemon = True      # Causes thread termination of program exit

    def run(self):
        try:
            while True:
		#Susur_Kananspesial2()
		#Susur_Kanan()
		#maju()
		#Susur_Kananspesial()
		#Susur_Kiri()
		#Susur_Kirispesial()
		mainpro()
		#putther3()
		#main_coba()
		#mundurCode()
		#tengoksemprot()
		#kepitingkiriCode()
        except (KeyboardInterrupt, SystemExit):
            pass

class MyThread1(Thread):
    def __init__(self):
        Thread.__init__(self)   # You must do this before anything else
        self.daemon = True      # Causes thread termination of program exit

    def run(self):
        try:
            while True:
		gerak()
		#maju()
		#main_coba()
		#ultra_kade(0.03)
		#ultra_kide(0.03)
		#ultra_deka(0.03)
        except (KeyboardInterrupt, SystemExit):
            pass
############################################### bangcan
#signal.signal(signal.SIGINT, multitasking.killall)
#@multitasking.task
#global threadLock
#class myThread(threading.Thread):
#	def __init__(self,threadID, name, counter):
#		threading.Thread.__init__(self)
#		self.threadID=threadID
#		self.name=name
#		self.counter=counter
#	def run(self):
#		try:
#			while True:
#				threadLock.acquire()
#				#gerak()
#				Susur_Kanan()
#				threadLock.release()
#		except (KeyboardInterrupt, SystemExit):
#			pass
#class myThread2(threading.Thread):
#        def __init__(self,threadID, name, counter):
#                threading.Thread.__init__(self)
#                self.threadID=threadID
#                self.name=name
#                self.counter=counter
#        def run(self):
#                try:
#                        while True:
#                                threadLock.acquire()
                                #Susur_Kanan()
				#putarkirisedangCode()
#				gerak()
#                                threadLock.release()
#                except (KeyboardInterrupt, SystemExit):
#                        pass


def tengoksemprot():
	tengokCode()
	air3()
	time.sleep(0.5)

def multithread():
	if __name__ == '__main__':
		thread = MyThread()
		thread1= MyThread1()
		thread.start()
		thread1.start()
		try:
			while thread.is_alive():

				thread.join()
				thread1.join()
		except (KeyboardInterrupt, SystemExit):
			print 'Shutting down ...'

##########################################sound activation###########
countingsound = 0
GPIO.setup("P8_16",GPIO.IN)

def sound_act(count):
	global sound
	global countingsound
	for i in range(0,count):
		GPIO.input("P8_16")
		if((GPIO.input("P8_16"))==0):
			countingsound=countingsound+1
			
		else:
			countingsound=0
	#		print "gada"	
	if(countingsound>=5):
		sound=1
		ledmic()
		print "ada suara"
	else:
		sound=0
		print "gada suara"

###############################################Buzzer Blinking Led #################################################################################
######################################################################################################################################################################

GPIO.setup("P9_17", GPIO.OUT)#LEDMIC
GPIO.setup("P9_11", GPIO.OUT)#LEDLILIN
GPIO.setup("P9_24", GPIO.OUT)#BUZZER
GPIO.setup("P9_18", GPIO.IN,pull_up_down=GPIO.PUD_UP)#LIMITSWITCH
GPIO.setup("P8_26", GPIO.IN)#FLAME KIRI
GPIO.setup("P8_11", GPIO.IN)#FLAME KANAN
def ledlilin():
	#sleselilin=0
	if(api==1):
		#while (apiruang==1):
		GPIO.output("P9_11", GPIO.HIGH)
		#sleselilin=1
		
	else:
		GPIO.output("P9_11", GPIO.LOW)
def ledlilin2():
	GPIO.output("P9_11",GPIO.HIGH)
	time.sleep(0.01)
	print "blinklilin"
	GPIO.output("P9_11",GPIO.LOW)
	time.sleep(0.01)
def ledmic():
	for i in range(0,4):
		GPIO.output("P9_17", GPIO.HIGH)
		time.sleep(0.1)
		print "blink mic"
		GPIO.output("P9_17", GPIO.LOW)
		time.sleep(0.1)		
def buzzer():
	GPIO.output("P9_24",GPIO.HIGH)
	time.sleep(0.2)
	print "buzzer"
	GPIO.output("P9_24",GPIO.LOW)
	time.sleep(0.02)
	print "buzzer mati"
############################## flame ### Limit Swtich ####################################################################################
#susurkanan==1
#susurkiri==0
#GPIO.setup("pin", GPIO.IN,pull_up_down=GPIO_PUD.UP)
#susurkanan=1
#susurkiri=0
def limitswitch():
	#data=gpio.input(limit)
	global susurkanan
	global susurkiri
	#GPIO.setup("P9_18",GPIO.IN)
	if(GPIO.input("P9_18")==0):
		print "kepencet CUK!!!!!!"
		mundurCode()
#		susurkanan=1
#		susurkiri=0
		time.sleep(0.3)
		if((susurkanan==1) and (susurkiri==0)):
			putarkirisedangCode()
			time.sleep(0.55)
		elif((susurkanan==0) and (susurkiri==1)):
			putarkanansedangCode()
			time.sleep(0.55)
	#else:
	#	print"tai"
def flamesen1():
	global flame1
	if(GPIO.input("P8_26")==0):
		flame1=1
		print "===========================================================================ada kesayangan di kiri kena flame kiri"
	print GPIO.input("P8_26")
def flamesen2():
	if(GPIO.input("P8_11")==0):
		flame2=1
		print "===========================================================================ada kesayangan di kanan kena flame kanan"
	print GPIO.input("P8_11")
#############################
def cari_api():
	global api

	cekUV(3)
	if(api==0):
		tengokCode()
		cekUV(3)
		if (api==1):
			majuCode()
			time.sleep(0.45)
	elif (api==1):
		majuCode()
		time.sleep(0.45)		
############################################################################# Infrared ###############################################################################
######################################################################################################################################################################


#infrared_bawah 	= 1
#infrared_atas 	= 1

def infrared1():
	global infrared_bawah
	global infrared_atas
	global jalanmisi
	GPIO.setup("P9_27",GPIO.IN)#sebenernya ini bAWAH
	GPIO.setup("P9_41",GPIO.IN)#sebernya ini yang atas


	infrared_atas = (GPIO.input("P9_27"))
	infrared_bawah = (GPIO.input("P9_41"))
	#kill_plug()
	#if ((jalanmisi==0)and(kill==0)):
	#print "ATAS:",infrared_atas
        #print "bawah",infrared_bawah


	if ((infrared_atas==1)and(infrared_bawah==0)):
		print "ANJINGGG!!!!!!"
		#print "atas",infrared_atas
 		#print "atas",infrared_bawah
 
		#kill_plug()
		diamCode()
		time.sleep(0.125)
		#geser()
		mundurCode()
		time.sleep(0.70)
		diamCode()
		time.sleep(0.125)
		putarkirisedangCode()
		time.sleep(1.50)#150
		diamCode()
		time.sleep(0.125)

def infrared2():
	global infrared_bawah
	global infrared_atas
	global jalanmisi
	GPIO.setup("P9_27",GPIO.IN)
	GPIO.setup("P9_41",GPIO.IN)


	infrared_atas = (GPIO.input("P9_27"))
	infrared_bawah = (GPIO.input("P9_41"))
	#kill_plug()
	#if ((jalanmisi==0)and(kill==0)):
	#print "ATAS:",infrared_atas
	#print "bawah",infrared_bawah


	if ((infrared_atas==1)and(infrared_bawah==0)):
		print "ANJINGGG!!!!!!"
		print "atas",infrared_atas
 		print "atas",infrared_bawah
 
		#kill_plug()
		diamCode()
		time.sleep(0.125)
		#geser()
		mundurCode()
		time.sleep(0.70)
		diamCode()
		time.sleep(0.125)
		putarkanansedangCode()
		time.sleep(1.45)
		diamCode()
		time.sleep(0.125)		
#############================== mainan larutan ====================###############
#==============================================================================#

def main_coba():
	berdiri(0,4,2.7)
	time.sleep(3)
	#sudut = 0
	while True:
		global sudut
		sudut = 0
		while (sudut <=360):
			sudut += 3
			#mundur()
			#maju()
			#jalan()
			#putarkiri_sedang()
			#putarkiri_kecil()
			#putarkanan_sedang()
			#putarkanan_kecil()
			#tengok()
			#belokkiri()
			#belokkanan()
			#putarkiri_sedang()
			#putarkiri_kecil()
			berdiri()
			#kepiting_kanan()
			#kepiting_kiri()
			#time.sleep(0.01)
#############################################
def normalisasi_velocity():
	global clpwm
	global crpwm

	clpwm = lpwm
	crpwm = rpwm

	
	
	################################################################## ~~~~ SUSUR PROXY ~~~~ ########################################################################
#@multitasking.task
def Susur_Kanan():
	global mpi
	global last_error
	global lpwm
	global rpwm
	global susurkanan
	global susurkiri
	susurkanan=1
	susurkiri=0
	#print "susur spesial"
	#lpwm=3.5
	#rpwm=3.5
	ultra_kade(0.005)
	ultra_deka(0.005)
	ultra_deki(0.005)
	infrared1()
	thermal1102()
	limitswitch()
	ledlilin()
	proxi()
	if(b4<19) and (b3<19):
		infrared1()
		limitswitch()
		thermal1102()
		proxi()
		while((b4<18) and (b3<18)):
			infrared1()
			limitswitch()
			proxi()
			thermal1102()
			putarkirisedangCode()
			lpwm=-9
			rpwm=-9
			ultra_deka(0.09)####### 0.09
			ultra_deki(0.09)####### 0.09
			print "putarkiri"
			time.sleep(0.22) ######ni bnag cand####################################

	elif(b5>=35):
		infrared1()
		limitswitch()
		thermal1102()
		proxi()
		#maju()
		#time.sleep(0.4)
		while((b4>20) and (b3>20) and (b5>=21)):
			infrared1()
			limitswitch()
			thermal1102()
			proxi()
			belokkananCode()
			ultra_deka(0.005)
			ultra_deki(0.005)
			ultra_kade(0.005)
			#print "kade",ultra_kade
			proxi()
			print "belokkanan"
			time.sleep(0.1) #ini bang cand****************************************
	elif(b5<=11):
		infrared1()
		thermal1102()
		limitswitch()
		proxi()
		while(b5<=11):
			kepitingkiriCode()
			infrared1()
			thermal1102()
			limitswitch()
			proxi()
			ultra_kade(0.03)
	else:	
		infrared1()
		limitswitch()
		thermal1102()
		proxi()
		error=(b5-17)
		P=(kp1*error)
		It=((error+last_error)*ki1)
		rate=(error-last_error)
		D=(rate*kd1)
		MV=(P+D+It)
		lpwm=4+MV
		rpwm=4-MV
		last_error=error
		if(rpwm>4):
			rpwm=4
		if(rpwm<0):
			rpwm=0
		if(lpwm>4):
			lpwm=4
		if(lpwm<0):
			lpwm=0
		normalisasi_velocity()
		#print "pid"
		#print "rpwm",rpwm
		#print "lpwm",lpwm
		print "susurkanan", susurkanan
		print "susurkiri", susurkiri
		time.sleep(Var_waktu)
######################################################################## ~~~~ PID ~~~~ ###############################################################################
error		= 0.0
last_error	= 0
kp1		= 0.8 #0.4 #0.55
kpspecial1	= 5
kp2		= 0.8#0.3
ki1		= 0
ki2		= 0
kd1		= 0.0 #0.3
kd2		= 0.0
P		= 0.0
It		= 0.0
D		= 0.0
rate		= 0.0
MV		= 0.0
Var_waktu	= 0.0
lpwm		= 0
rpwm		= 0
countbelok	= 0
susurkanan	= 0
susurkiri	= 0
loopmuterkanan	= 0
loopmuterkiri	= 0

################################################################## ~~~~ SUSUR TANPA PROXY ~~~~ ########################################################################

def Susur_Kananspesial():
	global mpi
	global last_error
	global lpwm
	global rpwm
	global susurkanan
	global susurkiri
	susurkanan=1
	susurkiri=0
	#print "susur spesial"
	#lpwm=3.5
	#rpwm=3.5
	ultra_kade(0.03)
	ultra_deka(0.03)
	ultra_deki(0.03)
	print "kade",b5
	#thermal1102()
	#proxi()
	if(b4<19) and (b3<19):
		#thermal1102()
	#	proxi()
		while((b4<18) and (b3<18)):
	#		proxi()
			#thermal1102()
			putarkirisedangCode()
			ultra_deka(0.09)
			ultra_deki(0.09)
			time.sleep(0.1)

	elif(b5>=30):#otan 17
		#thermal1102()
	#	proxi()
		while((b4>19) and (b3>19) and (b5>=23)):#otan 18
			#thermal1102()
	#		proxi()
			belokkananCode()
			ultra_deka(0.09)
			ultra_deki(0.09)
			ultra_kade(0.06)
			#proxi()
			#time.sleep(0.1)
	elif(b5<=11):
                infrared1()
                thermal1102()
                limitswitch()
                #proxi()
                while(b5<=11):
                        kepitingkiriCode()
                        infrared1()
                        thermal1102()
                        limitswitch()
                  #      proxi()
                        ultra_kade(0.03)

	else:	
		#thermal1102()
	#	proxi()
		error=(b5-20)
		P=(kp1*error)
		It=((error+last_error)*ki1)
		rate=(error-last_error)
		D=(rate*kd1)
		MV=(P+D+It)
		lpwm=4.5+MV
		rpwm=4.5-MV
		last_error=error
		if(rpwm>4.5):
			rpwm=4.5
		if(rpwm<0):
			rpwm=0
		if(lpwm>4.5):
			lpwm=4.5
		if(lpwm<0):
			lpwm=0
		normalisasi_velocity()
		#print "pid"
		#print "rpwm",rpwm
		#print "lpwm",lpwm
		time.sleep(Var_waktu)
loopmuterkanan=0
konk=0
def Susur_Kananspesial2():
        global mpi
        global last_error
        global lpwm
        global rpwm
        global susurkanan
        global susurkiri
	global loopmuterkanan
	global konk
        susurkanan=1
	susurkiri=0
        #print "susur spesial"
        #lpwm=3.5
        #rpwm=3.5
        ultra_kade(0.03)
        ultra_deka(0.03)
        ultra_deki(0.03)
        #print "kade",b5
        #thermal1102()
        proxi()
        if(b4<19) and (b3<19):
                #thermal1102()
                proxi()
                while((b4<18) and (b3<18)):
                        proxi()
                        #thermal1102()
                        putarkirisedangCode()
                        ultra_deka(0.09)
                        ultra_deki(0.09)
                        time.sleep(0.25)
	elif(b5>=30):#otan 17
                #thermal1102()
                proxi()
                while((b4>19) and (b3>19) and (b5>=23)):#otan 18
                        #thermal1102()
			if(loopmuterkanan<=400):
                        	proxi()
                        	belokkananCode()
                        	ultra_deka(0.09)
                        	ultra_deki(0.09)
                        	ultra_kade(0.06)
				limitswitch()
                        	proxi()
				loopmuterkanan+=1
				print loopmuterkanan
			elif(loopmuterkanan>400):
				loopmuterkanan=0
				ultra_deka(0.09)
				ultra_deki(0.09)
				while(((b3>15) or (b4>15))and(konk<=140)):
                        		majuCode()
					#time.sleep(0.01)
                        		ultra_deka(0.09)
                        		ultra_deki(0.09)
					konk+=1
					print konk
                        		#time.sleep(0.06)
			#		loopmuterkanan=0
                        #time.sleep(0.1)
	elif(b5<=11):
                infrared1()
                thermal1102()
                limitswitch()
                proxi()
                while(b5<=11):
                        kepitingkiriCode()
                        infrared1()
                        thermal1102()
                        limitswitch()
                        proxi()
                        ultra_kade(0.03)

        else:
                #thermal1102()
                proxi()
                error=(b5-17)#13 iniiiiiiiiiiiiiiiiii
                P=(kpspecial1*error)
                It=((error+last_error)*ki1)
                rate=(error-last_error)
                D=(rate*kd1)
                MV=(P+D+It)
                lpwm=4.5+MV
                rpwm=4.5-MV
                last_error=error
                if(rpwm>4.5):
                        rpwm=4.5
                if(rpwm<0):
                        rpwm=0
                if(lpwm>4.5):
                        lpwm=4.5
                if(lpwm<0):
                        lpwm=0
                normalisasi_velocity()
                #print "pid"
                #print "rpwm",rpwm
                #print "lpwm",lpwm
                time.sleep(Var_waktu)



susurkiri=0
def Susur_Kiri():
	global mpi
	global last_error
	global lpwm
	global rpwm
	global susurkiri
	susurkiri=1
	susurkanan=0
	ultra_kide(0.03)
	ultra_deka(0.03)
	ultra_deki(0.03)
	ultra_kiri(0.03)
	infrared2()
	thermal1102()
	ledlilin()
        limitswitch()
	proxi()
	print"susurkiri"

	if(b4<20) and (b3<20):
		infrared2()
		thermal1102()
                limitswitch()
	        proxi()

		while((b4<19) and (b3<19)):
			infrared2()
                	limitswitch()
			thermal1102()
			proxi()

			putarkanansedangCode()
			ultra_deka(0.09)
			ultra_deki(0.09)
			print "putarkanan"
			time.sleep(0.22)#0.2

	elif(b2>30):#25
		infrared2()
                limitswitch()
        	proxi()
		thermal1102()

		while((b4>20) and (b3>20) and (b2>35)):
			thermal1102()
			infrared2()
                	limitswitch()
 	      		proxi()
			belokkiriCode()
			ultra_deka(0.005)
			ultra_deki(0.005)
			ultra_kide(0.005)#0.06
			print "belokkiri"
			time.sleep(0.01)
	elif(b2<=9):
		infrared2()
		limitswitch()
		proxi()
		thermal1102()
		while(b2<=9):
			kepitingkananCode()
			infrared2()
			thermal1102()
			limitswitch()
			proxi()
			ultra_kide(0.03)
	else:
		infrared2()
                limitswitch()
        	proxi()
		thermal1102()

		error=(b2-15)#21
		P=(kp2*error)
		It=((error+last_error)*ki1)
		rate=(error-last_error)
		D=(rate*kd1)
		MV=(P+D+It)
		lpwm=4-MV
		rpwm=4+MV
		last_error=error
		if(rpwm>4):
			rpwm=4
		if(rpwm<0):
			rpwm=0
		if(lpwm>4):
			lpwm=4
		if(lpwm<0):
			lpwm=0
		normalisasi_velocity()
		print "pid"
		time.sleep(Var_waktu)

loopmuterkiri=0
konq=0
####################susurkirispesial
def Susur_Kirispesial():
	global mpi
	global last_error
	global lpwm
	global rpwm
	global susurkanan
	global susurkiri
	global loopmuterkiri
	global konq
	susurkiri=1
	susurkanan=0
	ultra_kide(0.03)
	ultra_deka(0.03)
	ultra_deki(0.03)
	#infrared2()
	thermal1102()
        limitswitch()
	proxi()

	if(b4<20) and (b3<20):
		#infrared2()
		thermal1102()
                limitswitch()
	        proxi()
		while((b4<19) and (b3<19)):
		#	infrared2()
	                limitswitch()
			thermal1102()
		    	proxi()

			putarkanansedangCode()
			ultra_deka(0.09)
			ultra_deki(0.09)
			print "putarkanan"
			time.sleep(0.1)#0.15

	elif(b2>25):
		#infrared2()
                limitswitch()
        	proxi()
		thermal1102()
		while((b4>20) and (b3>20) and (b2>25)):
			if(loopmuterkiri<=200):#250
                                thermal1102()
                                belokkiriCode()
                                ultra_deka(0.09)
                                ultra_deki(0.09)
                                ultra_kade(0.06)
                                limitswitch()
                                proxi()
                                loopmuterkiri+=1
                                print loopmuterkiri
				time.sleep(0.009)#0.01
                        elif(loopmuterkiri>200):
                                loopmuterkiri=0
                                ultra_deka(0.09)
                                ultra_deki(0.09)
                                while(((b3>20) or (b4>20))and(konq<=70)):#55
                                        majuCode()
                                        #time.sleep(0.01)
                                        ultra_deka(0.09)
                                        ultra_deki(0.09)
                                        konq+=1
                                        print konq

		#	thermal1102()
		#	infrared2()
                #	limitswitch()
        	#	proxi()
		#	belokkiriCode()
		#	ultra_deka(0.09)
		#	ultra_deki(0.09)
		#	ultra_kide(0.06)#0.06
		#	print "belokkiri"
		#	time.sleep(0.01)
	elif(b2<=9):
                infrared2()
                limitswitch()
                proxi()
                thermal1102()
                while(b2<=9):
                        kepitingkananCode()
                        infrared2()
                        thermal1102()
                        limitswitch()
                        proxi()
                        ultra_kide(0.03)

	else:
		#infrared2()
                limitswitch()
        	proxi()
		thermal1102()

		error=(b2-15)
		P=(kp2*error)
		It=((error+last_error)*ki1)
		rate=(error-last_error)
		D=(rate*kd1)
		MV=(P+D+It)
		lpwm=4.5-MV
		rpwm=4.5+MV
		last_error=error
		if(rpwm>4.5):
			rpwm=4.5
		if(rpwm<0):
			rpwm=0
		if(lpwm>4.5):
			lpwm=4.5
		if(lpwm<0):
			lpwm=0
		normalisasi_velocity()
		print "pid"
		time.sleep(Var_waktu)	
########################################################## thermal dan kompas
address1 = 0x69
address2 = 0x68
address3 = 0x6a
address4 = 0x60

pixel1=range(9)
pixel2=range(9)
pixel3=range(9)
bear1=0
bear2=0

def thermalbus1():
	global thermal1
        thermal1 = bus.read_byte_data(address1, reg1)
        return thermal1

def thermalbus2():
	global thermal2
	thermal2 = bus.read_byte_data(address2, reg2)
	return thermal2
def thermalbus3():
	global thermal3
	thermal3 = bus.read_byte_data(address3, reg3)
    	return thermal3
	
def thermalreg1():
	global thermal123
	global reg1
	
	reg1 = 0x00
	
	thermal123 = thermalbus1()
	revision1 = thermal123
	
	reg1 = 0x01

	thermal123 = thermalbus1()
	ambient1 = thermal123

	for i in range(0,8):
		reg1=reg1+1
		thermalbus1()
		pixel1[i] = thermal1
	time.sleep(0.004)
	print "thermal1 :",pixel1[0],pixel1[1],pixel1[2],pixel1[3],pixel1[4],pixel1[5],pixel1[6],pixel1[7]

def thermalreg2():
	global thermal321
	global reg2
	
	reg2= 0x00

	thermal321 = thermalbus2()
	revision2 = thermal321
	
	reg2 = 0x01
	
	thermal321 = thermalbus2()
	ambient2 = thermal321

	for j in range(0,8):
		reg2=reg2+1
		thermalbus2()
		pixel2[j] = thermal2
	time.sleep(0.004)
	print "thermal2 :",pixel2[0],pixel2[1],pixel2[2],pixel2[3],pixel2[4],pixel2[5],pixel2[6],pixel2[7]
	
def thermalreg3():
	global thermal111
	global reg3
	
	reg3 = 0x00
	
	thermal111 = thermalbus3()
	revision3 = thermal111
	
	reg3 = 0x01

	thermal111 = thermalbus3()
	ambient3 = thermal111

	for i in range(0,8):
		reg3=reg3+1
		thermalbus3()
		pixel3[i] = thermal3
	time.sleep(0.004)
	print "thermal3 :",pixel3[0],pixel3[1],pixel3[2],pixel3[3],pixel3[4],pixel3[5],pixel3[6],pixel3[7]

countning=0
def kanputarbalik():
	global countning
	ultra_deka(0.03)
        ultra_deki(0.03)
                #print "sensdeka :",sensdeka4
                #print "sensdeki :",sensdeki4
        #if ((b3>=20) or (b4>=20)):
         #       print "gada depan"
          #      ultra_deki(0.03)
	#	ultra_deka(0.03)
        while (((b3>25)or(b4>25))and(countning<190)):
        	putarkirisedangCode()
                                        #print "putar kanan"
                ultra_deki(0.03)
                ultra_deka(0.03)
		countning+=1
		print countning
	ledlilin()

flame1=0
flame2=0
cono=0
def thermal1102():
	global misiapi
	global skipperataan
	global apikanan
	global apikiri
	global flame1
	global flame2
	global cono
	#ultra_kide(0.06)
	#cekUV(2)###############             COBAAAAAAAAAAAAAAAAAAAAAAAA
	#ledlilin2()
 	if(api==1):
		#print "masuk cek thermal"
		#cekUV(3)#####################         COBAAAAAAAAAAAAAAAAAAAAAAAAAAAA
		thermalreg1()
		thermalreg2()
		thermalreg3()
		flamesen1()
		flamesen2()
		ledlilin()
		if((pixel1[0]>=80)or(pixel1[1]>=80)or(pixel1[2]>=80)or(pixel1[3]>=80)or(pixel1[4]>=80)or(pixel1[5]>=80)or(pixel1[6]>=80)or(pixel1[7]>=80)):
			print "api ada di depan"
			tengokCode()
			time.sleep(0.125)
			air3()
			cekUV(3)
			print "cek uv 1 nilai api:",api
			if(api==1):
				print "masih ada api di depan"
				tengokCode()
				cekUV(3)
				countkipas=0
				while((api==1)and(countkipas<2)):
					tengokCode()
					time.sleep(0.125)
					air3()
					cekUV(3)
					countkipas+=1
					print "COUNTKIPAS ",countkipas
				time.sleep(0.004)
				#cekUV(3)
				#print "cek uv 3 nilai api:",api
				#time.sleep(0.004)
				cono=0
				#cekUV(3)
				#print "cek uv 4 nilai api:",api
				if(api==0):
					diamCode()
                                        cekUV(5)
                                        time.sleep(0.5)
					if(api==0):
                                                print "api di depan udah mati1"
                                                misiapi=1
						#ledlilin()
                                                kanputarbalik()
						#ledlilin()
				elif(api==1):
                                        while(cono<3):#while
                                                mundurCode()
                                                time.sleep(0.25)
                                                cono+=1
						if(cono==2):
                                                        tengokCode()
                                                        time.sleep(0.125)
                                                        air3()
                                                diamCode()
                                                cekUV(5)
                                                time.sleep(1)
                                                if(api==0):
                                                        print "api di depanmati 2"
                                                        misiapi=1
							#ledlilin()
                                                        kanputarbalik()
							#ledlilin()
					diamCode()
                                        cekUV(5)
                                        time.sleep(1)
					if(api==0):
                                                print "api di depan udah mati 3"
                                                misiapi=1
						#ledlilin()
                                                kanputarbalik()
						#ledlilin()

			elif(api==0):
				diamCode()
                                cekUV(5)
                                time.sleep(0.5)
                                if(api==0):
					print "api di depan udah mati ===="
                                        misiapi=1
					#ledlilin()
                                        kanputarbalik()
					#ledlilin()
				#print "api di depan udah mati"
				#majuCode()
				#time.sleep(0.5)
				#flame1=0
				#flame2=0
				#misiapi=1

				#skipperataan=1
				#kanputarbalik()
		if(((pixel2[0]>=70)or(pixel2[1]>=70)or(pixel2[2]>=70)or(pixel2[3]>=70)or(pixel2[4]>=70)or(pixel2[5]>=70)or(pixel2[6]>=70)or(pixel2[7]>=70))or(flame1==1)):
			print "api ada dikiri"
			#tengokCode()
			#time.sleep(0.125)
			#apikanan=0
			#apikiri=1
			#putarkiriapi()
			putther3()
		if(((pixel3[0]>=70)or(pixel3[1]>=70)or(pixel3[2]>=70)or(pixel3[3]>=70)or(pixel3[4]>=70)or(pixel3[5]>=70)or(pixel3[6]>=70)or(pixel3[7]>=80))or(flame2==1)):
			#print "api ada dikanan"
			#tengokCode()
			#time.sleep(0.125)
			#apikanan=0
			#apikiri=1
			#putarkiriapi()
			putther()
		flame1=0
		flame2=0
#########################################
def bearing255():
	bear = bus.read_byte_data(address4, 1)
	return bear
####============ Pemanggilan Compass ===========###

def cmps():
	global bear255
	bear255 = bearing255()
	time.sleep(0.004)
	#print "nilai kompas ",bear255

arah=0

def arah_cmps():
	global arah
	cmps()	
	print "bear255 = ",bear255,arah
	
	if((bear255>=22) and (bear255<108)):
		arah=1
	elif((bear255>=108) and (bear255<149)):
		arah=2
	elif((bear255>=149) and (bear255<217)):
		arah=3
	else:
		arah=4
	print "arah : ",arah
	
	
detect_garis =0
arahawal=0
arahahir=0
nyasar=0
arahpul=0
def cek_nyasar():
	global arah
	global detect_garis
	global arahawal
	global arahahir
	global nyasar
	global arahpul
	if(misiapi==0):
		print "masuk cek nyasar"
		arah_cmps()
		detect_garis+=1
		print "detect garis:",detect_garis
		if(detect_garis==1):
			arahawal=arah
			if(arahawal==1):
				arahpul=3
			elif(arahawal==3):
				arahpul=1
			elif(arahawal==2):
				arahpul=4
			elif(arahawal==4):
				arahpul=2
			print "arahawal: ",arahawal
			print "arah pulang",arahpul
		elif(detect_garis>=2):
			arahahir=arah
			print "arahahir: ",arahahir
			print "hasil perbandingan = arahawal:",arahawal, " arahahir:", arahahir
			#if (arahawal==arahahir): 
			#	nyasar=1
			#	detect_garis=0
			#	print "nyasar"
			#else:
			#	nyasar=0
			#	detect_garis=0
			#	print "kagak nyasar"	
############################################################# kodingan nyasa 1=3 maju aneh emang
konnyasar1=1
garisnyasar1=0
garisnyasar2=0
garisnyasar3=0
def nyasar1():
	global garisnyasar1
	global garisnyasar2
	global garisnyasar3
	global arah
	global konnyasar1
	global garis
	global garisapi
	global nyasar

	arah_cmps()
	if(konnyasar1==1):
		garisnyasar1=arah
	elif(konnyasar1==2):
		garisnyasar2=arah
	elif(konnyasar1==3):
		garisnyasar3=arah

	if(garisnyasar1==garisnyasar3):
		nyasar=1
		#majuCode()
                #time.sleep(1)
                #garisapi=garisapi-2
                #garis=garis-2
		konnyasar1=0
		garisnyasar1=0
		garisnyasar2=0
		garisnyasar3=0
		print "tadi teh nyasar "	
	if(konnyasar1==3):
		konnyasar1=0

	konnyasar1=konnyasar1+1
	print"garisnyasar1:",garisnyasar1,"garisnyasar2:",garisnyasar2,"garisnyasar3",garisnyasar3

konnyasar2=1
garisnyasar11=0
garisnyasar22=0
garisnyasar33=0
def nyasar2():
        global garisnyasar11
        global garisnyasar22
        global garisnyasar33
        global arah
        global konnyasar2

        arah_cmps()
        if(konnyasar2==1):
                garisnyasar11=arah
        elif(konnyasar2==2):
                garisnyasar22=arah
        elif(konnyasar2==3):
                garisnyasar33=arah

        if(garisnyasar11==garisnyasar33):
                majuCode()
                time.sleep(0.75)
                konnyasar2=0
		if(garisbalik1==1):
			garisapi=garisapi+3
		elif(garisbalik2==1):
			garisapi=garisapi-3
	if(konnyasar2==3):
		konnyasar2=0

        konnyasar2=konnyasar2+1

########################## AIR ##########################30
GPIO.setup("P8_9", GPIO.OUT)
	
def air1():
	GPIO.output("P8_9",GPIO.HIGH)
	print "air======================================"
def air2():
	GPIO.output("P8_9", GPIO.LOW)
	print "matiin air"
def air3():
	air1()
	time.sleep(1.3)
	air2()
	time.sleep(0.5)

####################################putar thermal###############333


def putther2():
	global countapi
	global countapi2
	print "masuk putther2"
	thermalreg1()
	countapi=0
	#global api
	cekUV(3)
	while(((pixel1[0]<=50) and (pixel1[1]<=50)and (pixel1[2]<=50)and (pixel1[3]<=50)and (pixel1[4]<=50)and (pixel1[5]<=50)and (pixel1[6]<=50) and (pixel1[7]<=50))and (countapi<100)):
		putarkirikecilCode()
		#time.sleep(0.01)
		thermalreg1()
		countapi=countapi+1
		print"putarkiriputther2", countapi
		if(((pixel1[0]>=70) or (pixel1[1]>=70)or (pixel1[2]>=70)or (pixel1[3]>=70)or (pixel1[4]>=70)or (pixel1[5]>=70)or (pixel1[6]>=70) or (pixel1[7]>=70))and (api==1)):
			#diamCode()
			print "air phuttr2"
			tengokCode()
			air1()
			time.sleep(2)
			air2()
			time.sleep(1)
			cekUV(3)
			diamCode()
			time.sleep(0.5)
	countapi2=0
	if (((pixel1[0]<=50) and (pixel1[1]<=50)and (pixel1[2]<=50)and (pixel1[3]<=50)and (pixel1[4]<=50)and (pixel1[5]<=50)and (pixel1[6]<=50) and (pixel1[7]<=0))and (api==1)):
		while(((pixel1[0]<=50) and (pixel1[1]<=50)and (pixel1[2]<=50)and (pixel1[3]<=50)and (pixel1[4]<=50)and (pixel1[5]<=50)and (pixel1[6]<=50) and (pixel1[7]<=50))and (countapi2<50)and (api==1)):
			putarkanankecilCode()
			thermalreg1()
			countapi2=countapi2+1
			print "putarkananputther2" ,countapi2
			if(((pixel1[0]>=70) or (pixel1[1]>=70)or (pixel1[2]>=70)or (pixel1[3]>=70)or (pixel1[4]>=70)or (pixel1[5]>=70)or (pixel1[6]>=70) or (pixel1[7]>=70))and(api==1)):
                        	#diamCode()
				print "air phutter putar kiri2"
				tengokCode()
                 	      	air1()
                        	time.sleep(2)
                   	    	air2()
                       		time.sleep(1)
                        	cekUV(3)
				diamCode()
				time.sleep(0.5)
	

##########################################puther2

def putther():
    	global countapi36
	global countapi63
	global flame1
	global flame2
	print "masuk putther"
	flame1=0
	flame2=0
    	thermalreg1()
	countapi36=0
	countapi63=0
	cekUV(3)
	while(((pixel1[0]<=50) and (pixel1[1]<=50)and (pixel1[2]<=50)and (pixel1[3]<=50)and (pixel1[4]<=50)and (pixel1[5]<=50)and (pixel1[6]<=50) and (pixel1[7]<=50))and(countapi36<300)and(api==1)):
                putarkanankecilCode()
                time.sleep(0.05)
		print "putarkananputther"
                thermalreg1()
                countapi36=countapi36+1
		cekUV(3)
                print "konter 36",countapi36


def putther3():
        global countapi3
        global countapi6
	global flame1
	global flame2
	flame1=0
	flame2=0
        print "masuk putther3"
        thermalreg1()
        countapi3=0
        countapi6=0
        cekUV(3)
        while(((pixel1[0]<=50) and (pixel1[1]<=50)and (pixel1[2]<=50)and (pixel1[3]<=50)and (pixel1[4]<=50)and (pixel1[5]<=50)and (pixel1[6]<=50) and (pixel1[7]<=50))and (api==1)):
                putarkirikecilCode()
                #time.sleep(0.01)
                print "putarkiriputther3"
                thermalreg1()
                countapi3=countapi3+1
                cekUV(3)
                print countapi3

############################################################################# Cek UVTron #############################################################################
############b      ##########################################################################################################################################################

GPIO.setup("P8_7", GPIO.IN,pull_up_down=GPIO.PUD_UP)  
ap=1
def cekUV(count):
		global countingapi
		global api
		global apiruang
		global ap

		for i in range(0,count) :
			if (GPIO.input("P8_7") == 1) :
				countingapi+=1
			else :
				countingapi=0
		if(countingapi>=count):
			api=1
			apiruang=1
			garisapi=garis
			print "ada api"		
		else:
			api=0
			apiruang=0
			print "gk ada api"	
		ap=ap+1
		print ap
		return api

def therdeket():
	global cothera
	thermalreg1()
	cothera=0
	print "therdeket"
	while (((pixel1[0]<=130) and (pixel1[1]<=130) and (pixel1[2]<=130) and (pixel1[3]<=130) and (pixel1[4]<=130) and (pixel1[5]<=130) and (pixel1[6]<=130) and (pixel1[7]<=130)) and (cothera<10)):			
		majuCode()
		thermalreg1()
		#print "therdeket"
		cothera=cothera+1
		cekUV(3)
		print "cothera",cothera
		time.sleep(0.1)
	print "udah deket sama api ato countingnya abis"

def cari_api_KW_aja():
	global api
	global susurkanan
	global susurkiri
	global apiruang
	global misiapi	
	global countair
	print "masuk cari api aja"
	countapi = 0
	diamCode()
	time.sleep(0.125)
	cekUV(3)
	if (api==0):
		print "ga kedetect api, coba cari pake goyang inul"
		cekUV(3)
		while ((countapi<10) and (api==0)):
			#print "goyang inul"
			cekUV(3)
			print "ledlilin()"
			print "tengokCode()"
			time.sleep(0.05)
			countapi+=1
		#cekUV(3)
		#cmps_spesial()
		if (api==1):
			print "detect api setelah cari api goyang-goyang"
			#ledlilin()
			diamCode()
			time.sleep(0.125)
			majuCode()
			time.sleep(0.75)
			diamCode()
			time.sleep(4)
			putther()
			
			#air1()
			#time.sleep(2)
			#air2()
			#time.sleep(0.5)
			#air3()
			diamCode()
			time.sleep(0.125)
			cekUV(3)
			countapi=0
			while((countapi<25)and(api==0)):
				cekUV(3)
				#ledlilin()
				print "tengokCode()"
				time.sleep(0.05)
				countapi+=1
			#ledlilin()
			if (api==0):
				#cari_api_KW_kembali()
				if (api==0):
					print "udah matiin api"
					misiapi=1
					apiruang=1
					#perataan()
					if (countgaris>2):
						susurkanan=1
						susurkiri=0
					elif (countgaris<=2):
						susurkanan=0
						susurkiri=1
					#munduraja()
		elif (api==0):
			mundurCode()
			time.sleep(0.5)
			putarkirisedangCode()
			time.sleep(1)#ledlilin()
	elif (api==1):
		garisapi=garis+1
		print "udah detect api, jadi gk usah goyang-goyang"
		#cmps_spesial()
		print "ledlilin()"
		diamCode()	
		time.sleep(0.125)
		majuCode()
		time.sleep(1)
		diamCode()
		time.sleep(0.125)
		putther()
		therdeket()
		putther3()
		tengokCode()
		print "air kw"
		air1()
		time.sleep(2)
		air2()
		time.sleep(0.125)
		diamCode()
		time.sleep(0.125)
		cekUV(3)
		if(api==1):
			countair=0
			while((api==1) and (countair<5)):
				putther()
				tengokCode()
				print "masuk while airkw2"
				air1()
				time.sleep(2)
				air2()
				time.sleep(0.125)
				cekUV(3)
				countair=countair+1
		if(api==1):
                        countair=0
                        while((api==1) and (countair<5)):
				mundurCode()
				time.sleep(0.3)
                                putther()
                                tengokCode()
                                print "masuk while airkw2(2)"
                                air1()
                                time.sleep(2)
                                air2()
                                time.sleep(0.125)
                                cekUV(3)
                                countair=countair+1

		if(api==0):
			diamCode()
			time.sleep(2)
			misiapi==1
			jalanmisi==1
			print "jalanmisi=1"
			print "misiapi=1 hasil cari api kw"

	
############################################################################ PROXIMITY ################################################################################	
#######################################################################################################################################################################
 
state1=0
state2=0

garis		= 0
ruang		= 0
lorong		= 0
apiruang	= 0
misiapi		= 0
countingapi	= 0
susur		= 0
api		= 0
kondisicek	= 0
cekcek		= 0
countgaris	= 0
asal 		= 0
jalanmisi	= 0
countgarismisi	= 0
skipperataan	= 0
garpul=0
counttt=0
####========= Algoritma ========###
garisruang=0
def proxi():
	global misiapi
	global mulai
	global slesemisi
	global asal
	global garis
	global garisapi
	global garisruang
	global counttt
	global garpul

	ADC.read("P9_40")
	ADC.read("P9_38")
	if(ADC.read("P9_40")<=0.95):#0.95
		state1=1
	else:
		state1=0
		
	if(ADC.read("P9_38")<=0.97):
		state2=1
	else:
		state2=0
	#print state1,state2	

	if (misiapi==0):
		if (state1==1):
			#print "garis"
			#print state1,state2
			#print ADC.read("P9_35")
			garis+=1
			print garis
			garisapi=garis+1
			misiproxi()
			garisruang=garis
		if ((state1==1) and (state2==1)):
			print "home"
			#print state1,state2
			
	if(misiapi==1):
		if(state1==1):
			if(garpul==0):
				diamCode()
				time.sleep(0.4)
				garisapi=garisapi-1
				majuCode()
				time.sleep(0.3)
				ultra_kade(0.06)
				while((b5<28) and (counttt<300)):
					kepitingkiriCode()
					ultra_kade(0.06)
					counttt+=1
					print counttt
				garpul=1
			elif(garpul==1):
				print "garispulang"
				if(garisbalik1==1):
					#print "garispulang"
					garisapi=garisapi-1
					misiproxi()
				elif(garisbalik2==1):
					garisapi=garisapi+1
					misiproxi()
			elif((state1==1)and(state2==1)):
				print "home balik"
				done=1
		elif(state1==1)and(state2==1):
			print "los tapi dapat bunderan putih jadi misi selesai"
			done=1
garisruang=0
tambahgar=0	
counm=0	
coun12=0
counci=0
nyasa=0
def misiproxi():
	global garis
	global ruang
	global lorong
	global startruang
	global apiruang
	global misiapi
	global susur
	global countingapi
	global api
	global kondisicek
	global cekcek
	global start
	global stop	
	global mulai
	global asal
	global countgaris
	global nyasar
	global jalanmisi
	global countgarismisi
	global slesemisi
	global depanhome
	global skipperataan
	global loopmuterkanan
	global loopmuterkiri
	global susurkanan
	global susurkiri
	global putarkanansekali
	global garisapi
	global done
	global tambahgar
	global garisbalik1
	global garisbalik2
	global counm
	global counn
	global coun12
	global counci
	#print "countgaris:",countgaris
	arah_cmps()
	#cmps_misi()
	cek_nyasar()
	#ledlilin()
	buzzer()
	nyasar1()
	diamCode()
	time.sleep(0.4)
	print "garisbalik1:",garisbalik1,"garisbalik2",garisbalik2
	if(apiruang==1):
			print "di ruangan ada api"
			if(misiapi==1):
				print "api berhasil dipadamkan"
				if(api==0):
					print "keluar dari ruang yang ada api"
					if(garisapi==(garis+1)):
						majuCode()
						time.sleep(0.2)
						apiruang=0
			elif(misiapi==0):
				print "mundur karna api belom padam"
				mundurCode()
				time.sleep(0.4)
				#coun12=0
				putarkanansedangCode()
				time.sleep(1)
				ultra_deka(0.09)
				ultra_deki(0.09)
				while((coun12<=50)and((b3>17)or(b4>17))):
					putarkanansedangCode()
					ultra_deka(0.09)
					ultra_deki(0.09)
				#time.sleep(1.50)#1.18
					coun12+=1
					print coun12
				ultra_deka(0.09)
                                ultra_deki(0.09)
                                while((counci<=19000)and((b3>17) and (b4>17))):
                                	majuCode()
                                        ultra_deka(0.09)
                                        ultra_deki(0.09)
					counci+=1
				#majuCode()
				#time.sleep(0.5)
				garisapi-=1
				garis-=1
				#cari_api_KW_lagi()
			
	elif(apiruang==0):
		print "CEK INI PENTING","garis api:",garisapi,"garis ruang:",garisruang,"arahawal",arah,"garis:",garis
		print "ada kemungkinan dalam ruang ada api"
		if(misiapi==1):#jalan pulang
			if((garisapi==garisruang)or(garisapi==garisruang+2)):
				print"keluar ruang api","arah:",arah,"arahpulang",arahpulang
				majuCode()
				time.sleep(0.3)
			elif(garisbalik1==1):
				if((garisapi==1)and(arah==arahpul)):
					print"tempatbalik1"
					majuCode()
					time.sleep(1)#0.8
					done=1
				elif((garisapi==1)and(arah!=arahpul)):
					garisapi+=1
                                	print "mundur garis balik1"
                                	mundurCode()
                                	time.sleep(0.65)
                                	if(susurkiri==1):
                                        	putarkanansedangCode()
                                        	time.sleep(0.9)
                                        	majuCode()
                                        	time.sleep(0.9)
                                	elif(susurkanan==1):
                                        	putarkirisedangCode()
                                        	time.sleep(1.18)
                                        	majuCode()
                                        	time.sleep(0.9)
				elif((garisapi>=1)and(arah!=arahpul)):
					print "mundur garis balik1 1"
					mundurCode()
					time.sleep(0.65)
			#		if(susurkiri==1):
					putarkanansedangCode()
					time.sleep(0.9)
					majuCode()
					time.sleep(0.9)
			#		elif(susurkanan==1):
					#putarkirisedangCode()
					#time.sleep(1.18)
					#majuCode()
					#time.sleep(0.9)


			elif(garisbalik2==1):
				print"arah:",arah,"arah pulang",arahpul
				if((garisapi==5)and(arah==arahpul)):
					majuCode()
					time.sleep(0.8)
					done=1
					print"balik2 kondisi1"
				elif((garisapi==5)and(arah!=arahpul)):
					garisapi-=1
					print "mundur garis balik2"
					mundurCode()
					time.sleep(0.65)
					if(susurkiri==1):
                                		putarkanansedangCode()
						time.sleep(0.9)
						majuCode()
						time.sleep(0.9)
					elif(susurkanan==1):
						putarkirisedangCode()
						time.sleep(1.18)
						majuCode()
						time.sleep(0.9)
				elif((garisapi<=7)and(arah!=arahpul)):
					mundurCode()
                                        time.sleep(0.65)
					print "kondisi3 balik2"
                                        if(susurkiri==1):
                                                putarkanansedangCode()
                                                time.sleep(0.9)
                                                majuCode()
                                                time.sleep(0.9)
                                        elif(susurkanan==1):
                                                putarkirisedangCode()
                                                time.sleep(1.18)
                                                majuCode()
                                                time.sleep(0.9)

		elif(misiapi==0):
			if(garis==1):
				majuCode()
				time.sleep(0.3)
			elif(garis>=2):
				cari_api()
				if((api==0)and(nyasar==0)):
					mundurCode()
					time.sleep(0.45)
					if(susurkanan==1):
						putarkirisedangCode()
						time.sleep(1)
						counm=0
						ultra_deka(0.09)
						ultra_deki(0.09)
						while((counm<=80)and((b3>17) or (b4>17))):
							majuCode()
							ultra_deka(0.09)
							ultra_deki(0.09)
						#time.sleep(0.9)
							#print "counm", counm
							counm+=1
							print counm
							print"majuuuuuuuuuuuuuuuu"
					else:
						counn=0
						putarkanansedangCode()
						time.sleep(1.02)
						ultra_deka(0.09)
						ultra_deki(0.09)
						while((counn<=80)and((b3>17)or(b4>17))):
							majuCode()
							ultra_deka(0.09)
							ultra_deki(0.09)
							counn+=1
							print counn
				
				elif(nyasar==1):
                        		#majuCode()
                        		#time.sleep(1)
					#print "masuk misi proxi nyasar yeh a"
					nyasar=0
                        		garisapi=garisapi-2
                        		garis=garis-2
					majuCode()
					time.sleep(1)
                        		print"ah maju teuuuuu"
					print "GARIS API",garisapi,"GARIS:",garis
					print "maju karna ada api diruangan atau nyasar"
			
					
######################################################################### ~~~~ ULTRASONIC ~~~~ ########################################################################

def ultra_kiri(delay):
        global a1
        global b1
        coun1 = 0
        count1= 0
	
        m1 =0.230
        b11 =0.692
        GPIO.setup("P8_14", GPIO.OUT) #trigger
        GPIO.output("P8_14", GPIO.LOW)
        #GPIO.setup("P8_14", GPIO.IN) #echo
        GPIO.output("P8_14", GPIO.HIGH)
        time.sleep(0.000002)
        GPIO.output("P8_14", GPIO.LOW)
        GPIO.setup("P8_14",GPIO.IN)
        while (GPIO.input("P8_14")==0) and (coun1<=3000):
                coun1=coun1+1
        #start = time.time()
        while GPIO.input("P8_14")==1:
                count1=count1+1
        a1=((m1*count1)+b11)
        b1= int(a1)
		
        print "||kiri", b1
	return b1 
	

def ultra_kide(delay):
        global a2
        global b2
        count2 = 0
        counter2= 0
        m2 =0.33
        b22 =0.16
	
        GPIO.setup("P9_15", GPIO.OUT) #trigger
        GPIO.output("P9_15", GPIO.LOW)
        GPIO.setup("P9_12", GPIO.IN) #echo
        GPIO.output("P9_15", GPIO.HIGH)
        time.sleep(0.000002)
        GPIO.output("P9_15", GPIO.LOW)
        #GPIO.input("P9_23")
        while (GPIO.input("P9_12")==0) and (count2<=3000):
                count2=count2+1
        #start = time.time()
        while GPIO.input("P9_12")==1:
                counter2=counter2+1
        a2=((m2*counter2)+b22)
        b2= int(a2)
	
	print " ||kide", b2
	return b2
	#print b2
	

def ultra_deki(delay):
        global a3
        global b3
        count3 = 0
        counter3= 0
	
        m3 =0.34
        b33 =0.34
        GPIO.setup("P9_30", GPIO.OUT) #trigger
        GPIO.output("P9_30", GPIO.LOW)
        GPIO.setup("P9_23", GPIO.IN) #echo
        GPIO.output("P9_30", GPIO.HIGH)
        time.sleep(0.000002)
        GPIO.output("P9_30", GPIO.LOW)
        #GPIO.input("P9_23")
        while (GPIO.input("P9_23")==0) and (count3<=3000):
                count3=count3+1
        #start = time.time()
        while GPIO.input("P9_23")==1:
                counter3=counter3+1
        a3=((m3*counter3)+b33)
        b3= int(a3)
	
        print " ||deki", b3
	return b3 
	#print b3
	#time.sleep(delay)
def ultra_deka(delay):
        global a4
        global b4
        count4 = 0
        counter4= 0

        m4 =0.30
        b44 =0.46

        GPIO.setup("P8_15", GPIO.OUT) #trigger
        GPIO.output("P8_15", GPIO.LOW)
        GPIO.setup("P8_17", GPIO.IN) #echo
        GPIO.output("P8_15", GPIO.HIGH)
        time.sleep(0.000002)
        GPIO.output("P8_15", GPIO.LOW)
        #GPIO.input("P9_23")
        while (GPIO.input("P8_17")==0) and (count4<=3000):
                count4=count4+1
        #start = time.time()
        while GPIO.input("P8_17")==1:
                counter4=counter4+1
        a4=((m4*counter4)+b44)
        b4= int(a4)
					
        print " ||deka", b4
	#print b4 
	return b4
	#time.sleep (delay)
def ultra_kade(delay):
        global a5
        global b5
        count5 = 0
        counter5= 0
        m5 =0.294
        b55 =0.588

        GPIO.setup("P8_10", GPIO.OUT) #trigger
        GPIO.output("P8_10", GPIO.LOW)
        GPIO.setup("P8_8", GPIO.IN) #echo
        GPIO.output("P8_10", GPIO.HIGH)
        time.sleep(0.000002)
        GPIO.output("P8_10", GPIO.LOW)
        #GPIO.input("P9_23")
        while (GPIO.input("P8_8")==0) and (count5<=3000):
                count5=count5+1
        #start = time.time()
        while GPIO.input("P8_8")==1:
                counter5=counter5+1
        a5=((m5*counter5)+b55)
        b5= int(a5)
	
	print " ||kade", b5
	return b5 
	#time.sleep(0.01)
	#print b5
def ultra_kanan(delay):
        global a6
        global b6
	global has16
        count6 = 0
        counter6= 0
        m6 =0.357
        b66 =1.78
        GPIO.setup("P8_18", GPIO.OUT) #trigger
        GPIO.output("P8_18", GPIO.LOW)
        GPIO.output("P8_18", GPIO.HIGH)
        time.sleep(0.000002)
        GPIO.output("P8_18", GPIO.LOW)
        #GPIO.input("P9_23")
	GPIO.setup("P8_18", GPIO.IN) #echo
        while (GPIO.input("P8_18")==0) and (count6<=3000):
                count6=count6+1
        #start = time.time()
        while GPIO.input("P8_18")==1:
                counter6=counter6+1
	a6=((m6*counter6)+b66)
	b6= int(a6)
	
        print " ||kanan",b6
	return b6
 
#has7=0	
def ultra_beki(delay):
        global a7
        global b7
        coun7 = 0
        count7= 0
	global has7
        m7 =0.285
        b77 =0.571
        GPIO.setup("P8_12", GPIO.OUT) #trigger
        GPIO.output("P8_12", GPIO.LOW)
	#time.sleep(0.000005)
        #GPIO.setup("P8_14", GPIO.IN) #echo
        GPIO.output("P8_12", GPIO.HIGH)
        time.sleep(0.000002)
        GPIO.output("P8_12", GPIO.LOW)
        GPIO.setup("P8_12",GPIO.IN)
        while (GPIO.input("P8_12")==0) and (coun7<=3000):
                coun7=coun7+1
        #start = time.time()
        while GPIO.input("P8_12")==1:
                count7=count7+1
        a7=((m7*count7)+b77)
        b7= int(a7)
	#for i in range(0, 4):
	#	if has7 > b7:
	#		has7=has7
	#	else:
	#		has7=b7 	
        print "||beki", b7
	return b7

def ultra_beka(delay):
        global a8
        global b8
        coun8 = 0
        count8= 0
        global has8
        m8 =0.281
        b88 =0.140
        GPIO.setup("P9_25", GPIO.OUT) #trigger
        GPIO.output("P9_25", GPIO.LOW)
        #time.sleep(0.000005)
        #GPIO.setup("P8_14", GPIO.IN) #echo
        GPIO.output("P9_25", GPIO.HIGH)
        time.sleep(0.000002)
        GPIO.output("P9_25", GPIO.LOW)
        GPIO.setup("P9_25",GPIO.IN)
        while (GPIO.input("P9_25")==0) and (coun8<=3000):
                coun8=coun8+1
        #start = time.time()
        while GPIO.input("P9_25")==1:
                count8=count8+1
        a8=((m8*count8)+b88)
        b8= int(a8)
        #for i in range(0, 4):
        #       if has7 > b7:
        #               has7=has7
        #       else:
        #               has7=b7
        print "||beka", count8
        return b8 

def maincoba():	
	while True:

#		berdiri(0,4,2.7)
		#Susur_Kiri()
#		ultra_kide(0.06)
#		ultra_deki(0.09)
#		ultra_deka(0.09)
#		ultra_kade(0.03)
#		ultra_kanan(0.03)
#		ultra_kiri(0.03)
#		ultra_beki(0.03)
		ultra_beka(0.03)
		#belokkananCode()
		#susur_kanan_spesial()
#		print "depan:",ADC.read("P9_40")
#		print "belki:",ADC.read("P9_36")
		#print state2
		#infrared1()
		#proxi()
		#berdiri(0,4,3)
		#cekUV(3)
#		thermalreg1()
		#nilaither1()
		#time.sleep(0.5)
		#putther()
		#air3()
		#arah_cmps()
		#ledmic()
		#buzzer()
		#limitswitch()
		#ledlilin2()
		#ledlilin()
		#flamesen1()
		#flamesen2()
		#aadc()
#		sound_act(3)
		#print GPIO.input("P9_18")
		time.sleep(0.01)#0.01

#berdiri(0,1,6.5)

#maincoba()
#while True:


multithread()
#multitask()
#main_coba()

######################### bang can 1 ############################
#try:
#	if __name__ == '__main__':
#		threadLock=threading.Lock()
#		threads=[]
#		thread1=myThread(1, "Thread-1",1)
#		thread2=myThread2(1, "Thread-2",1)
#		thread1.start()
#		thread2.start()
#		threads.append(thread1)
#		threads.append(thread2)
#		for t in threads:
#			t.join()
#except(KeyboardInterrupt, SystemExit):
#	print 'Shutting down...........'
###################################################
#if __name__== "__main__":
#	Susur_Kanan()
#	gerak()
####################3333333 bang can 2#######################
#signal.signal(signal.SIGINT, multitasking.killall)
#@multitasking.task
#def hello():
#	#try:
#	#while True:
#	gerak()
	#except (KeyboardInterrupt, SystemExit):
         #              pass

#def holle():
	#try:
#	while True:
#	Susur_Kanan()
	#except (KeyboardInterrupt, SystemExit):
         #             pass

#@multitasking.task

#if __name__ == "__main__":
#	try:
#		while True:
			#hello()
			#holle()
#			gerak()
#			Susur_Kanan()
			#putarkirisedangCode()
#	except (KeyboardInterrupt, SystemExit):
 #       	print "shutting down"

