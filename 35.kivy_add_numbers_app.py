# Import necessary libraries
import json
from kivy.app import App  # Base class for the app
from kivy.uix.boxlayout import BoxLayout  # Layout to organize widgets vertically
from kivy.uix.textinput import TextInput  # For user input
from kivy.uix.button import Button  # Button widget
from kivy.uix.label import Label  # Label to show calculation


# Define the main calculator App class
class calculatorApp(App):

    # This function builds the UI and loads the dictionary
    def build(self):
        # Create a vertical box layout with padding and spacing
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a text input box for the user to enter a number
        self.input_box = TextInput(
            multiline=False,       # Single-line input
            size_hint=(1, 0.3),    # Takes full width and 30% height
            hint_text='Enter a number'  # Placeholder text
        )
        self.input_box_2 = TextInput(
            multiline=False,  # Single-line input
            size_hint=(1, 0.3),  # Takes full width and 30% height
            hint_text='Enter another number'  # Placeholder text
        )

        # Create a button labeled "Result"
        self.result_button = Button(
            text='Result',
            size_hint=(1, 0.2)  # Full width, 20% height
        )

        # When the button is pressed, call the result() function
        self.result_button.bind(on_press=self.calculated_numbers)

        # Create a label to display the translated word or error message
        self.finalresult = Label(
            text='',
            size_hint=(1, 0.3)  # Full width, 30% height
        )

        # Add all widgets to the layout
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.input_box_2)
        self.layout.add_widget(self.result_button)
        self.layout.add_widget(self.finalresult)

        # call the function that calculates numbers

        # Return the layout to be rendered
        return self.layout

    # Function to perform calculation when the button is clicked
    def calculated_numbers(self, instance):
        number1 = float(self.input_box.text.strip())
        number2 =float(self.input_box_2.text.strip())

        calculated_result = number1 + number2


        # Update the label to show the translated word
        self.finalresult.text = str(calculated_result)

# Instantiate the app and run it
calculatorApp().run()
