from flask import Blueprint
from controllers.interceptions import *
from models.intModel import *

interceptions = Blueprint("interceptions" , __name__, static_folder="static", template_folder="template")

@interceptions.route("/", methods = ["GET"])
def showInts():
    return getIntLeadersJSON()

@interceptions.route('/deleteInt' , methods = ['POST'])
def delInt():
    id = request.form['intId']
    intDelete(id)
    return redirect('/stats/interceptions')

@interceptions.route('/addInt', methods = ['GET'])
def addIntPage():
    return render_template('addInt.html')

@interceptions.route('/updateInt', methods=['GET'])
def updateIntPage():
    return render_template('updateInt.html')


@interceptions.route('deleteInt' , methods = ['GET'])
def deleteIntPage():
    return render_template('deleteInt.html')

@interceptions.route('/addInt' , methods = ['POST'])
def addInt():
    intId = request.form["interceptionId"]
    playId = request.form["playId"]
    teamId = request.form["teamId"]
    playerId = request.form["playerId"]
    intPosition = request.form["intPosition"]
    intYards = request.form["intYards"]
    intTD = request.form["intTD"]

    interception = Interception(
        id = intId,
        playerId=playerId,
        playId = playId,
        teamId=teamId,
        intPosition=intPosition,
        intYards=intYards,
        intTd=intTD,
        int=1,
        intNull=0
    )
    dataToReturn = interceptionAdder(interception)
    return dataToReturn

@interceptions.route('/updateInt' , methods = ['POST'])
def updateInt():
    print('updateInt')
    intId = request.form["interceptionId"]
    playId = request.form["playId"]
    teamId = request.form["teamId"]
    playerId = request.form["playerId"]
    intPosition = request.form["intPosition"]
    intYards = request.form["intYards"]
    intTD = request.form["intTD"]

    formObject = Interception(
        id = intId,
        playerId=playerId,
        playId = playId,
        teamId=teamId,
        intPosition=intPosition,
        intYards=intYards,
        intTd=intTD,
        int=1,
        intNull=0
    )
    intList = getQuery(intId)
    previousObject = Interception(
        id = intList[0][0],
        playId = intList[0][1],
        teamId = intList[0][2],
        playerId = intList[0][3],
        intPosition = intList[0][4],
        int = intList[0][5],
        intYards = intList[0][6],
        intTd = intList[0][7],
        intNull = intList[0][8],
    )

    if formObject.id != "":
        previousObject.id = formObject.id
    if formObject.playId != "":
        previousObject.playId = formObject.playId
    if formObject.teamId != "":
        previousObject.teamId = formObject.teamId
    if formObject.playerId != "":
        previousObject.playerId = formObject.playerId
    if formObject.intPosition != "":
        previousObject.intPosition = formObject.intPosition
    if formObject.int != "":
        previousObject.int = formObject.int
    if formObject.intYards != "":
        previousObject.intYards = formObject.intYards
    if formObject.intTd != "":
        previousObject.intTd = formObject.intTd
    if formObject.intNull != "":
        previousObject.intNull = formObject.intNull
    
    return intUpdate(previousObject)
