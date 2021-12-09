from datetime import datetime
import html
from flask import Flask, render_template
from process_jeopardy import info, header

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", header=header, info=info.replace('\n', '<br>'))

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)