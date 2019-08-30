# Basic request
from flask import Blueprint, render_template, current_app, flash, request

home_blueprint = Blueprint("home_view", "home_route")


@home_blueprint.route("/")
def index_page():

    return render_template("page/index.html")
