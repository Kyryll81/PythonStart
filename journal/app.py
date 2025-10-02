from flask import Flask
from flask_migrate import Migrate

from flasgger import Swagger

from config import Config

from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)


from db import db
db.init_app(app)

import routes
migrate = Migrate(app, db)
routes.init_routes(app, db)

swagger = Swagger(app)


if __name__ == "__main__":
    app.run(debug=True, port=5005)