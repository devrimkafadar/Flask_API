from flask import Blueprint
from controllers.passer import *
from flask import render_template ,Flask , redirect, url_for ,request
from models.passerModel import * 



passer = Blueprint("passer" , __name__, static_folder="static", template_folder="template")

@passer.route("/outcome_stat")
def showOutcomeStat():
    return getOutcomeStatJSON()

@passer.route("/average_pass")
def showAvgPass():
    return getAvgPassJSON()

@passer.route("/qb_wr_duos")
def showDuos():
    return getQbWrDuoJSON()

@passer.route('/', methods=['GET'])
def mainPasser():
    liste = getOutcomeStatJSON()
    liste2 = getAvgPassJSON()
    liste3 = getQbWrDuoJSON()
    return render_template('passer.html', pass_outcome = liste, avgPass = liste2,qbwrDuo = liste3)


@passer.route("/addPasser" , methods=["GET","POST"])
def passer_add_page():
    if request.method == "POST":
        form_passId = request.form["passId"]
        form_playerId = request.form["playerId"]
        form_teamId = request.form["teamId"]
        form_playId = request.form["playId"]
        form_passPosition = request.form["passPosition"]
        form_passOutcomes = request.form["passOutcomes"]
        form_passLength = request.form["passLength"]
        form_passComp= request.form["passComp"]
        form_passTd = request.form["passTd"]
        form_passInt= request.form["passInt"]
        form_passIntTd= request.form["passIntTd"]
        form_passSack = request.form["passSack"]
        form_passSackYds = request.form["passSackYds"]
        form_passHit = request.form["passHit"]
        form_passDef = request.form["passDef"]

                                
        new_passer = Passer(
                        form_passId,
                        form_playerId,
                        form_teamId,
                        form_playId,
                        form_passPosition,
                        form_passOutcomes,
                        form_passLength,
                        form_passComp,
                        form_passTd,
                        form_passInt,
                        form_passIntTd,
                        form_passSack,
                        form_passSackYds,
                        form_passHit,
                        form_passDef)
        passerAdder(new_passer)
        return redirect("/stats/passer")
    else:
        return render_template("addPasser.html")
                           
@passer.route("/deletePasser" , methods = ["GET" , "POST"])
def passer_delete(): 
    if request.method == 'POST':
        form_passId=request.form['passId']
        passerDelete(form_passId)
        return redirect("/stats/passer")
    else: 
        return render_template("deletePasser.html")



@passer.route("/updatePasser" , methods=["GET" , "POST"])
def passer_update():
    if request.method == "POST":
        form_passId = request.form["passId"]
        form_playerId = request.form["playerId"]
        form_teamId = request.form["teamId"]
        form_playId = request.form["playId"]
        form_passPosition = request.form["passPosition"]
        form_passOutcomes = request.form["passOutcomes"]
        form_passLength = request.form["passLength"]
        form_passComp= request.form["passComp"]
        form_passTd = request.form["passTd"]
        form_passInt= request.form["passInt"]
        form_passIntTd= request.form["passIntTd"]
        form_passSack = request.form["passSack"]
        form_passSackYds = request.form["passSackYds"]
        form_passHit = request.form["passHit"]
        form_passDef = request.form["passDef"]
        

        formObject = Passer(
                        form_passId,
                        form_playerId,
                        form_teamId,
                        form_playId,
                        form_passPosition,
                        form_passOutcomes,
                        form_passLength,
                        form_passComp,
                        form_passTd,
                        form_passInt,
                        form_passIntTd,
                        form_passSack,
                        form_passSackYds,
                        form_passHit,
                        form_passDef)



        gameList = getQuery(form_passId)
        print(gameList)
        oldRowObject = Passer(gameList[0][0],gameList [0][1],gameList[0][2],gameList[0][3],gameList[0][4],gameList[0][5],gameList[0][6],gameList[0][7],gameList[0][8],gameList[0][9],gameList[0][10],gameList[0][11],gameList[0][12],gameList[0][13],gameList[0][14])
        print(oldRowObject.passLength)
        if formObject.passId != "":
            oldRowObject.passId=formObject.passId
        if formObject.playerId  != "":
            oldRowObject.playerId=formObject.playerId
        if formObject.teamId != "":
            oldRowObject.teamId=formObject.teamId
        if formObject.playId  != "":
            oldRowObject.playId=formObject.playId
        if formObject.passPosition  != "":
            oldRowObject.passPosition=formObject.passPosition
        if formObject.passOutcomes  != "":
            oldRowObject.passOutcomes=formObject.passOutcomes
        if formObject.passLength  != "":
            oldRowObject.passLength=formObject.passLength
        if formObject.passComp  != "":
            oldRowObject.passComp=formObject.passComp
        if formObject.passTd != "":
            oldRowObject.passTd=formObject.passTd    
        if formObject.passInt  != "":
            oldRowObject.passInt=formObject.passInt
        if formObject.passIntTd  != "":
            oldRowObject.passIntTd=formObject.passIntTd    
        if formObject.passSack  != "":
            oldRowObject.passSack=formObject.passSack    
        if formObject.passSackYds  != "":
            oldRowObject.passSackYds=formObject.passSackYds   
        if formObject.passHit  != "":
            oldRowObject.passHit=formObject.passHit  
        if formObject.passDef  != "":
            oldRowObject.passDef=formObject.passDef              
        print(oldRowObject.passLength)
        passerUpdate(oldRowObject)
                
          
            
            
            
            
     
        return redirect("/stats/passer")
    else:
        return render_template("updatePasser.html")