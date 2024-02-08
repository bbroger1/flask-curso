from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

import os

load_dotenv(".env")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("TRACK_MODIFICATIONS")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["UPLOAD_FILES"] = os.getenv("UPLOAD_FILES")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = "login"
bcrypt = Bcrypt(app)

from app.routes import *
from app.models.user import *
from app.models.contact import *
from app.models.post import *
from app.models.comment import *
