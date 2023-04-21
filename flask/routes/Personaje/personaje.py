from flask import Blueprint, request, jsonify,render_template,url_for,redirect
from models import Personaje
from forms import PersonajeForm
from app import db
from werkzeug.exceptions import abort

appPersonaje = Blueprint('appPersonaje',__name__,template_folder="templates")

@appPersonaje.route('/')
@appPersonaje.route('/index')
@appPersonaje.route('/personaje')
def inicio():
    personajes = Personaje.query.all()
    totalDepersonajes = Personaje.query.count()
    return render_template('index.html', personajes = personajes, totalDepersonajes = totalDepersonajes)

@appPersonaje.route('/agregar', methods = ["GET","POST"])
def agregar(): 
    personaje = Personaje()
    personajeForm = PersonajeForm(obj=personaje)
    if request.method == "POST":
        if personajeForm.validate_on_submit():
            personajeForm.populate_obj(personaje)
            db.session.add(personaje)
            db.session.commit()
            return redirect(url_for('appPersonaje.inicio'))
    return render_template('agregar.html', forma = personajeForm)

@appPersonaje.route('/editar/<int:id>',methods= ["GET","POST"])
def editar(id):
    personaje = Personaje.query.get_or_404(id)
    personajeForm = PersonajeForm(obj=personaje)
    if request.method == "POST":
        if personajeForm.validate_on_submit():
            personajeForm.populate_obj(personaje)
            db.session.commit()
            return redirect(url_for('appPersonaje.inicio'))
    return render_template('editar.html',forma=personajeForm)

@appPersonaje.route('/eliminar/<int:id>')
def eliminar(id):
    personaje = Personaje.query.get_or_404(id)
    db.session.delete(personaje)
    db.session.commit()
    return redirect(url_for('appPersonaje.inicio'))

@appPersonaje.route('/salir')
def salir():
    return abort(404)
@appPersonaje.errorhandler(404)
def paginaNoEncontrada(error):
      return render_template('error404.html', error=error),404