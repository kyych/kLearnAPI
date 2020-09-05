from run import app
from flask import jsonify


@app.route('/')
def index():
    return jsonify({'message': "kLearnAPI, to authenticate do a post to /login please."})
