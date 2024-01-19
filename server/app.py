# flask_app.py

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>", 200


@app.route("/print/<parameter>")
def print_parameter(parameter):
    print(parameter)  # Add this line to print to the console
    return parameter


@app.route("/count/<int:parameter>")
def count(parameter):
    result = "\n".join(str(i) for i in range(parameter))
    print(result)  # Add this line to print to the console
    return result


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math_operations(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return str(result), 200


if __name__ == "__main__":
    app.run(port=5555, debug=True)
