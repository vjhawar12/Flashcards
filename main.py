from flask import Flask 

files = ["home.html", "inner.html", "error.html"]

def getPage(fileName): 
	file = ""
	if fileName in files: 
		with open(fileName) as f: 
			file = f.read() 
		return file
	return getPage("error.html")

app = Flask(__name__)

@app.route("/")
def main(): 
	return getPage("home.html")

@app.route("/inner")
def next(): 
	return getPage("inner.html")