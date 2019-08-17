import os
import logging
import socket
from flask import Flask, jsonify
import pandas as pd
import numpy as np
import tensorflow as tl
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.datasets import fashion_mnist

HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS', 'localhost')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME', 'flask')
IP = os.environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8080))
HOME_DIR = os.environ.get('OPENSHIFT_HOMEDIR', os.getcwd())

log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'host_name': HOST_NAME,
        'app_name': APP_NAME,
        'ip': IP,
        'port': PORT,
        'home_dir': HOME_DIR,
        'host': socket.gethostname()
    })