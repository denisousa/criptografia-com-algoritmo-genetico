from flask import request, jsonify, render_template, send_file
from project.services.encrypt_service import  apply_encrypt
from project.services.descrypt_service import apply_descrypt
from project import app
from project.utils.operations_file import get_all_file_paths
import os


@app.route("/encrypt", methods=["POST"])
def encrypt():
    paths = get_all_file_paths(app.config['UPLOAD_FOLDER'])
    [os.remove(path) for path in paths]
    text_file = request.files["file"]
    filename = text_file.name 
    apply_encrypt(text_file)
    return send_file(
        f"{app.config['UPLOAD_FOLDER']}\\Encrypt.txt",
        as_attachment=True
    )


@app.route("/get_key", methods=["GET"])
def get_key():
    return send_file(
        f"{app.config['UPLOAD_FOLDER']}\\Key.txt",
        as_attachment=True
    )


@app.route("/descrypt", methods=["POST"])
def descrypt():
    encrypt_file = request.files["file"]
    keys_file = request.files["key"]
    apply_descrypt(encrypt_file, keys_file)
    return send_file(
        f"{app.config['UPLOAD_FOLDER']}\\Descrypt.txt", 
        as_attachment=True
    )
