from flask import Blueprint, render_template, jsonify
import socket, psutil

bp = Blueprint("main", __name__)

@bp.route("/")
def dashboard():
    return render_template("dashboard.html", cpu=psutil.cpu_percent(), mem=psutil.virtual_memory())

@bp.route("/health")
def health():
    return jsonify({"status": "ok", "host": socket.gethostname()})
