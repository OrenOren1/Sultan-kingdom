from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    if os.path.exists("Scores.txt") and (os.path.getsize("Scores.txt") != 0):
        with open('score.html.txt', 'r') as f:
            return render_template('content.html', score=f.read())
    else:
        # file error
        return render_template('error.html')

app.run()
