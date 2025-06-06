import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "flaskuser"),
    "password": os.getenv("DB_PASSWORD", "flaskpass"),
    "database": os.getenv("DB_NAME", "flaskdb"),
    "port": int(os.getenv("DB_PORT", 3306))
}
