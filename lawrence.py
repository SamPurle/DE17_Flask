from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'kubrick.db')


db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/')
def root():
    return "Welcome to my awsome website!"



# @app.route('/consultant/<string:cohort>')
# def consultant(cohort: str):
#     return "This is the consultant portal for {}".format(cohort)


@app.route('/consultant')
def consultant():
    # grab cohort from the query string /consultant?cohort=de17
    chrt = request.args.get('cohort')
    cohortdetails = Cohort.query.filter_by(cohortname=chrt).first()
    result = cohort_schema.dump(cohortdetails)
    return jsonify(result), 200


@app.route('/client')
def client():
    client = request.args.get('client_name')
    client_details = Client.query.filter_by(name=client).first()
    result = client_schema.dump(client_details)
    return jsonify(result), 200


class Cohort(db.Model):
    __tablename__ = 'cohort'
    id = Column(Integer, primary_key=True)
    cohortname = Column(String, unique=True)
    startdate = Column(String)
    specialism = Column(String)


class CohortSchema(ma.Schema):
    class Meta():
        fields = ('id', 'cohortname', 'startdate', 'specialism')


cohort_schema = CohortSchema()

class Client(db.Model):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    head_office = Column(String, unique = True)
    sector = Column(String)

class ClientSchema(ma.Schema):
    class Meta():
        fields = ('id', 'name', 'head_office', 'sector')

client_schema = ClientSchema()



if __name__ == '__main__':
    app.run()
