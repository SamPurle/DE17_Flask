import pymysql

connection = pymysql.connect(host = 'de17mysql.c2wjymfkhjvo.eu-west-2.rds.amazonaws.com',
                             user = 'admin',
                             password = 'Pa$$w0rd',
                             db = 'retail',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

cur = connection.cursor()

show = 'show tables;'


cur.execute(show)
result = cur.fetchall()
print('The table in the reail database are: \n{}\n'.format(result))


for table in result:
    table_name = table['Tables_in_retail']
    q = 'select * from {};'.format(table_name)
    cur.execute(q)
    result = cur.fetchall()
    print('{}: \n{}\n'.format(table_name, result))
