from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
app.secret_key = 'somesecretkey'
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column('content_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    describtion = db.Column(db.String(200), nullable=False)
    image = db.Column(db.Text, nullable=False, default='default image path')

    def __repr__(self):
        return 'Project: ' + str(self.id)

import views