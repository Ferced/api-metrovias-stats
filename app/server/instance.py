from flask import Flask
from flask_cors import CORS
from flask_restplus import Api, Resource, fields
from environment.instance import environment_config
import os


class Server(object):

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        # Path de directorio
        self.basedir = os.path.abspath(os.path.dirname(__file__)+r"\..")
        # Configuracion APP
        self.app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(self.basedir,r'db/db.sqlite')
        print ("BASE DE DATOS: ")
        print ('sqlite:///' + os.path.join(self.basedir,'db/db.sqlite'))
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
        self.api = Api(self.app, 
            version='1.0', 
            title='Api metroviasStats',
            description='Una api para trackear las metrovias stats', 
            doc = environment_config["swagger-url"]
        )
    def run(self):
        self.app.run(
                debug = environment_config["debug"], 
                port = environment_config["port"]
            )

server = Server()