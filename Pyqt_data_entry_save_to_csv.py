import os.path
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QLabel, QLineEdit, QPushButton,QMessageBox)



class DataEntry(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.setGeometry(380,380,300,100)

        self.setWindowTitle('Data Entry tool')

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText('Enter Name')

        self.submit = QPushButton('Submit')

        self.submit.clicked.connect(self.dataentry_csv)

        #pass the widget to the layout

        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.submit)

        # Apply the layout to the window
        self.setLayout(self.layout)

    def dataentry_csv(self):
        input_name = self.input_name.text()
        if os.path.isfile('files/data_entry.csv'):
            with open('files/data_entry.csv','a') as file:
                file.write(f"{input_name}\n")

        else:
            with open('files/data_entry.csv','w') as file:
                file.write("name\n")
                file.write(f"{input_name}\n")

        self.input_name.clear()

        QMessageBox.information(self, 'Success','Data has been added to the csv file')


# Main application setup
app = QApplication(sys.argv)  # Create application object
window = DataEntry()      # Create an instance of the BMI calculator
window.show()                 # Show the GUI window
sys.exit(app.exec())          # Run the application and exit when done
