from flask import Flask
import os


app = Flask(__name__)
UPLOAD_FOLDER = f"{os.path.dirname(os.path.abspath(__file__))}\\temp"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from .controllers import main_controller
