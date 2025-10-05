from flask import Flask
from flask_migrate import Migrate
from flasgger import Flasgger

from config import Config
from routes import routes
from models import db


app: Flask = Flask(__name__)
app.config.from_object(Config)
swagger: Flasgger = Flasgger(app)

db.init_app(app)
migrate: Migrate = Migrate(app, db)

app.register_blueprint(routes)

