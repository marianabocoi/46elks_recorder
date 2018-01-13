from flask import Flask

application = Flask(__name__, static_folder='wav')

from app import views
