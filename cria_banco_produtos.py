import mysql.connector

print('Conectar...')

conn = mysql.connector.connect(
        host='bancoaws.cwk0wcobxxss.us-east-1.rds.amazonaws.com',
        user='admin',
        password='123456789'
)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `Produtos`;")

cursor.execute("CREATE DATABASE `Produtos`;")

cursor.execute("Use `Produtos`;")

cursor.execute(
    '''
    CREATE TABLE Produtos(
        id int NOT NULL AUTO_INCREMENT,
        nome varchar(100) not null,
        preco decimal(5,2) not null,
        PRIMARY KEY(`id`)
    )
    '''
)



conn.commit()
cursor.close()
conn.close()