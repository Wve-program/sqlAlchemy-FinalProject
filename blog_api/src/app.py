from flask import Flask

from .config import app_config
from .models import db, bcrypt 

def create_app(env_name):
  """
  Create app
  """
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  
  bcrypt.init_app(app) # add this line

  db.init_app(app) # add this line

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your first endpoint is workin'

  return app
