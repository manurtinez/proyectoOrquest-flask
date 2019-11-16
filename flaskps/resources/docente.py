from flask import (
    render_template,
    jsonify,
    abort,
    url_for,
    request,
    redirect,
    session,
    flash,
)
from flaskps.models.configuracion import configuracion
from flaskps.models.rol import Rol
from flaskps.models.usuario_tiene_rol import User_tiene_rol
from flaskps.models.escuela import Escuela
from flaskps.models.nivel import Nivel
from flaskps.models.usuario import User
from flaskps.models.barrio import Barrio
from flaskps.models.genero import Genero
from flaskps.models.docente import Docente
import json, requests

def listadoDocente():
    if 'email' not in session:
        return redirect(url_for("accesoDenegado"))
    tabla = configuracion.get_config()
    if tabla.sitio_habilitado == 0:
        return redirect(url_for("mantenimiento"))
    lista = Docente.all()
    tiposDNI = []
    listaLoc = []
    dnis = requests.get(
        "https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento"
    )
    localidades = requests.get(
        "https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad"
    )
    dnis = json.loads(dnis.text)
    localidades = json.loads(localidades.text)
    user = User.get_by_email(session['email'])
    roles = Rol.all()
    aux = []
    for r in roles:
        if User_tiene_rol.tiene_rol(user.id, r.id):
            aux.append(r.nombre)
    print(aux)
    return render_template(
        "/docente/listado.html", lista=lista, cant=tabla.cantListar,
        escuelas=Escuela.get_all(),
        niveles=Nivel.get_all(),
        barrios=Barrio.get_all(),
        generos=Genero.get_all(),
        dnis=dnis,
        localidades=localidades,
        roles=aux,
    )
def crearDocente():
    p = request.form
    Docente.create(
        p["apellido"],
        p["nombre"],
        p["fechaN"],
        p["localidad"],
        p["domicilio"],
        p["genero"],
        p["tipoD"],
        p["numero"],
        p["telefono"],
    )
    return redirect(url_for("listadoDocente"))

def actualizarDocente(dni):
    return None

def eliminarDocente(dni):
    return None

   