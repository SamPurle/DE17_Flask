import json
import pymysql.cursors

def lambda_handler():
    connection = pymysql.connect(host='de17mysql.c2wjymfkhjvo.eu-west-2.rds.amazonaws.com',
                             user='admin',
                             password='Pa$$w0rd',
                             db='retail')
    cur = connection.cursor()
    cur.execute('SELECT * FROM orders;')
    result = cur.fetchall()
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

res = lambda_handler()

print(res)
