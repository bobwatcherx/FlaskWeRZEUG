from flask import Flask,render_template,request
import json
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/generate/",methods=['POST'])
def generate():
	mypass = request.form.get('password')
	tohash = generate_password_hash(mypass)
	return render_template("index.html",tohash=tohash)


@app.route("/decrypt/",methods=['POST'])
def dec():
	mypass = request.form.get('password')
	textdec = request.form.get('textdec')
	result = check_password_hash(mypass,textdec)
	return render_template("index.html",result=result)




