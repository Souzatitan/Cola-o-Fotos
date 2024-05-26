import mysql.connector
from mysql.connector import errorcode



try:
    conn=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Efds11091999.',
      )
    
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)
            
            
cursor = conn.cursor()

cursor.execute ("'DROP DATABASE IF EXIST `usuarios`;")
cursor.execute ("CREATE DATABASE `usuario`;")
cursor.execute ("USE `usuarios`;")   

TABLLE = []
TABLLE ['info_usuarios']=('''
         CREATE TABLLE `info_usuarios`(
             `nome` varchar(20) NOT NULL;
             `email` nvarchar(50) NOT NULL;
             `nickname` varhchar(8) NOT NULL;
             `senha` varchar(100)NOT NULL
             PRIMARY KEY (`nickname`)
         )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
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


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("Bruno Divino", "BD", generate_password_hash("alohomora").decode('utf-8')),
      ("Camila Ferreira", "Mila", generate_password_hash("paozinho").decode('utf-8')),
      ("Guilherme Louro", "Cake", generate_password_hash("python_eh_vida").decode('utf-8'))
]
cursor.executemany(usuario_sql, usuarios)

print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

cursor.executemany(info, info)

cursor.execute('select * from jogoteca.info')
print(' -------------  info:  -------------')
for info in cursor.fetchall():
    print(info[1])

conn.commit()

cursor.close()
conn.close()


    
