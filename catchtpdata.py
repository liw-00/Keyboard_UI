# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:13:37 2017

@author: Celfras--Levi
"""

import threading
import time
import serial

class Readtpdata:
    
    def __init__(self,Port="COM3"):
        self.TP_serial=None
        self.TP_port=Port
        self.TP_alive=False
        self.TP_wait=None
        self.ID=None
    
    def waiting(self):
        if not self.TP_wait is None:
            self.TP_wait.wait()
            
    def SetStopEvent(self):
        if not self.TP_wait is None:
            self.TP_wait.set()
        self.TP_alive=False
        self.stop()
        
    def start(self):
        
        self.TP_serial=serial.Serial()
        self.TP_serial.port=self.TP_port
        self.TP_serial.baudrate=921600
        self.TP_serial.timeout=1
        self.TP_serial.open()
        
        if self.TP_serial.isOpen():
            self.TP_wait=threading.Event()
            self.TP_alive=True
            self.thread_read=None
            self.thread_read=threading.Thread(target=self.Reader)
            self.thread_read.setDaemon(1)
            self.thread_read.start()
            return True
        else:
            return False
                    
    def Reader(self):
        while self.TP_alive:
            time.sleep(0.05)
            data=''
            temp=''
            data=data.encode('utf-8')
            n=self.TP_serial.inWaiting()                             

            data=self.TP_serial.readline()    
            n=self.TP_serial.inWaiting()
            if len(data)>0 and n==0:
                try:
                    temp=data
                    '''temp=data.decode('utf-8')'''
                    print('串口数据:',temp)
                except:
                    print('无法读取串口数据')
            self.TP_data=temp     
            self.TP_wait.set()
            self.TP_alive=False
            
    def stop(self):
        self.TP_alive=False
        self.thread_read.join()
        if self.TP_serial.isOpen():
            self.TP_serial.close()
            
def Catchdata():
    temp=''
    tp=Readtpdata()
    #tp.sendport = '**1*80*'
    try:
        if tp.start():
            tp.waiting()
            temp=tp.TP_data
            tp.stop()

        else:
            pass
    except Exception as ex:
        #print('出现错误',str(ex))
        print(' waiting for input ')
        tp.TP_serial.close()
        
    if tp.TP_alive:
        tp.stop()
    
    del tp
    return temp


def inputdatatokey(tempdata):
  
    linekey_1=['Esc','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','Home','End','Insert','Delete']
    linekey_2=['~','1','2','3','4','5','6','7','8','9','0','-','+','Backspace']
    linekey_3=['Tab','q','w','e','r','t','y','u','i','o','p','{','}','|']
    linekey_4=['Capslock','a','s','d','f','g','h','j','k','l',':','"','Enter']
    linekey_5=['Shift','z','x','c','v','b','n','m','<','>','?','Right Shift']
    linekey_6=['Fn','Ctrl','Windows','Alt','Space','Right Alt','PrtScn','Right Ctrl','Pgup','↑','PgDn']
    linekey_7=['←','↓','→']

    linecode_1=['1B','70','71','72','73','74','75','76','77','78','79','7A','7B','24','23','2D','2E']
    linecode_2=['81','31','32','33','34','35','36','37','38','39','30','BD','BB','8']
    linecode_3=['9','51','57','45','52','54','59','55','49','4F','50','DB','DD','DC']
    linecode_4=['14','41','53','44','46','47','48','4A','4B','4C','BA','DE','6C']
    linecode_5=['10','5A','58','43','56','42','4E','4D','BC','BE','BF','A0']
    linecode_6=['B8','11','5B','12','20','A2','2A','A1','21','26','22']
    linecode_7=['25','28','27']
  
    linedir_1=dict(zip(linekey_1,linecode_1))
    linedir_2=dict(zip(linekey_2,linecode_2))
    linedir_3=dict(zip(linekey_3,linecode_3))
    linedir_4=dict(zip(linekey_4,linecode_4))    
    linedir_5=dict(zip(linekey_5,linecode_5))
    linedir_6=dict(zip(linekey_6,linecode_6))
    linedir_7=dict(zip(linekey_7,linecode_7))

    linecode=[]
    linecode.append(linecode_1)
    linecode.append(linecode_2)
    linecode.append(linecode_3)
    linecode.append(linecode_4)
    linecode.append(linecode_5)
    linecode.append(linecode_6)
    linecode.append(linecode_7)
    
    #linekeydir=dict(dict(dict(dict(dict(dict(linedir_1,**linedir_2),**linedir_3),**linedir_4),**linedir_5),**linedir_6),**linedir_7)
    
    def findkey_coordinate(code,linecode):
        coordinate=[]
        for data in code:
            row=0
            for keyline in linecode:
                try:
                    col=keyline.index(data)
                    coordinate.append([row,col])
                except:
                    row+=1
        return coordinate
        
    
    def separateinput(tempdata):
        input_coordinate=[]
        coordinate_state=[]
        try:
            input_data=tempdata.decode()
            input_list=(input_data.replace('\r\n','')).split(',')
            inputdata_byte=len(input_list)
            '''print(inputdata_byte)'''
            keydata=[]
                       
            keystate=[]
            
            if inputdata_byte > 3 and ((inputdata_byte - 1)%3) == 0 :
                for d in range(inputdata_byte//3):
                     
                    if input_list[2+3*d] !='0' :
                        keydata.append(input_list[2+3*d])
                        if input_list[3+3*d] !='0' :
                            keystate.append([1])
                        else:
                            keystate.append([0])
                    else:
                        pass
                    
                print('按键值：',keydata)
                #print('输出值：',linekeydir[keydata])
                #print('坐标值：',findkey_coordinate(keydata,linecode))
                input_coordinate=findkey_coordinate(keydata,linecode)
                
                #print('按键状态',keystate)
                for i in range(len(input_coordinate)):
                    coordinate_state.append(input_coordinate[i]+keystate[i])
                #print('坐标值和坐标状态：',coordinate_state)
        except Exception:
            pass
        return coordinate_state
      
    return separateinput(tempdata)

