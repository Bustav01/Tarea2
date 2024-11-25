from werkzeug.security import generate_password_hash,check_password_hash
from .models import *
from . import db

# Metodos Generales
def validar_campo_vacio(campos: dict[str, str]) -> list[str]:
    '''Valida que los campos no estén vacíos. Retorna lista de claves con campos vacíos
    Parámetros: campos: diccionario con campos y sus valores (string)'''
    return [campo for campo, valor in campos.items() if not valor.strip()]

def obener_formulario(formulario: dict) -> Compra:
    '''Obtiene los datos dentro de un formulario'''
    return Compra(nombre=formulario.get('nombre','').strip(),
                  edad=formulario.get('edad','').strip(),
                  tarros=formulario.get('tarros','').strip()
                  )

# Metodos para ejercicio 1
def calc_total(tarros:int, valor_tarros:int)->int:
    return tarros * valor_tarros

def calc_descuento(edad:int,valor_compra:int)->float:
    if edad < 18:
        return 0.0
    if 18 <= edad <= 30:
        return round(valor_compra * 0.15,1)
    if edad > 30:
        return round(valor_compra * 0.25,1)

def calc_totalPagar(edad:int,valor_compra:int,descuento:float)->float:
    if edad < 18:
        resultado = round(valor_compra,0)
    else:
        resultado = round( valor_compra - descuento,0)
    return resultado


# Metodos para ejercicio 2
def usuario_existe(username:str) -> bool:
    '''Verifica si el usuario ya existe'''
    return Usuario.query.filter_by(username=username).first() is not None

def crear_usuario(username:str, password:str, role:str='user') -> dict[str,bool]:
    '''Crea usuario si no existe
    Retorno: diccionario con detalles'''
    if usuario_existe(username):
        reporte = {'mensaje': 'El usuario ya existe' ,'exito':False}
    else:
        password_hash = generate_password_hash(password)
        new_user = Usuario(username=username,password_hash=password_hash,role=role)
        db.session.add(new_user)
        db.session.commit()
        reporte = {'mensaje':'Usuario creado','exito':True}
    return reporte

def chk_password_usuario(user,password) -> bool:
    return check_password_hash(user.password_hash,password)

def edit_usuario(user_id, username:str, password:str, role:str=None) -> dict[str,bool]:
    '''Edita los detalles de un usuario existente.
    Retorna: diccionario con mensaje de éxito'''

    if not usuario_existe(username):
        return {'mensaje': 'Usuario no encontrado', 'exito': False}
    if username:
        Usuario.username = username
    if password:
        Usuario.password_hash = generate_password_hash(password)
    if role:
        Usuario.role = role
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {'mensaje': f'Error al actualizar el usuario: {str(e)}', 'exito': False}
    return {'mensaje': 'Usuario actualizado', 'exito': True}

