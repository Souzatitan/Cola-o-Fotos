import mysql.connector
from mysql.connector import errorcode



try:
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Efds11091999.',
      )
    
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)
            
            
cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `usuario`;")
cursor.execute("CREATE DATABASE `usuario`;")
cursor.execute("USE `usuario`;")

TABLE={}
TABLE['info_usuarios']='''
    CREATE TABLE `info_usuarios` (
        `nome` varchar(20) NOT NULL,
        `email` varchar(50) NOT NULL,
        `nickname` varchar(8) NOT NULL,
        `senha` varchar(100) NOT NULL,
        PRIMARY KEY (`nickname`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
'''

for tabela_nome in TABLE:
      tabela_sql = TABLE[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

conn.commit()

cursor.close()
conn.close()


    
