from flask import Flask, render_template, request, abort
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<filename>', methods=['GET'])
def render_file_content(filename='file1.txt'):
    try:
        # Determine file path
        parent_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(parent_directory, filename)
        
        # Extract query parameters
        start_line = int(request.args.get('start_line', 1))
        end_line = int(request.args.get('end_line', -1))
        
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Handle negative indices for end_line
            if end_line < 0:
                end_line = len(lines) + end_line + 1
            
            # Extract the lines based on start_line and end_line
            content = ''.join(lines[start_line - 1:end_line])
    except FileNotFoundError:
        return render_template('error.html', error_message=f"File '{filename}' not found.")
    except UnicodeDecodeError:
        return render_template('error.html', error_message=f"Error decoding file '{filename}'. Please ensure it is encoded properly.")
    except Exception as e:
        return render_template('error.html', error_message=f"An error occurred: {str(e)}")
    
    return render_template('file_content.html', content=content)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error_message="Internal server error"), 500

if __name__ == '__main__':
    app.run(debug=True)
