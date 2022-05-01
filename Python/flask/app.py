from flask import Flask
### WSGI application
app = Flask(__name__)

@app.route("/") ## Decorator for increasing the functionality of welcome function
def welcome():
    return "welcome to the Training Basket and please please give your feedback"

@app.route("/batch")
def prem():
    return "welcome to my lecture and please please submit your feedback after class"

if __name__ == "__main__":
    app.run(debug=True)
