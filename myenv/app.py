from flask import Flask, render_template, request
from markupsafe import Markup
import os

app = Flask(__name__)

def read_file_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return file.readlines()
    except FileNotFoundError:
        return [f"Error: File {file_path} not found"]
    except PermissionError:
        return [f"Error: Permission denied while trying to access {file_path}"]
    except Exception as e:
        return [f"An unexpected error occurred: {e}"]

@app.route('/')
@app.route('/<filename>', methods=['GET'])
def render_file_content(filename='file1.txt'):
    try:
        # Determine file path
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(parent_dir, filename)
        
        # Read the content of the file
        lines = read_file_lines(file_path)

        start_line = request.args.get('start_line', type=int)
        end_line = request.args.get('end_line', type=int)

        if start_line is not None and end_line is not None:
            try:
                lines = lines[start_line - 1:end_line]
            except Exception as e:
                return render_template('error_template.html', error=f"Error processing lines: {e}")

        content = '<br>'.join(lines)
    except FileNotFoundError:
        return render_template('error.html', error_message=f"File '{filename}' not found.")
    except ValueError:
        return render_template('error.html', error_message="Invalid line number parameter.")
    except Exception as e:
        return render_template('error.html', error_message=f"An error occurred: {str(e)}")
    
    # Preserve any HTML markup in the content
    content = Markup(content)

    return render_template('lines.html', content=content)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error_message="Internal server error"), 500

if __name__ == '__main__':
    app.run(debug=True)
