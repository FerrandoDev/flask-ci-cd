from flask import Blueprint, jsonify
import mysql.connector  # si tu l'as déjà installé plus tard

from config import DB_CONFIG

article_routes = Blueprint('article_routes', __name__)

@article_routes.route('/', methods=['GET'])
def index():
    return 'Bienvenue sur l\'API Flask !'

@article_routes.route('/articles', methods=['GET'])
def get_articles():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM articles")
    articles = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(articles)
