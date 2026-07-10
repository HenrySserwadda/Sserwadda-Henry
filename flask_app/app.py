# Import flask
from flask import Flask

# Create an Instance of a flask class
# ''__name__" is a special variable that tells Flask where to look for resouces

app = Flask(__name__)

#Decorator: /about : Maps the URL '/' 

@app.route('/')

# Define a function to display text Welcome to Flask

def home():
    # Write the Text that can be displayed on your browser
    return '<h1> Welcom to Flask Framework </h2>'

# To Ensure your server runs only if this script is executed directly

if __name__ == '__main__':
    app.run(debug=True)