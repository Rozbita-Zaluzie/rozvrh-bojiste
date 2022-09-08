from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

from app.schedule import get_schedule



app = Flask(__name__, template_folder='templates')
CORS(app, support_credentials=True)



@app.route('/<classN>', methods=['GET'])
def schedule(classN):
    response = get_schedule(classN)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

