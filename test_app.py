from flask import Flask, render_template, request
import os
from flask import redirect, url_for
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('index.html')

@app.route('/About.html')
def about():
    return render_template('About.html')

@app.route("/favicon.ico")
def favicon():
    return(url_for('static',filename='favicon.ico'))

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/send', methods = ['GET','POST'])
def send():
    if request.method == 'POST':
        age = request.form['age']
        return render_template('age.html',age=age)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
