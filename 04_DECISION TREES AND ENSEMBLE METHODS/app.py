# flask API

from flask import Flask,jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define a route for GET requests
# @app.route('/<int:number>/')
# def increment(number):
#     print("api called number", number)
#     return "Increment number is" + str(number+1)


# # Define a route for GET requests
# @app.route('/<string:name>/')
# def increment(name):
#     print("api called name", name)
#     return "my name is" + str(name)


details = [
    {'name':'henil', 'address':'surat'}
]

@app.route('/test', methods=['GET'])
def testing():
    return jsonify(details)

if __name__ == "__main__":
    app.run(debug=True)




# Define a route for GET requests
@app.route('/test', methods=['GET'])
def hello_world():
    return "Hello, World!"

# Define a route for GET requests
@app.route('/ml', methods=['GET'])
def new():
    return "data science"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
