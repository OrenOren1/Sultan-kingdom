from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    if os.path.exists("../score/scores.txt") and (os.path.getsize("../score/scores.txt") != 0):
        with open('../score/scores.txt', 'r') as f:
            return render_template('score.html', score=f.read())
    else:
        # file error
        return render_template('error.html')

app.run()
