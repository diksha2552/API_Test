from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:disk@2552@/Company_struct'
@app.route("/")

class Company_struct(db.Model):
    __tablename__ = 'details_empl'
    id_1 = db.column('id_1', db.Integer, primary_key = True)
    name = db.column('name', db.Unicode)
    doj = db.column('doj', db.Integer)
    parent_id = db.column('parent_id')

    def __init__(self, id_1, name, doj, parent_id):
        self.id_1 = id_1
        self.name = name
        self.doj = doj
        self.parent_id = parent_id

