from flask import Flask, render_template
from os import path

app = Flask(__name__, template_folder='templates')

@app.route("/")
def main(): 
	return render_template("index.html", name=None)

if __name__=="__main__":
    app.run(host="localhost", port=8080)
