#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pandas as pd
import matplotlib.pyplot as plt

#Importar​ aquí las librerías a utilizar

from PyQt5 import uic, QtWidgets

qtCreatorFile = "appandas.ui" #Aquí​ va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        #Aquí​ van los botones
        self.boton1.clicked.connect(self.getCSV)
        self.boton2.clicked.connect(self.plot)
    #Aquí​ van las nuevas funciones
    def plot (self) :
       x=self.df['col1']
       y=self.df['col2']
       plt.plot(x,y)
       plt.show()
       estad = "Estadisticas de col2: "+str(self.df['col2'].describe())
       self.resultado.setText(estad)

    #Esta​ función abre el archivo CSV    
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/')
        if filePath != "":
            print ("Dirección",filePath) #Opcional​ imprimir la dirección del archivo
            self.df = pd.read_csv(str(filePath))
    
  
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
