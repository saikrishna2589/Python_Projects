import os  # Module to handle file and folder operations
from flask import Flask, render_template_string, request  # Flask essentials for web app and handling file uploads

# Initialize the Flask app
app = Flask(__name__)

# Define the folder where uploaded files will be stored
app.config["UPLOAD_FOLDER"] = "uploads"

# Create the folder if it doesn't already exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


# Define the route for the main page with both GET and POST allowed
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # This variable will store either the file content or error message
    message_client = ""

    # Check if the form was submitted (POST request)
    if request.method == 'POST':

        # Get the file object from the submitted form
        file_object = request.files['file']
        print(type(file_object), file_object)  # Optional debug print

        # Extract the file name (e.g., data.txt, report.json)
        file_name = file_object.filename

        # Check if the file ends with a valid text-based extension
        if file_name.endswith(('.txt', 'csv', '.json')):

            # Construct full path to where the file will be saved
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)

            # Save the uploaded file to the server
            file_object.save(file_path)

            # Open the file and read its content as plain text
            with open(file_path, 'r') as file:
                data = file.read()

            # Store the content to display on the webpage
            message_client = data

        else:
            # If the file is not a text file, show a warning message instead
            message_client = "This is not a text file. Please upload text files only (.txt, .csv, or .json)."

    # Render HTML on the browser with the message passed in
    return render_template_string("""
    <html>
    <title> Upload file</title>
    <h1> Please upload a text file to save on the server</h1>

    <!-- File upload form -->
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">  <!-- File selection field -->
        <input type="submit" value="Uploaddd">  <!-- Upload button -->
    </form>

    <!-- If there's any message from the backend (either content or error), display it -->
    {% if html_message %}
        <p>{{ html_message }}</p>
    {% endif %}
    </html>
    """, html_message=message_client)  # Pass the message to the HTML template


# Run the Flask app in debug mode (auto reloads on code changes)
app.run(debug=True)
