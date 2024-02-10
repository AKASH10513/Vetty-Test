from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and its handler
from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
