# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:36:13 2017
@author: Celfras--Levi
"""

from PyQt5.QtWidgets import QMainWindow,QWidget,QGridLayout,QGroupBox,QApplication,QPushButton,QHBoxLayout,QVBoxLayout,QTextEdit,QLineEdit,QLabel,QComboBox
from PyQt5.QtGui import QIcon,QPalette,QFont,QTextCursor
from PyQt5.QtCore import Qt,QObject,pyqtSignal,QThread,pyqtSlot,QPropertyAnimation
import sys
import time

from sys import path
path.append('.')
from catchtpdata import Readtpdata,Catchdata,inputdatatokey

global textnarray
textnarray=[]


class EmittingStream(QObject):
    textWritten = pyqtSignal(str)
    def flush(self):
        pass         

    def write(self,text):                                                  
        self.textWritten.emit(str(text))

class KeyboardUI(QMainWindow):
        
    def __init__(self):
        super().__init__()
        self.keyboard()
        QThread.currentThread().setObjectName('main')
        self.__work_done=None
        self.__threads=None
        self.animation=None
        self.animation = None
    
    def __del__(self):
        sys.__stdout__ = sys.stdout                                  # 初始化标准输出
        sys.__stderr__ = sys.stderr                                  # 初始化标准输出'''

    def closeEvent(self,event):
        if self.animation is None:
            self.animation=QPropertyAnimation(self,"windowOpacity")
            self.animation.setDuration(300)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.close)
            self.animation.start()
            event.ignore()


    def keyboard(self):        
        self.setWindowTitle('KeyBoard Test Tool Beta1.0')
        
        self.savedStdout = sys.stdout
        self.savedStderr = sys.stderr
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)  # 重新定义系统标准输出
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)  # 重新定义系统标准错误'''
        
        mainLayout=QGridLayout()
        serailLayout=QGridLayout()

        line1Layout=QHBoxLayout()
        line2Layout=QHBoxLayout()
        line3Layout=QHBoxLayout()
        line4Layout=QHBoxLayout()
        line5Layout=QHBoxLayout()
        line6Layout=QHBoxLayout()
        line7Layout=QHBoxLayout()

        self.Serial_chose_Widget=QGroupBox('')
        self.TxtWidget=QTextEdit()
        self.Txtline=QLineEdit()
        self.Txtline.setFont(QFont("Roman times",13))
        
        self.runbutton=QPushButton('RUN')
        
        self.serial_name_label=QLabel(' 串口')
        self.serial_name_widget=QComboBox()

        self.serial_name_widget.addItem("COM1")
        self.serial_name_widget.addItem("COM2")
        self.serial_name_widget.addItem("COM3")
        self.serial_name_widget.addItem("COM4")
        self.serial_name_widget.addItem("COM5")
        self.serial_name_widget.addItem("COM6")
        self.serial_name_widget.addItem("COM7")
        self.serial_name_widget.addItem("COM8")
        self.serial_name_widget.addItem("COM9")
        self.serial_name_widget.addItem("COM10")

        self.serail_baudrate_label=QLabel("波特率")
        self.serial_lineedit = QLineEdit()
        
        
        self.Serial_chose_Widget.setLayout(serailLayout)
        serailLayout.addWidget(self.serial_name_label,0,0,1,2)
        serailLayout.addWidget(self.serial_name_widget, 0,2,1,3)
        serailLayout.addWidget(self.serail_baudrate_label,1,0,1,2)
        serailLayout.addWidget(self.serial_lineedit,1,2,1,3)


        self.line1widget=QWidget()
        self.line1widget.setLayout(line1Layout)
        self.line2widget=QWidget()
        self.line2widget.setLayout(line2Layout)
        self.line3widget=QWidget()
        self.line3widget.setLayout(line3Layout)
        self.line4widget=QWidget()
        self.line4widget.setLayout(line4Layout)
        self.line5widget=QWidget()
        self.line5widget.setLayout(line5Layout)
        self.line6widget=QWidget()
        self.line6widget.setLayout(line6Layout)
        self.line7widget=QWidget()
        self.line7widget.setLayout(line7Layout)
        
        MainWindow=QWidget()
        MainWindow.setLayout(mainLayout)
        self.setCentralWidget(MainWindow)

        mainLayout.addWidget(self.Serial_chose_Widget,0,0,1,1)
        mainLayout.addWidget(self.TxtWidget,0,1,1,18)
        mainLayout.addWidget(self.runbutton,1,0,1,1)
        mainLayout.addWidget(self.Txtline,1,1,1,18)
        key_line1=['Esc','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','Home','End','Insert','Delete']
        key_line2=['~\n·\n','!\n1\n','@\n2\n','#\n3\n','$\n4\n','%\n5\n','^\n6\n','&&\n7\n','*\n8\n','(\n9\n',')\n0\n','-\n-\n','+\n=\n','\nBackspace\n']
        key_line3=['\nTab\n','\nQ\n','\nW\n','\nE\n','\nR\n','\nT\n','\nY\n','\nU\n','\nI\n','\nO\n','\nP\n','{\n[\n','}\n]\n','|\n\\\n']
        key_line4=['\nCaps Lock\n','\nA\n','\nS\n','\nD\n','\nF\n','\nG\n','\nH\n','\nJ\n','\nK\n','\nL\n',':\n;\n','"\n\'\n','\nEnter\n']
        key_line5=['\nShift\n','\nZ\n','\nX\n','\nC\n','\nV\n','\nB\n','\nN\n','\nM\n','<\n,\n','>\n.\n','?\n/\n','\nShift\n']
        key_line6=['\nFn\n','\nCtrl\n','\n▆▇\n▇▇','\nAlt\n','\n------------------------------------------------------------------\n','\nAlt\n','\nPrtScn\n','\nCtrl\n','\nPgUp\n','\n↑\n','\nPgDn\n']
        key_line7=['←','↓','→']
        
        key_line=[]
        key_line.append(key_line1)
        key_line.append(key_line2)
        key_line.append(key_line3)
        key_line.append(key_line4)
        key_line.append(key_line5)
        key_line.append(key_line6)
        key_line.append(key_line7)
        
        self.button=locals()
        
        positions1= [ j for j in range(17)]
        for position,key in zip(positions1,key_line1):
            self.button['button1_%s'%position]=QPushButton(key)
            self.button['button1_%s'%position].setFont(QFont("Roman times",8,QFont.Bold))
            #self.button['button1_%s'%position].setCheckable(True)
            #self.button['button1_%s'%position].setAutoExclusive(True)
            line1Layout.addWidget(self.button['button1_%s'%position],position)
        mainLayout.addWidget(self.line1widget,2,0,1,19)
              
        positions2= [ j for j in range(14)]
        for position,key in zip(positions2,key_line2):
            self.button['button2_%s'%position]=QPushButton(key)
            self.button['button2_%s'%position].setFont(QFont("Roman times",9,QFont.Bold))
            line2Layout.addWidget(self.button['button2_%s'%position],position)
            line2Layout.setSpacing(8)
        mainLayout.addWidget(self.line2widget,3,0,1,19) 
        
        positions3= [ j for j in range(14)]
        for position,key in zip(positions3,key_line3):
            self.button['button3_%s'%position]=QPushButton(key)
            self.button['button3_%s'%position].setFont(QFont("Roman times",9,QFont.Bold))
            line3Layout.addWidget(self.button['button3_%s'%position],position)
            line3Layout.setSpacing(10)
        mainLayout.addWidget(self.line3widget,4,0,1,19)

        positions4= [ j for j in range(13)]
        for position,key in zip(positions4,key_line4):
            self.button['button4_%s'%position]=QPushButton(key)
            self.button['button4_%s'%position].setFont(QFont("Roman times",9,QFont.Bold))
            line4Layout.addWidget(self.button['button4_%s'%position],position)
            line4Layout.setSpacing(13)
        mainLayout.addWidget(self.line4widget,5,0,1,19)

        positions5= [ j for j in range(12)]
        for position,key in zip(positions5,key_line5):
            self.button['button5_%s'%position]=QPushButton(key)
            self.button['button5_%s'%position].setFont(QFont("Roman times",9,QFont.Bold))
            line5Layout.addWidget(self.button['button5_%s'%position],position)
            line5Layout.setSpacing(15)
        mainLayout.addWidget(self.line5widget,6,0,1,19)


        positions6= [ j for j in range(11)]
        for position,key in zip(positions6,key_line6):
            self.button['button6_%s'%position]=QPushButton(key)
            self.button['button6_%s'%position].setFont(QFont("Roman times",9,QFont.Bold))
            if key=='\n------------------------------------------------------------------\n':
                self.button['button6_%s'%position].setStyleSheet('''
                QPushButton{
                color: rgb(211,211,211) ;
                }
                ''')

            line6Layout.addWidget(self.button['button6_%s'%position],position)
            line6Layout.setSpacing(12)
        mainLayout.addWidget(self.line6widget,7,0,1,19)

        positions7= [ j for j in range(3)]
        for position,key in zip(positions7,key_line7):
            self.button['button7_%s'%position]=QPushButton(key)
            self.button['button7_%s'%position].setFont(QFont("Roman times",9,QFont.Bold))

            line7Layout.addWidget(self.button['button7_%s'%position],position+8)
            line7Layout.setSpacing(12)
        mainLayout.addWidget(self.line7widget,8,14,1,5)
        
        self.move(300,150)
        self.show()
        
    def normalOutputWritten(self, text):
        cursor = self.TxtWidget.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.TxtWidget.setTextCursor(cursor)
        self.TxtWidget.ensureCursorVisible()


def changebutton(data):
    
    linekey_1=['Esc','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','Home','End','Insert','Delete']
    linekey_2=['~','1','2','3','4','5','6','7','8','9','0','-','+','Backspace']
    linekey_3=['Tab','Q','W','E','R','T','Y','U','I','O','P','{','}','|']
    linekey_4=['Capslock','A','S','D','F','G','H','J','K','L',':','"','Enter']
    linekey_5=['Shift','Z','X','C','V','B','N','M','<','>','?','Right Shift']
    linekey_6=['Fn','Ctrl','Windows','Alt','Space','Right Alt','PrtScn','Right Ctrl','Pgup','↑','PgDn']
    linekey_7=['←','↓','→']
    
    linekey=[]
    linekey.append(linekey_1)
    linekey.append(linekey_2)
    linekey.append(linekey_3)
    linekey.append(linekey_4)
    linekey.append(linekey_5)
    linekey.append(linekey_6)
    linekey.append(linekey_7)

    if len(data)!=0:
        for d in data:
            row,col,state=d[0],d[1],d[2]
            #print('进入判断',d)
            if state==1:
                #print('button'+str(row+1)+'_'+str(col))
                ex.button['button'+str(row+1)+'_'+str(col)].setStyleSheet('''
                    QPushButton{
                    background-color: rgb(255,255,102);
                    }
                    ''')
                text=str(linekey[row][col])
                textnarray.append(text)
                
            else:
                ex.button['button'+str(row+1)+'_'+str(col)].setStyleSheet('''
                    QPushButton{
                    background-color: rgb(211,211,211) ;
                    }
                    ''')
            
                               
class Changebuttoncolor(QThread,QApplication):
    _signal=pyqtSignal(list)
    datalist=[]
    def __init__(self):
        super().__init__()
        self.working=True
        
    def changestart(self,printdata):
        self.start()
        #print(printdata)
        
    def run(self):
        temp=Catchdata()
        self.datalist=inputdatatokey(temp)
        if len(self.datalist)!=0:           
            self._signal.emit(self.datalist)
            #print('数据已发送',self.datalist)
            '''self._signal.connect(changebutton)'''
            time.sleep(0.02)
        else:
            pass

          
if __name__=='__main__':
    
    app=0
    app=QApplication(sys.argv)     
    app.setStyleSheet(''' 
        QPushButton{
        background-color: rgb(211,211,211) ;
        }
        ''')
    ex=KeyboardUI()
    ex.runbutton.setStyleSheet('''
        QPushButton{
        background-color: rgb(51,153,255) ;
        height:18px;
        border-style: inset;
        border-radius: 5px;
        border-color: beige;
        }
        QPushButton:pressed{
        background-color: rgb(220, 220, 0);
        border-style: inset;}'''
        )          
    ex.show()

    while 1:
        try:
            threads=Changebuttoncolor()
            threads._signal.connect(changebutton)
            threads.start()
            time.sleep(0.17)
            #QApplication.processEvents()
            #time.sleep(0.08)
            line_txt=((str(textnarray).replace(',','')).replace(' ','')).replace('\'',' ')
            ex.Txtline.setText(line_txt)

            for col1 in range(17):                  
                ex.button['button1'+'_'+str(col1)].setStyleSheet('''
                    QPushButton{
                    background-color: rgb(211,211,211);
                    }
                    ''')
            for col2 in range(14):
                ex.button['button2'+'_'+str(col2)].setStyleSheet('''
                    QPushButton{
                    background-color: rgb(211,211,211);
                    }
                    ''')
                
            for col3 in range(14):
                ex.button['button3'+'_'+str(col3)].setStyleSheet('''
                    QPushButton{
                    background-color: rgb(211,211,211);
                    }
                    ''')
            
            for col4 in range(13):
                ex.button['button4'+'_'+str(col4)].setStyleSheet('''
                    QPushButton{
                    background-color: rgb(211,211,211);
                    }
                    ''')
            
            for col5 in range(12):
                ex.button['button5'+'_'+str(col5)].setStyleSheet('''
                    QPushButton{
                    background-color: rgb(211,211,211);
                    }
                    ''')
                
            for col6 in range(11):
                if col6== 4:
                    ex.button['button6'+'_'+str(col6)].setStyleSheet('''
                        QPushButton{
                        background-color: rgb(211,211,211);
                        color: rgb(211,211,211) ;
                        }
                        ''')  
                else:
                    ex.button['button6'+'_'+str(col6)].setStyleSheet('''
                        QPushButton{
                        background-color: rgb(211,211,211);
                        }
                        ''')
                    
            for col7 in range(3):
                ex.button['button7'+'_'+str(col7)].setStyleSheet('''
                    QPushButton{
                    background-color: rgb(211,211,211);
                    }
                    ''')

            QApplication.processEvents()
            
        except Exception:
            print('程序停止')
            break  
        
    sys.exit(app.exec_())

