from flask import Flask
from site_package.config import Config
from flask_mail import Mail

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from site_package.main.routes import main
    from site_package.orders_package.routes import order
    app.register_blueprint(main)
    app.register_blueprint(order)

    return app