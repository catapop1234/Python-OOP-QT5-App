import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PYPOSQT import Ui_MainWindow
import os
from app1.produs_mgr import ProdusMGR
from app1.servici_mgr import ServiciuMGR
from app1.pachet_mgr import PachetMGR

class MainWindow(QtWidgets.QMainWindow): 

    mgr_produse = ProdusMGR()
    mgr_serviciu = ServiciuMGR()
    mgr_pachet = PachetMGR(mgr_produse, mgr_serviciu)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(self.on_pushButton1_clicked)
        self.ui.pushButton_3.clicked.connect(self.on_pushButton2_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_pushButton3_clicked)
        self.ui.pushButton.clicked.connect(self.on_pushButton7_clicked)
        self.ui.pushButton_13.clicked.connect(self.on_pushButton13_clicked)


        self.ui.pushButton_5.clicked.connect(self.on_pushButton4_clicked)
        self.ui.pushButton_6.clicked.connect(self.on_pushButton5_clicked)
        self.ui.pushButton_7.clicked.connect(self.on_pushButton6_clicked)
        self.ui.pushButton_8.clicked.connect(self.on_pushButton8_clicked)
        self.ui.pushButton_14.clicked.connect(self.on_pushButton14_clicked)


        self.ui.pushButton_9.clicked.connect(self.on_pushButton9_clicked)
        self.ui.pushButton_10.clicked.connect(self.on_pushButton10_clicked)
        self.ui.pushButton_11.clicked.connect(self.on_pushButton11_clicked)
        self.ui.pushButton_12.clicked.connect(self.on_pushButton12_clicked)
        self.ui.pushButton_15.clicked.connect(self.on_pushButton15_clicked)
        



    def on_pushButton1_clicked(self):
        print("Adauga")
        self.mgr_produse.read_produse()

    def on_pushButton2_clicked(self):
        #print("din xml")
        self.mgr_produse.init_lista_from_xml("/home/cata/Desktop/Ti/VS Code/Eclipse/An2_sem2/POO/Lab poo/POS/app1/Produs.xml")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Ai incarcat cu succes Produsele din fisierul XML in lista programului")
        #msg.setInformativeText("More info")
        msg.setWindowTitle("Produs")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        #print("Dialog result:", retval)

    def on_pushButton3_clicked(self):
        #print("in xml")
        self.mgr_produse.save_elemente_to_xml("/home/cata/Desktop/Ti/VS Code/Eclipse/An2_sem2/POO/Lab poo/POS/app1/Produs2.xml")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Ai incarcat cu succes Produsele din lista programului in fisierul XML")
        msg.setWindowTitle("Produs")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
    
    def on_pushButton13_clicked(self):
        #print("in json")
        self.mgr_produse.save_elements_to_json("/home/cata/Desktop/Ti/VS Code/Eclipse/An2_sem2/POO/Lab poo/POS/app1/Produs2.json")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Ai incarcat cu succes Produsele din lista programului in fisierul JSON")
        msg.setWindowTitle("Produs")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def on_pushButton7_clicked(self):
        print("Afiseaza")
        self.mgr_produse.write_produse()

    
    def on_pushButton4_clicked(self):
        print("Adauga")

    def on_pushButton5_clicked(self):
        print("din xml")
        self.mgr_pachet.init_lista_from_xml("/home/cata/Desktop/Ti/VS Code/Eclipse/An2_sem2/POO/Lab poo/POS/app1/Pachet3.xml")

    def on_pushButton6_clicked(self):
        print("in xml")
        self.mgr_pachet.save_elemente_to_xml("/home/cata/Desktop/Ti/VS Code/Eclipse/An2_sem2/POO/Lab poo/POS/app1/Pachet2.xml")
    
    def on_pushButton14_clicked(self):
        print("in json")
        self.mgr_pachet.save_elements_to_json("/home/cata/Desktop/Ti/VS Code/Eclipse/An2_sem2/POO/Lab poo/POS/app1/Pachet2.json")

    def on_pushButton8_clicked(self):
        print("Afiseaza")
        self.mgr_pachet.write_pachet()


    def on_pushButton9_clicked(self):
        print("Adauga")

    def on_pushButton10_clicked(self):
        print("din xml")
        self.mgr_serviciu.init_lista_from_xml("/home/cata/Desktop/Ti/VS Code/Eclipse/An2_sem2/POO/Lab poo/POS/app1/Serviciu.xml")

    def on_pushButton11_clicked(self):
        print("in xml")
        self.mgr_serviciu.save_elemente_to_xml("/home/cata/Desktop/Ti/VS Code/Eclipse/An2_sem2/POO/Lab poo/POS/app1/Serviciu2.xml")

    def on_pushButton15_clicked(self):
        print("in json")
        self.mgr_serviciu.save_elements_to_json("/home/cata/Desktop/Ti/VS Code/Eclipse/An2_sem2/POO/Lab poo/POS/app1/Serviciu2.json")

    def on_pushButton12_clicked(self):
        print("Afiseaza")
        self.mgr_serviciu.write_servicii()



def main():
    app = QtWidgets.QApplication(sys.argv)  # Use QtWidgets.QApplication
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



    
















if __name__ == "__main__":
    main()
