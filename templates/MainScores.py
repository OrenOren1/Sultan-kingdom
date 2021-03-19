from flask import render_template, Flask

# def score_server():

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home.html')
if __name__ == '__main__':
   app.run()