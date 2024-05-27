from app import db


class usuario(db.Model):
    nome = db.column(db.String(20),nullable=False)
    email = db.column(db.String(50),unique=True,nullable=False)
    nickname = db.column(db.String(8),unique=True,primary_key=True)
    senha = db.collumn(db.interger,unique=True, nullable=False)