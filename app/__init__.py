from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

# Initializing the app
app = Flask(__name__,instance_relative_config = True)

# Setting up configs
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap.init_app(app)

from .main import views