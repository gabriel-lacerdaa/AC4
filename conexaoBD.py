import mysql.connector

conn = mysql.connector.connect(
        host='bancoaws.cwk0wcobxxss.us-east-1.rds.amazonaws.com',
        user='admin',
        password='123456789'
)
cursor = conn.cursor()