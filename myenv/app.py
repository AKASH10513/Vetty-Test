from flask import Flask, render_template, request, abort
from markupsafe import Markup
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<filename>', methods=['GET'])
def render_file_content(filename='file1.txt'):
    try:
        # Determine file path
        parent_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(parent_directory, filename)
        
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Extract optional URL query parameters
            start_line = int(request.args.get('start_line', 1))
            end_line = int(request.args.get('end_line', -1))
            
            # Handle negative indices for end_line
            if end_line < 0:
                end_line = len(lines) + end_line + 1
            
            # Validate line numbers
            if start_line < 1 or end_line < start_line or end_line > len(lines):
                raise ValueError("Invalid line number parameter.")
            
            # Extract the lines based on start_line and end_line
            content = ''.join(lines[start_line - 1:end_line])
    except FileNotFoundError:
        return render_template('error.html', error_message=f"File '{filename}' not found.")
    except ValueError:
        return render_template('error.html', error_message="Invalid line number parameter.")
    except Exception as e:
        return render_template('error.html', error_message=f"An error occurred: {str(e)}")
    
    # Preserve any HTML markup in the content
    content = Markup(content)

    return render_template('file_content.html', content=content)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error_message="Internal server error"), 500

if __name__ == '__main__':
    app.run(debug=True)
