from flask import Flask, Blueprint
from routers.games import games
from routers.interceptions import interceptions
from routers.passer import passer
from routers.players import players
from routers.plays import plays
from routers.receivers import receiver

index = Blueprint("index" , __name__, static_folder="static", template_folder="template")

index.register_blueprint(games , url_prefix="/games")
index.register_blueprint(interceptions , url_prefix="/interceptions")
index.register_blueprint(passer , url_prefix="/passer")
index.register_blueprint(players , url_prefix="/players")
index.register_blueprint(plays , url_prefix="/plays")
index.register_blueprint(receiver , url_prefix="/receivers")


@index.route("/")
def directRoute():
    return "<h1>index</h1>"