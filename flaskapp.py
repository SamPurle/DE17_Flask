from flask import Flask, request


app = Flask(__name__)

@app.route('/cohort')
def cohort():
    cohort_name = request.get.args('cohort')
