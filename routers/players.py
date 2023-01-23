from flask import Blueprint
from controllers.players import *
from models.playerModel import *

players = Blueprint("players" , __name__, static_folder="static", template_folder="template")

@players.route("/" , methods = ['GET'])
def playersInfo():
    return generalPlayerInformation()

'''@players.route("/", methods = ['POST'])
def addPlayer():
    form_playerId = request.form["playerId"]
    form_firstName = request.form["firstName"]
    form_lastName = request.form["lastName"]
    form_fullName = request.form["fullName"]
    form_position = request.form["position"]
    form_nflId = request.form["nflId"]
    form_collage = request.form["collage"]
    form_height = request.form["height"]
    form_weight = request.form["weight"]
    form_dob = request.form["dob"]
    form_ageAtDraft = request.form["ageAtDraft"]
    form_profileURL = request.form["profileURL"]
    
    player = Player(
            playerId=form_playerId,
            nameFirst=form_firstName,
            nameLast=form_lastName,
            nameFull=form_fullName,
            position=form_position,
            nflId=form_nflId,
            college=form_collage,
            heightInches=form_height,
            weight=form_weight,
            dob=form_dob,
            ageAtDraft=form_ageAtDraft,
            playerProfileUrl=form_profileURL
        )
    dataToReturn = playerAdder(player)

    return dataToReturn'''


@players.route('/addPlayer' , methods=['GET'])
def addPlayerPage():
    return render_template('addPlayer.html')

@players.route('/deletePlayer' , methods=['GET'])
def delPlayerPage():
    return render_template('deletePlayer.html')

@players.route('/updatePlayer' , methods=['GET'])
def upPlayerPage():
    return render_template('updatePlayer.html')


@players.route('/deletePlayer', methods=['POST'])
def deletePlayer():
    id = request.form['playerId']
    playerDelete(id)
    return redirect('/stats/players')


@players.route('/updatePlayer' , methods = ['POST'])
def updatePlayer():
    form_playerId = request.form["playerId"]
    form_firstName = request.form["firstName"]
    form_lastName = request.form["lastName"]
    form_fullName = request.form["fullName"]
    form_position = request.form["position"]
    form_nflId = request.form["nflId"]
    form_collage = request.form["collage"]
    form_height = request.form["height"]
    form_weight = request.form["weight"]
    form_dob = request.form["dob"]
    form_ageAtDraft = request.form["ageAtDraft"]
    form_profileURL = request.form["profileURL"]

    formObject = Player(
            playerId=form_playerId,
            nameFirst=form_firstName,
            nameLast=form_lastName,
            nameFull=form_fullName,
            position=form_position,
            nflId=form_nflId,
            college=form_collage,
            heightInches=form_height,
            weight=form_weight,
            dob=form_dob,
            ageAtDraft=form_ageAtDraft,
            playerProfileUrl=form_profileURL
        )
    playerInfoList = getQuery(form_playerId)
    previousObject = Player(
        playerId=playerInfoList[0][0],
        nameFirst=playerInfoList[0][1],
        nameLast=playerInfoList[0][2],
        nameFull=playerInfoList[0][3],
        position=playerInfoList[0][4],
        nflId=playerInfoList[0][5],
        college=playerInfoList[0][6],
        heightInches=playerInfoList[0][7],
        weight=playerInfoList[0][8],
        dob=playerInfoList[0][9],
        ageAtDraft=playerInfoList[0][10],
        playerProfileUrl=playerInfoList[0][11],
    )
    if formObject.playerId != "":
        previousObject.playerId = formObject.playerId
    if formObject.nameFirst != "":
        previousObject.nameFirst = formObject.nameFirst
    if formObject.nameLast != "":
        previousObject.nameLast = formObject.nameLast
    if formObject.playerId != "":
        previousObject.nameFull = formObject.nameFull
    if formObject.position != "":
        previousObject.position = formObject.position
    if formObject.nflId != "":
        previousObject.nflId = formObject.nflId
    if formObject.college != "":
        previousObject.college = formObject.college
    if formObject.heightInches != "":
        previousObject.heightInches = formObject.heightInches
    if formObject.weight != "":
        previousObject.weight = formObject.weight
    if formObject.dob != "":
        previousObject.dob = formObject.dob
    if formObject.ageAtDraft != "":
        previousObject.ageAtDraft = formObject.ageAtDraft
    if formObject.playerProfileUrl != "":
        previousObject.playerProfileUrl = formObject.playerProfileUrl
    
    return playerUpdate(previousObject)

@players.route('/addPlayer',methods=['POST'])
def addPlayer():
    form_playerId = request.form["playerId"]
    form_firstName = request.form["firstName"]
    form_lastName = request.form["lastName"]
    form_fullName = request.form["fullName"]
    form_position = request.form["position"]
    form_nflId = request.form["nflId"]
    form_collage = request.form["collage"]
    form_height = request.form["height"]
    form_weight = request.form["weight"]
    form_dob = request.form["dob"]
    form_ageAtDraft = request.form["ageAtDraft"]
    form_profileURL = request.form["profileURL"]
    
    player = Player(
            playerId=form_playerId,
            nameFirst=form_firstName,
            nameLast=form_lastName,
            nameFull=form_fullName,
            position=form_position,
            nflId=form_nflId,
            college=form_collage,
            heightInches=form_height,
            weight=form_weight,
            dob=form_dob,
            ageAtDraft=form_ageAtDraft,
            playerProfileUrl=form_profileURL
        )
    playerAdder(player)

    return redirect('/stats/players')

