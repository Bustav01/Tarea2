from app import create_app,db
from app.models import Usuario
from app.methods import crear_usuario
def crear_admin_usr():
    '''Crea un usuario administrador si éste no existe
    Esta script debe ser ejecutada antes de iniciar el sitio, con el fin de no '''
    app = create_app()
    with app.app_context():
        db.create_all()

        userlist = [
            {'username': 'juan', 'password': 'admin', 'role': 'Administrador'},
            {'username': 'pepe', 'password': 'user', 'role': 'Usuario'}]
        for user in userlist:
            if not Usuario.query.filter_by(username = user['username']).first():
                print(f'LOG : Creando Usuario {user["username"]}...')
                crear_usuario(user['username'],user['password'],user['role'])
            else:
                print(f'LOG : Usuario {user["username"]} ya existe')

if __name__ == '__main__':
    crear_admin_usr()



