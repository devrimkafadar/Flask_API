from flask import Flask, render_template
from helpers.database.connectDatabase import *
from models.intModel import *
    

intLeadersQuery = '''
    select namefull, position, COUNT(*) as interceptions 
    from interception left join players on players.playerid = interception.playerid
    group by namefull, position order by interceptions desc
'''
mostYardsAfterIntQuery = '''
    select namefull, position, draftteam, sum(intyards) as totalYardsReturned
    from (teams right join interception on teams.teamid = interception.teamid)
    left join players on players.playerid=interception.playerid
    group by namefull, position, draftteam order by totalYardsReturned desc;
'''
interceptionsInQuarters = '''
    select quarter, COUNT(*) as interceptions from interception left join plays 
    on plays.playid = interception.playid
    group by quarter order by interceptions desc;
'''

interceptionAddingQuery = '''
    insert into interception (interceptionid, playerid, playid, teamid ,intposition, intyards, inttd, int, intnull)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s);
'''
interceptionUpdateQuery = "update interception set playerid = '{}', playid = '{}', teamid = '{}', intposition = '{}', intyards = {}, inttd = {}, int = {}, intnull={} where interceptionid = '{}'"

def getQuery(id):
    selectionQuery = "select * from interception where interceptionid = '{}'".format(id)
    liste = manipulateDBWithGivenData2(selectionQuery,id)
    return liste

def intDelete(id):
    theQ = "delete from interception where interceptionid = '{}'".format(id)
    onlyQueryDBoperation(theQ)
    redirect('stats/interceptions')

def intUpdate(i):
    theQ = interceptionUpdateQuery.format(i.playerId,i.playId,i.teamId,i.intPosition,i.intYards,i.intTd,i.int,i.intNull,i.id)
    onlyQueryDBoperation(theQ)
    return redirect('/stats/interceptions')
    #return render_template('interceptions.html' , datas = intList, datasYDS = yardList, datasQuarter = quarterList)

def getIntLeadersJSON():
    intList = getRequestedDataFromDB(intLeadersQuery)
    yardList = getRequestedDataFromDB(mostYardsAfterIntQuery)
    quarterList = getRequestedDataFromDB(interceptionsInQuarters)
    return render_template('interceptions.html' , datas = intList, datasYDS = yardList, datasQuarter = quarterList)


def getIntYardsLeadersJSON():
    yardList = getRequestedDataFromDB(mostYardsAfterIntQuery)
    return render_template('interceptions_mostYds.html' , datas = yardList)

def getInterceptionsInQuartersJSON():
    quarterList = getRequestedDataFromDB(interceptionsInQuarters)
    return render_template('interceptions_intPerQ.html' , datas=quarterList)


def interceptionAdder(interception):
    val = (
        interception.id,
        interception.playerId,
        interception.playId,
        interception.teamId,
        interception.intPosition,
        interception.intYards,
        interception.intTd,
        interception.int,
        interception.intNull
    )
    addGivenData(interceptionAddingQuery, val)
    updatedIntList = getRequestedDataFromDB(intLeadersQuery)
    updatedYardList = getRequestedDataFromDB(mostYardsAfterIntQuery)
    updatedQuarterList = getRequestedDataFromDB(interceptionsInQuarters)
    return render_template('interceptions.html' , datas = updatedIntList, datasYDS = updatedYardList, datasQuarter = updatedQuarterList)