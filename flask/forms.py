from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PersonajeForm(FlaskForm):
    nombre_personaje = StringField('Nombre', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class NpcForm(FlaskForm):
    nombre_npc = StringField('Nombre', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
    
class RutaForm(FlaskForm):
    nombre_ruta = StringField('Nombre', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
    
class CaminoForm(FlaskForm):
    nombre_camino = StringField('Nombre', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
    
class MisionForm(FlaskForm):
    nombre_mision = StringField('Nombre', validators=[DataRequired()])
    enviar = SubmitField('Enviar')