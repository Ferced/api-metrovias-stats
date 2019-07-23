from flask_sqlalchemy import SQLAlchemy
import os

db=SQLAlchemy()
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    linea=db.Column(db.String(500))
    tweet=db.Column(db.String(500))
    fecha=db.Column(db.DateTime)
    def __init__(self, linea,tweet,fecha):
        self.linea=linea
        self.tweet=tweet
        self.fecha=fecha 
