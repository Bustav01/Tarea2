from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    '''Inicialización de aplicación'''
    app = Flask(__name__,template_folder='templates')

    #Configurar base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    #Importar rutas
    from .routes import app_routes
    app.register_blueprint(app_routes)
    return app