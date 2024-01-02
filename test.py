from flask import jsonify,Flask,request

app = Flask(__name__)

incomes = [{"description": "Salary", "income": 30000}]

@app.route('/')
def hello():
    return "hello"

@app.route('/incomes')
def get_income():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return "", 204
