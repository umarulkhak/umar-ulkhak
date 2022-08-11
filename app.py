from flask import Flask, render_template, flash, request, url_for, redirect, session
import os


IMAGE_FOLDER = os.path.join('static', 'img_pool')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template("home.html")



@app.route('/portofolio')
def about():

    return render_template("index.html")


app.run(debug=True)
