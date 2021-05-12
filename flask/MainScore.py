#!/usr/bin/env python
from flask import Flask, render_template
import os
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo:27017")

@app.route('/')
def todo():
    if os.path.exists("scores.txt") and (os.path.getsize("scores.txt") != 0):
        with open('scores.txt', 'r') as f:
            return render_template('score.html', score=f.read())
    elif os.path.exists("scores.txt") and (os.path.getsize("/src/scores.txt") != 0):
         with open('scores.txt', 'r') as f:
            return render_template('score.html', score=f.read()) 
    else:
        # file error
        return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9092), debug=True)
