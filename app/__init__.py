from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5001", allow_headers="*", supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'  
db = SQLAlchemy(app)
migrate = Migrate(app, db) 

from app import routes
