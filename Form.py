import sys
from PyQt5 import QtWidgets

class FormWindow(QtWidgets.QWidget):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Input Form")
        self.layout = QtWidgets.QFormLayout()

        # Create widgets for the form
        self.nume_label = QtWidgets.QLabel("Numele:")
        self.nume_input = QtWidgets.QLineEdit()

        self.cod_intern_label = QtWidgets.QLabel("Codul intern:")
        self.cod_intern_input = QtWidgets.QLineEdit()

        self.pret_label = QtWidgets.QLabel("Pretul:")
        self.pret_input = QtWidgets.QLineEdit()

        self.categorie_label = QtWidgets.QLabel("Categoria:")
        self.categorie_input = QtWidgets.QLineEdit()

        self.p_label = QtWidgets.QLabel("Producator:")
        self.p_input = QtWidgets.QLineEdit()

        # Add widgets to the layout
        self.layout.addRow(self.nume_label, self.nume_input)
        self.layout.addRow(self.cod_intern_label, self.cod_intern_input)
        self.layout.addRow(self.pret_label, self.pret_input)
        self.layout.addRow(self.categorie_label, self.categorie_input)
        self.layout.addRow(self.p_label, self.p_input)

        # Create a submit button
        self.submit_button = QtWidgets.QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_form)

        # Add the button to the layout
        self.layout.addRow(self.submit_button)

        # Set the layout for the form window
        self.setLayout(self.layout)

    def submit_form(self):
        # Retrieve input values
        nume = self.nume_input.text()
        cod_intern = self.cod_intern_input.text()
        pret = int(self.pret_input.text())
        categorie = self.categorie_input.text()
        prod=self.p_input.text()

        # Call the manager method to add the new element
        self.manager.add_element(nume, cod_intern, pret, categorie,prod)

        # Show a confirmation message
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Form Submitted")
        msg.setText(f"Numele: {nume}\nCodul intern: {cod_intern}\nPretul: {pret}\nCategoria: {categorie}\nProducator: {prod}")
        msg.exec_()

        # Close the form after submission
        self.close()
