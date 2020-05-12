from flask import Flask
from site_package.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from site_package.main.routes import main

    app.register_blueprint(main)


    return app