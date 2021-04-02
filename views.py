from flask import Flask, render_template, redirect
from app import app
from app import Content

@app.route('/')
@app.route('/index.html')
def home():
    frontpage_content = Content.query.all()[:3]
    return render_template('index.html', content=frontpage_content)

@app.route('/404.html')
def error():
    return render_template('404.html')

@app.route('/cv.html')
def cv():
    return render_template('cv.html')

@app.route('/hire-me.html')
def hire():
    return render_template('hire-me.html')

@app.route('/projects-grid-cards.html')
def projects():
    all_projects = Content.query.all()
    return render_template('projects-grid-cards.html', projects=all_projects)

@app.route('/<file_id>')
def image_display(file_id):
    data = Content.query.filter_by(id=file_id)[0]
    return render_template('display.html', data=data)