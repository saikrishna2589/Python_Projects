# Import necessary libraries
import json
from kivy.app import App  # Base class for the app
from kivy.uix.boxlayout import BoxLayout  # Layout to organize widgets vertically
from kivy.uix.textinput import TextInput  # For user input
from kivy.uix.button import Button  # Button widget
from kivy.uix.label import Label  # Label to show translation

# Path to the JSON file that contains English-German word mappings
file_loc = 'files/english_german.json'

# Define the main Translator App class
class TranslatorApp(App):

    # This function builds the UI and loads the dictionary
    def build(self):
        # Create a vertical box layout with padding and spacing
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a text input box for the user to enter a word
        self.input_box = TextInput(
            multiline=False,       # Single-line input
            size_hint=(1, 0.3),    # Takes full width and 30% height
            hint_text='Enter a word'  # Placeholder text
        )

        # Create a button labeled "Translate"
        self.translate_button = Button(
            text='Translate',
            size_hint=(1, 0.2)  # Full width, 20% height
        )

        # When the button is pressed, call the translate() function
        self.translate_button.bind(on_press=self.translate)

        # Create a label to display the translated word or error message
        self.translation = Label(
            text='',
            size_hint=(1, 0.5)  # Full width, 50% height
        )

        # Add all widgets to the layout
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.translate_button)
        self.layout.add_widget(self.translation)

        # Load the dictionary from the JSON file
        self.translate_from_json()

        # Return the layout to be rendered
        return self.layout

    # Function to perform translation when the button is clicked
    def translate(self, instance):
        word = self.input_box.text.strip()  # Get and clean the input word
        # Look up the word in the dictionary, or return "Word not found"
        translated_word = self.dictionary.get(word, 'Word not found')
        # Update the label to show the translated word
        self.translation.text = translated_word

    # Function to load the English-German dictionary from a JSON file
    def translate_from_json(self):
        try:
            with open(file_loc, 'r') as file:
                self.dictionary = json.load(file)
        except FileNotFoundError:
            # If the file is missing, initialize an empty dictionary and show error
            self.dictionary = {}
            self.translation.text = 'Dictionary file not found!'

# Instantiate the app and run it
TranslatorApp().run()
