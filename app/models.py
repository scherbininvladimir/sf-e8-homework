from flask import Flask
import enum
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://skillfactory_user:skillfactory_password@localhost/skillfactory_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(300), unique=False, nullable=True)
    words_count = db.Column(db.Integer, unique=False, nullable=True)
    http_status_code = db.Column(db.Integer)

class TaskStatus (enum.Enum):
    NOT_STARTED = 1
    PENDING = 2
    FINISHED = 3
    FAILURE = 4

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(300), unique=False, nullable=True)
    timestamp = db.Column(db.DateTime())
    task_status = db.Column(db.Enum(TaskStatus))
    http_status = db.Column(db.Integer)
