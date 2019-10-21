from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    
    # Creating app configs
    app.config.from_object(config_options[config_name])
    
    # Initializing the app
    # app = Flask(__name__,instance_relative_config = True)

    # Setting up configs
    # app.config.from_object(DevConfig)

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .main import views
    # from .main import errors

    return app