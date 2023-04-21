from flask import Flask, render_template
import logging
from flask_migrate import Migrate
from database import db
from config import BasicConfig
from routes.Personaje.personaje import appPersonaje
from werkzeug.exceptions import abort


app = Flask(__name__)

app.register_blueprint(appPersonaje)

app.config.from_object(BasicConfig)

db.init_app(app)
migrate = Migrate()
logging.basicConfig(level=logging.DEBUG, filename = "debug.log")
migrate.init_app(app,db)
