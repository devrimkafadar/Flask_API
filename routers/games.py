from flask import Blueprint
from controllers.games import *
from flask import render_template ,Flask , redirect, url_for ,request
from models.gameModel import *
import numpy as np


games = Blueprint("games" , __name__, static_folder="static", template_folder="template")

@games.route("/", methods=["GET"])
def showGeneralGameInformation():
    return generalGameInformation()


@games.route("/addGame" , methods=["GET" , "POST"])
def game_add_page():
    if request.method == "POST":
       form_gameId = request.form["gameId"]
       form_season = request.form["season"]
       form_week = request.form["week"]
       form_gameDate = request.form["gameDate"]
       form_gameTimeEastern = request.form["gameTimeEastern"]
       form_gameTimeLocal = request.form["gameTimeLocal"]
       form_homeTeamId = request.form["homeTeamId"]
       form_visitorTeamId = request.form["visitorTeamId"]
       form_seasonType = request.form["seasonType"]
       form_weekNameAbbr= request.form["weekNameAbbr"]
       form_homeTeamFinalScore = request.form["homeTeamFinalScore"]
       form_visitingTeamFinalScore = request.form["visitingTeamFinalScore"]
       form_winningTeam = request.form["winningTeam"]
       
       new_game = Game(form_gameId,form_season,form_week,form_gameDate,form_gameTimeEastern,form_gameTimeLocal,form_homeTeamId,form_visitorTeamId,form_seasonType,form_weekNameAbbr,form_homeTeamFinalScore,form_visitingTeamFinalScore,form_winningTeam)
       gameAdder(new_game)
       return redirect("/stats/games")
    else :
       return render_template("addGame.html")
       
@games.route("/deleteGame" , methods = ["GET" , "POST"])
def game_delete(): 
    if request.method == 'POST':
        form_gameId=request.form['gameId']
        gameDelete(form_gameId)
        return redirect("/stats/games")
    else: 
        return render_template("deleteGame.html")
        
@games.route("/updateGame" , methods=["GET" , "POST"])
def game_update():
    if request.method == "POST":
        form_gameId = request.form["gameId"]
        form_season = request.form["season"]
        form_week = request.form["week"]
        form_gameDate = request.form["gameDate"]
        form_gameTimeEastern = request.form["gameTimeEastern"]
        form_gameTimeLocal = request.form["gameTimeLocal"]
        form_homeTeamId = request.form["homeTeamId"]
        form_visitorTeamId = request.form["visitorTeamId"]
        form_seasonType = request.form["seasonType"]
        form_weekNameAbbr= request.form["weekNameAbbr"]
        form_homeTeamFinalScore = request.form["homeTeamFinalScore"]
        form_visitingTeamFinalScore = request.form["visitingTeamFinalScore"]
        form_winningTeam = request.form["winningTeam"]
        
        formObject = Game(form_gameId,form_season,form_week,form_gameDate,form_gameTimeEastern,form_gameTimeLocal,form_homeTeamId,form_visitorTeamId,form_seasonType,form_weekNameAbbr,form_homeTeamFinalScore,form_visitingTeamFinalScore,form_winningTeam)
        gameList = getQuery(form_gameId)
        oldRowObject = Game(gameList[0][0],gameList [0][1],gameList[0][2],gameList[0][3],gameList[0][4],gameList[0][5],gameList[0][6],gameList[0][7],gameList[0][8],gameList[0][9],gameList[0][10],gameList[0][11],gameList[0][12])

        if formObject.gameId  != "":
            oldRowObject.gameId=formObject.gameId
        if formObject.season  != "":
            oldRowObject.season=formObject.season
        if formObject.week != "":
            oldRowObject.week=formObject.week
        if formObject.gameDate  != "":
            oldRowObject.gameDate=formObject.gameDate
        if formObject.gameTimeEastern  != "":
            oldRowObject.gameTimeEastern=formObject.gameTimeEastern
        if formObject.gameTimeLocal  != "":
            oldRowObject.gameTimeLocal=formObject.gameTimeLocal
        if formObject.homeTeamId  != "":
            oldRowObject.homeTeamId=formObject.homeTeamId
        if formObject.visitorTeamId  != "":
            oldRowObject.visitorTeamId=formObject.visitorTeamId
        if formObject.seasonType != "":
            oldRowObject.seasonType=formObject.seasonType    
        if formObject.weekNameAbbr  != "":
            oldRowObject.weekNameAbbr=formObject.weekNameAbbr
        if formObject.homeTeamFinalScore  != "":
            oldRowObject.homeTeamFinalScore=formObject.homeTeamFinalScore    
        if formObject.visitingTeamFinalScore  != "":
            oldRowObject.visitingTeamFinalScore=formObject.visitingTeamFinalScore    
        if formObject.winningTeam  != "":
            oldRowObject.winningTeam=formObject.winningTeam   
        
        gamesUpdate(oldRowObject)
                
          
            
            
            
            
     
        return redirect("/stats/games")
    else:
        return render_template("updateGame.html")