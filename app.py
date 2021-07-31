# from flask import Flask
# app=Flask(__name__)

# @app.route('/')
# def welcome():
#     return "Welcome to Flask"

# if __name__ == "__main__":
#     app.run()

from flask import Flask
# Creates WSGI Application
app = Flask(__name__)

# @app.route(rule, options)

# decorator with binding with function


@app.route('/')
def welcome():
    return "Welcome to Flask"


@app.route('/new')
def prahlad():
    return "Welcome to Prahlad Inala"


# App Starts here
if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
