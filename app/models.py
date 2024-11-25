from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False) #TO DO: recibir hash
    role = db.Column(db.String(10), nullable=False)


class Compra:
    def __init__(self, nombre:str='', edad:str='', tarros:str=''):
        self.nombre = nombre
        self.edad = edad
        self.tarros = tarros

    def set_compra(self, nombre:str, edad:int, tarros:int):
        self.nombre = nombre
        self.edad = edad
        self.tarros = tarros
    def get_compra(self)->dict:
        return {
            'nombre' : self.nombre,
            'edad' : self.edad,
            'tarros' : self.tarros,
                }
