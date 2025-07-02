import sys  # Required to interact with the system (needed for QApplication)
import PyQt6  # Main PyQt6 module

# Import the necessary widgets from PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

# Create a class for the temperature converter window
class TempCentigradeToFahrenheit(QWidget):
    def __init__(self):
        super().__init__()  # Call the parent class constructor

        # Create a vertical layout to stack widgets one below the other
        self.layout = QVBoxLayout()

        # Create a label prompting the user to enter temperature
        self.temp_label = QLabel('Temperature in degrees (C)')

        # Create a text input field for the user to type Celsius value
        self.temp_entry = QLineEdit()

        # Create a button that the user clicks to convert the temperature
        self.button = QPushButton('Convert to Fahrenheit degrees')

        # Create a label to display the result (starts empty)
        self.result = QLabel('')

        # Add all widgets to the vertical layout
        self.layout.addWidget(self.temp_label)
        self.layout.addWidget(self.temp_entry)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.result)

        # Set the layout to the main window
        self.setLayout(self.layout)

        # Connect the button click event to the function that does the conversion
        self.button.clicked.connect(self.convert_temp)

    # Function that runs when the button is clicked
    def convert_temp(self):
        user_input_celsius = self.temp_entry.text()  # Get the text entered by the user
        fahrenheit = float(user_input_celsius) * 9/5 + 32  # Convert Celsius to Fahrenheit
        output = self.result.setText(str(fahrenheit))  # Display the result in the label
        return output  # Return value is optional here — not used, but fine to keep

# Create the main application object
app = QApplication(sys.argv)

# Create an instance of the converter window
window = TempCentigradeToFahrenheit()

# Show the window
window.show()

# Keep the application running until the user closes it
sys.exit(app.exec())
