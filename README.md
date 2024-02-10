File Viewer Web Application
This is a Flask-based web application that allows users to view the contents of text files in their web browser.

Features
File Viewing: Users can view the contents of text files directly in their web browser.
Line Selection: Optional URL query parameters allow users to specify start and end line numbers to view only a portion of the file.
Error Handling: The application gracefully handles file not found errors, invalid line number parameters, and other unexpected errors, displaying informative error messages to the user.
HTML Markup Preservation: Any HTML markup present in the file content is preserved and rendered properly in the browser.

Usage
1... Clone this repository to your local machine:
2... Navigate to the project directory:
3... Install the required dependencies:
     pip install -r /myenv/requirements.txt
4... Run the Flask application:
     python app.py

Open your web browser and go to http://127.0.0.1:5000/ to view the default file (file1.txt). Optionally, you can specify a different file name in the URL, e.g., http://127.0.0.1:5000/file2.txt.

You can also specify start and end line numbers as URL query parameters to view only a portion of the file, e.g., http://127.0.0.1:5000/file1.txt?start_line=5&end_line=10.

Dependencies
Flask: Web framework for Python
MarkupSafe: Library for HTML escaping
