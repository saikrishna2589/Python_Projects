
import sys  # Required to use sys.argv and exit the app properly
import PyQt6  # PyQt6 is the GUI framework being used

# Importing required GUI components from PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

# Creating a class for the BMI Calculator, which is a QWidget (basic window)
class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()  # Call the parent class constructor

        self.setWindowTitle("BMI Calculator")  # Set the title of the window

        # Create a vertical layout to stack widgets on top of each other
        self.layout = QVBoxLayout()

        # Input box for weight
        self.weight_entry = QLineEdit()
        self.weight_entry.setPlaceholderText("Weight (kg)")  # Shows a hint in the input box

        # Input box for height
        self.height_entry = QLineEdit()
        self.height_entry.setPlaceholderText("Height (m)")  # Shows a hint in the input box

        # Button to trigger BMI calculation
        self.button = QPushButton('Calculate BMI')

        # Label to display the result
        self.result = QLabel('')

        # Add all the widgets to the layout
        self.layout.addWidget(self.weight_entry)
        self.layout.addWidget(self.height_entry)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.result)

        # Apply the layout to the window
        self.setLayout(self.layout)

        # Connect the button click to the BMI calculation function
        self.button.clicked.connect(self.calculateBMI)

    # Function that calculates BMI
    def calculateBMI(self):
        user_input_weight = float(self.weight_entry.text().strip())  # Get and clean the weight input
        user_input_height = float(self.height_entry.text().strip())  # Get and clean the height input

        # Calculate BMI using the formula and round to 2 decimal places
        bmi = round(user_input_weight / (user_input_height ** 2), 2)

        # Display the result in the result label
        output = self.result.setText(f" Your BMI is {str(bmi)}")
        return output

# Main application setup
app = QApplication(sys.argv)  # Create application object
window = BMICalculator()      # Create an instance of the BMI calculator
window.show()                 # Show the GUI window
sys.exit(app.exec())          # Run the application and exit when done
