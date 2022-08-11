from jogoteca import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,render_template,request,redirect,session,flash, url_for

class Jogos (db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    nome=db.Column(db.String(50),nullable=False)
    categoria=db.Column(db.String(40),nullable=False)
    console=db.Column(db.String(20),nullable=False)
    
    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios (db.Model):
    nome=db.Column(db.String(20),nullable=False)
    nickname=db.Column(db.String(8),nullable=False,primary_key=True)
    senha=db.Column(db.String(100),nullable=False)

    def __repr__(self):#codigo pronto que garante que o modelo acima vai rodar com o banco e printar informações
        return '<Name %r>' % self.name

