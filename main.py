#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar, QFileDialog
from PyQt5 import QtGui, uic

qtCreatorFile = "dialog.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class LinearniSifra(QMainWindow, Ui_MainWindow):
    def error(self,msg):
        print(msg)
        
    def code(self):
        outstring = ""
        rdystring = ""
        instring = self.input.toPlainText()
        a = int(self.aKey.text())
        b = int(self.bKey.text())
        x = 0   
        
        for i in range (0,len(instring)):
            
            if (instring[i]<"a" or instring[i]>"z") and instring[i]!=" ":
                if instring[i]>="A" and instring[i]<="Z":
                    rdystring+=chr(ord(instring[i])+32)    
            else:
                rdystring+=instring[i]

       

        for i in range (0,len(rdystring)):
            
            if rdystring[i]==" ":
                outstring+="xwx"
            else:
                x = ord(rdystring[i])-97
                outstring+= chr(((a*x+b) % 26)+97)
        
        self.output.setText(outstring)
        
    def decode(self):
        deinstring = self.input.toPlainText()
        deoutstring = ""
        a = int(self.aKey.text())
        b = int(self.bKey.text())
        x = 0
        i=0
        while i<len(deinstring):
            if deinstring[i:(i+3)]=="xwx":
                deoutstring+=" "
                i+=3
            else:
                x=ord(deinstring[i])-97
                while x<b:
                    x+=26
                while (x-b)%a!=0:
                    x+=26
                
                x=int((x-b)/a)
                deoutstring+=chr(x+97)
                i+=1
                
        self.output.setText(deoutstring)
        
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.codeButton.clicked.connect(self.code)
        self.decodeButton.clicked.connect(self.decode)
        #self.saveButton.clicked.connect(self.saveFile)
        #self.messageEdit.textChanged.connect(self.loadMessage)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinearniSifra()
    window.show()
    sys.exit(app.exec_())