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

        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText('Enter the first name')

        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText('Enter the last name')



        self.submit = QPushButton('Submit')

        self.submit.clicked.connect(self.dataentry_csv)

        #pass the widget to the layout

        self.layout.addWidget(self.first_name)
        self.layout.addWidget(self.last_name)
        self.layout.addWidget(self.submit)


        # Apply the layout to the window
        self.setLayout(self.layout)

    def dataentry_csv(self):
        first_name_input = self.first_name.text()
        last_name_input = self.last_name.text()

        if os.path.isfile('files/data_entry.csv'):
            with open('files/data_entry.csv','a') as file:
                file.write(f"{first_name_input} , {last_name_input} \n")

        else:
            with open('files/data_entry.csv','w') as file:
                file.write("first_name,last_name\n")
                file.write(f"{first_name_input},{last_name_input}\n")

        self.first_name.clear()
        self.last_name.clear()

        QMessageBox.information(self, 'Success','Data has been added to the csv file')


# Main application setup
app = QApplication(sys.argv)  # Create application object
window = DataEntry()      # Create an instance of the BMI calculator
window.show()                 # Show the GUI window
sys.exit(app.exec())          # Run the application and exit when done
