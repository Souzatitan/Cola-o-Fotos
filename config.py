import os

SQLALCHEMY_DATABASE_URI ='mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'Efds11091999.',
        servidor = 'localhost',
        database = 'usuario'
        
    )
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'