from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow


app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'kubrick.db')


db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/')
def root():
    return 'Welcome to my awesome web-site!'

'''@app.route('/consultant/<string:cohort>')
def consultant(cohort: str):
    return 'This is the consultant page for {}'.format(cohort)'''

@app.route('/consultant')
def consultant():
    chrt = request.args.get('cohort')
    cohort_details = cohort.query.filter_by(cohort_name = chrt).first()
    result = cohort_schema.dump(cohort_details)
    return jsonify(result), 200

@app.route('/client')
def client():
    client = request.args.get('client')
    client_details = client.query.filter_by(name = client).first()
    result = client_schema.dump(client_details)
    return jsonify(result), 200

class Cohort(db.Model):
    __tablename__ = 'cohort'
    id = Column(Integer, primary_key = True)
    cohort_name = Column(String, unique = True)
    start_date = Column(String)
    specialism = Column(String)

class CohortSchema(ma.Schema):
    class Meta():
        fields = ('id', 'cohort_name', 'start_date', 'specialism')

class ClientSchema(ma.Schema):
    class Meta():
        fields = ('id', 'name', 'head_office', 'sector')



if __name__ == '__main__':
    app.run()
