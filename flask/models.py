from app import db
class Personaje(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre_personaje = db.Column(db.String(250))
class Npc(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre_npc = db.Column(db.String(250))
class Ruta(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre_ruta = db.Column(db.String(250))
class Camino(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre_camino = db.Column(db.String(250))
class Mision(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre_mision = db.Column(db.String(250))