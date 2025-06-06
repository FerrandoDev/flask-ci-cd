from flask import Flask
from .routes import article_routes


def create_app():
    app = Flask(__name__)  # Crée l'application Flask
    app.register_blueprint(article_routes)  # Ajoute les routes définies ailleurs
    return app
