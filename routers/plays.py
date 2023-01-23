from flask import Blueprint
from controllers.plays import *
from models.playModel import * 
from flask import render_template ,Flask , redirect, url_for ,request


plays = Blueprint("plays" , __name__, static_folder="static", template_folder="template")

@plays.route("/results_by_quarter")
def showQuarterResults():
    return getQuarterResultsJSON()

@plays.route("/max_avg_yards_by_down")
def showMaxAvgYards():
    return getMaxAvgYardsDownJSON()

@plays.route("/most_yards_by_distance")
def showMostYardsDistance():
    return getMostYardsDistanceJSON()

@plays.route('/', methods=['GET'])
def mainPasser():
    liste = getQuarterResultsJSON()
    liste2 = getMaxAvgYardsDownJSON()
    liste3 = getMostYardsDistanceJSON()
    return render_template('plays.html', results_by_quarter = liste, maxavgYards = liste2,most_yards_distance = liste3)


       
@plays.route("/deletePlay" , methods = ["GET" , "POST"])
def play_delete(): 
    if request.method == 'POST':
        form_playId=request.form['playId']
        playDelete(form_playId)
        return redirect("/stats/plays")
    else: 
        return render_template("deletePlay.html")
        


@plays.route("/addPlay" , methods=["GET","POST"])
def palys_add_page():
    if request.method == "POST":
        form_playId = request.form["playId"]
        form_gameId = request.form["gameId"]
        form_quarter = request.form["quarter"]
        form_possessionTeamId = request.form["possessionTeamId"]
        form_nonpossessionTeamId = request.form["nonpossessionTeamId"]
        form_playType = request.form["playType"]
        form_playType2 = request.form["playType2"]
        form_gameClock = request.form["gameClock"]
        form_down= request.form["down"]
        form_distance = request.form["distance"]
        form_turnover= request.form["turnover"]
        form_safety= request.form["safety"]
        form_offensiveYards= request.form["offensiveYards"]
        form_netYards = request.form["netYards"]
        form_firstDown = request.form["firstDown"]
        form_scorePossession = request.form["scorePossession"]
        form_scoreNonpossession = request.form["scoreNonpossession"]
        form_homeScorePre= request.form["homeScorePre"]
        form_visitingScorePre = request.form["visitingScorePre"]
        form_homeScorePost = request.form["homeScorePost"]
        form_visitingScorePost = request.form["visitingScorePost"]


                                
        new_play = Play(
                        form_playId,
                        form_gameId,
                        form_quarter,
                        form_possessionTeamId,
                        form_nonpossessionTeamId,
                        form_playType,
                        form_playType2,
                        form_gameClock,
                        form_down,
                        form_distance,
                        form_turnover,
                        form_safety,
                        form_offensiveYards,
                        form_netYards,
                        form_firstDown,
                        form_scorePossession,
                        form_scoreNonpossession,
                        form_homeScorePre,
                        form_visitingScorePre,
                        form_homeScorePost,
                        form_visitingScorePost)
        playAdder(new_play)
        return redirect("/stats/plays")
    else:
        return render_template("addPlay.html")




        
@plays.route("/updatePlay" , methods=["GET" , "POST"])
def play_update():
    if request.method == "POST":
        form_playId = request.form["playId"]
        form_gameId = request.form["gameId"]
        form_quarter = request.form["quarter"]
        form_possessionTeamId = request.form["possessionTeamId"]
        form_nonpossessionTeamId = request.form["nonpossessionTeamId"]
        form_playType = request.form["playType"]
        form_playType2 = request.form["playType2"]
        form_gameClock = request.form["gameClock"]
        form_down= request.form["down"]
        form_distance = request.form["distance"]
        form_turnover= request.form["turnover"]
        form_safety= request.form["safety"]
        form_offensiveYards= request.form["offensiveYards"]
        form_netYards = request.form["netYards"]
        form_firstDown = request.form["firstDown"]
        form_scorePossession = request.form["scorePossession"]
        form_scoreNonpossession = request.form["scoreNonpossession"]
        form_homeScorePre= request.form["homeScorePre"]
        form_visitingScorePre = request.form["visitingScorePre"]
        form_homeScorePost = request.form["homeScorePost"]
        form_visitingScorePost = request.form["visitingScorePost"]


                               
        formObject = Play(
                        form_playId,
                        form_gameId,
                        form_quarter,
                        form_possessionTeamId,
                        form_nonpossessionTeamId,
                        form_playType,
                        form_playType2,
                        form_gameClock,
                        form_down,
                        form_distance,
                        form_turnover,
                        form_safety,
                        form_offensiveYards,
                        form_netYards,
                        form_firstDown,
                        form_scorePossession,
                        form_scoreNonpossession,
                        form_homeScorePre,
                        form_visitingScorePre,
                        form_homeScorePost,
                        form_visitingScorePost)
        
        playList = getQuery(form_playId)
        
        oldRowObject = Play(
                        playList[0][0],
                        playList[0][1],
                        playList[0][2],
                        playList[0][3],
                        playList[0][4],
                        playList[0][5],
                        playList[0][6],
                        playList[0][7],
                        playList[0][8],
                        playList[0][9],
                        playList[0][10],
                        playList[0][11],
                        playList[0][12],
                        playList[0][13],
                        playList[0][14],
                        playList[0][15],
                        playList[0][16],
                        playList[0][17],
                        playList[0][18],
                        playList[0][19],
                        playList[0][20])


        if formObject.playId  != "":
            oldRowObject.playId=formObject.playId
        if formObject.gameId  != "":
            oldRowObject.gameId=formObject.gameId
        if formObject.quarter != "":
            oldRowObject.quarter=formObject.quarter
        if formObject.possessionTeamId  != "":
            oldRowObject.possessionTeamId=formObject.possessionTeamId
        if formObject.nonpossessionTeamId  != "":
            oldRowObject.nonpossessionTeamId=formObject.nonpossessionTeamId
        if formObject.playType  != "":
            oldRowObject.playType=formObject.playType
        if formObject.playType2  != "":
            oldRowObject.playType2=formObject.playType2
        if formObject.gameClock  != "":
            oldRowObject.gameClock=formObject.gameClock
        if formObject.down != "":
            oldRowObject.down=formObject.down    
        if formObject.distance  != "":
            oldRowObject.distance=formObject.distance
        if formObject.turnover  != "":
            oldRowObject.turnover=formObject.turnover    
        if formObject.safety  != "":
            oldRowObject.safety=formObject.safety    
        if formObject.offensiveYards  != "":
            oldRowObject.offensiveYards=formObject.offensiveYards
        if formObject.netYards  != "":
            oldRowObject.netYards=formObject.netYards  
        if formObject.firstDown  != "":
            oldRowObject.firstDown=formObject.firstDown
        if formObject.scorePossession  != "":
            oldRowObject.scorePossession=formObject.scorePossession
        if formObject.scoreNonpossession  != "":
            oldRowObject.scoreNonpossession=formObject.scoreNonpossession
        if formObject.homeScorePre  != "":
            oldRowObject.homeScorePre=formObject.homeScorePre
        if formObject.visitingScorePre  != "":
            oldRowObject.visitingScorePre=formObject.visitingScorePre
        if formObject.homeScorePost  != "":
            oldRowObject.homeScorePost=formObject.homeScorePost
        if formObject.visitingScorePost  != "":
            oldRowObject.visitingScorePost=formObject.visitingScorePost

        playUpdate(oldRowObject)
                
          
            
            
            
            
     
        return redirect("/stats/plays")
    else:
        return render_template("updatePlay.html")