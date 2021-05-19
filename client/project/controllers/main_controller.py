from flask import request, jsonify, render_template, send_from_directory, url_for, redirect
from project import app


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/descrypt", methods=["GET"])
def descrypt():
    return render_template("descrypt.html")