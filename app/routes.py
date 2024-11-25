from flask import Blueprint, render_template,request
from app.methods import *

app_routes = Blueprint('app_routes', __name__)


# RUTAS:
@app_routes.route('/')
def home():
    return render_template('home.html')

@app_routes.route('/ejercicio1', methods=['GET', 'POST'])
def ej1():
    print("LOG: ruta //ejercicio1 ejecutada")
    errores:list = []
    cotizacion = obener_formulario(request.form.to_dict()) if request.method == 'POST' else Compra()
    resultado = None

    if request.method == 'POST':
        # Validación
        print("LOG: Validación campos vacíos y rangos")
        campos_vacios:list[str] = validar_campo_vacio(cotizacion.get_compra())
        if campos_vacios:
            errores.append(f"Campos vacíos: {', '.join(campos_vacios)}")
        if not campos_vacios:
            if cotizacion.edad and (not cotizacion.edad.isdigit() or int(cotizacion.edad) <= 0):
                errores.append("La edad debe ser un número mayor a 0.")
            if cotizacion.tarros and (not cotizacion.tarros.isdigit() or int(cotizacion.tarros) <= 0):
                errores.append("La cantidad de tarros debe ser un número mayor a 0.")
        print("LOG: Validación completada")
        if not errores:
            cotizacion.edad = int(cotizacion.edad)
            cotizacion.tarros = int(cotizacion.tarros)
            valor_tarros:int = 9000

            # Procesar datos
            total_sinDescuento:int = calc_total(cotizacion.tarros, valor_tarros)
            descuento:float = calc_descuento(cotizacion.edad, total_sinDescuento)
            total_pagar:float = calc_totalPagar(cotizacion.edad,total_sinDescuento, descuento)

            resultado = {
                'Nombre del cliente': fr' ${cotizacion.nombre}',
                'Total sin descuento': fr' ${total_sinDescuento}',
                'El descuento es': fr' {descuento}',
                'El total a pagar es de' : fr'{total_pagar}'
            }
    return render_template('ejercicio1.html',
                           datos=cotizacion.get_compra(),
                           errores=errores,
                           resultado=resultado)

@app_routes.route('/ejercicio2', methods=['GET', 'POST'])
def ej2():
    print("LOG: ruta /ejercicio2 ejecutada")
    mensaje = None
    errores:list = []
    datos:dict ={'usuario':'', 'password':''}

    if request.method == 'POST':
        # Obtener datos de formulario
        datos['usuario'] = request.form.get('usuario','').strip()
        datos['password'] = request.form.get('password','').strip()

        # Validación
        campos_vacios = validar_campo_vacio(datos)
        if campos_vacios:
            errores.append("Campos vacíos: {', '.join(campos_vacios)}")
        else:
            user = Usuario.query.filter_by(username=datos['usuario']).first()
            if user and chk_password_usuario(user, datos['password']):
                mensaje = f"Bienvenido {user.role} {user.username}"
            else:
                mensaje = f"Usuario o contraseña incorrectos"
    return render_template('ejercicio2.html',
                           datos = datos,
                           mensaje=mensaje,
                           errores=errores)