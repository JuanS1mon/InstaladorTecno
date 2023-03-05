import sys
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import Qt, QPropertyAnimation,QEasingCurve
from PyQt5.QtWidgets import QMainWindow, QApplication
from db import *
from VerifSO import *
from backoffice import *
from Diccionario import errores

#Crearmos la clase principal de el entorno grafico
class Ventana_Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sistema.ui', self)

        # comunicacion con la base de datos
        #self.basededatos = conexion()

        #Saca Barra FEA
        window = QMainWindow()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(1) #1 es visible  0 invisible

        #sizedgrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #Mover Ventana
        self.frame_barra.mouseevent = self.mover_ventana

        # Controles de barra
        self.b_cerrar.clicked.connect(lambda: self.close())
        self.b_minimizar.clicked.connect(self.control_minimizar)


        # Trae los datos del config.cfg
        server, base = leer_cfg()
        self.T_Server.setText (base)
        self.T_Base.setText(server)
        self.B_conexion.clicked.connect(conexion)

        #Trae datos de Info.Sys para arielito
        self.B_info.clicked.connect(VerifSo)

        #Instalador - Actualiza campos en BD.
        #fantasia, cuit, RazonSocial, Direccion, CantCajas, ClienteID=self.completa_Sistema()
        self.B_Update.clicked.connect(self.completa_Sistema)






        # Minimizar
    def control_minimizar(self):
        self.showMinimized()

        #SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # mover ventana
    def MousePressEvent(self, event):
        self.click_position = event.globalpos()

    def mover_ventana(self, event):
        print('asd')
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalpos() - self.click_position)
                self.click_position = event.globalpos()
                event.accept()
            if event.globalpos().y() <=10:
                self.showMaximized()
            else:
                self.showNormal()

    #Valores a llenar para la tabla Sistema de tecnolar.
    def completa_Sistema(self):
        fantasia = self.T_Fantasia.text()
        RazonSocial =self.T_RazonSocial.text()
        Direccion = self.T_Direccion.text()
        cuit = self.T_Cuit.text()
        ClienteID = self.T_ClienteWeb.text()
        CantCajas = self.T_Cajas.text()
        BackOffice(fantasia, cuit, RazonSocial, Direccion, CantCajas, ClienteID)

        #return fantasia, cuit, RazonSocial, Direccion, CantCajas, ClienteID






if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Ventana_Principal()
    GUI.show()
    sys.exit(app.exec())

