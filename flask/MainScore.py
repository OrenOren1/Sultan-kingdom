from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    if os.path.exists("../flask/scores.txt") and (os.path.getsize("../flask/scores.txt") != 0):
        with open('../flask/scores.txt', 'r') as f:
            return render_template('score.html', score=f.read())
    else:
        # file error
        return render_template('error.html')

app.run()
