from flask import Flask

#Create an instance of the Flask class
app = Flask(__name__)

#Define a route for the root URL ("/")
@app.route('/')
def helloWorld():
#This function will be executed when the root URL is accessed
    return 'Hello, World!'
#Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)