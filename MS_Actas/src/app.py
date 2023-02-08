from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/ActasReunionBD'
mongo = PyMongo(app)


@app.route('/actas/<id>', methods=['GET'])

