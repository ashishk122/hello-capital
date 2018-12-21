import flask
from flask import Blueprint, Flask, g, jsonify
import time
from api import APPS

APP = Flask(__name__)

APP.register_blueprint(APPS)

