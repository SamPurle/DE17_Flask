from flask import Flask, request, jsonify
import pymysql
from datetime import datetime as dt




app = Flask(__name__)



# Connect to the database
connection = pymysql.connect(host='de17mysql.c2wjymfkhjvo.eu-west-2.rds.amazonaws.com',
                             user='admin',
                             password='Pa$$w0rd',
                             db='retail')
cur = connection.cursor()





# create endpoints
# app.route('/')
# def endpoints
q = 'show tables;'
# q = 'insert blablabla'
cur.execute(q)
# connection.commit()
result = cur.fetchall()
print(result)





# CHALLENGE TWO ENDPOINTS
# - TO CREATE / INSERT A PRODUCT
# i.e. http://127.0.0.1:5000/product?name=widget&price=2.99
# DONT FORGET TO COMMIT!!!

@app.route('/product')
def product():
    name = request.args.get('name')
    price = request.args.get('price')
    q = 'insert into product (name, price) values ("{}", {})'.format(name, price)
    cur.execute(q)
    connection.commit()

    return 'Successfully inserted {} with price {}'.format(name, price)

@app.route('/orders')
def orders():
    customerid = request.args.get('customerid')
    productid = request.args.get('productid')
    qty = request.args.get('qty')
    q = 'insert into orders (customerid, productid, qty, orderdate) values ({}, {}, {}, "{}")'.format(customerid, productid, qty, dt.today())
    cur.execute(q)
    connection.commit()

    return 'Successfully placed order for {} of {} with for Customer {} on {}'.format(qty, productid, customerid, dt.today())



if __name__ == '__main__':
    app.run()
