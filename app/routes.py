from flask import Blueprint, request, render_template

main_routes = Blueprint('main', __name__)

# jednostavna in-memory lista
logs = []

@main_routes.route("/", methods=["GET"])
def index():
    return render_template("index.html", logs=logs)

@main_routes.route("/add-log", methods=["POST"])
def add_log():
    log_entry = request.form.get("log")
    if log_entry:
        logs.append(log_entry)
    return render_template("index.html", logs=logs)