import os

from flask import Flask

from crow.extensions import (
  db,
)

def create_app(config_filename="flask.cfg"):
  """Create Flask application factories."""

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_pyfile(config_filename)

  initialize_extensions(app)
  register_blueprints(app)

  return app

def initialize_extensions(app):
  """Initializing Flask extensions."""

  db.init_app(app)

  return None

def register_blueprints(app):
  """Registering Flask blueprints."""

  from crow.main.views import main
  from crow.api.api import api

  app.register_blueprint(main)
  app.register_blueprint(api)
  
  return None