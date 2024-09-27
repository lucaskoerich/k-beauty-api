from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from models import db
from routes.auth import auth_bp
from routes.clients import clients_bp
from routes.procedures import procedures_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SALT'] = os.getenv('SALT')
app.config.from_object('config.Config')

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(clients_bp)
app.register_blueprint(procedures_bp)

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1']
    
    app.run(host=host, port=port, debug=debug)
