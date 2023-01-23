from flask import Flask, render_template
from helpers.database.connectDatabase import *
from models.playerModel import *

generalInfoQuery = '''
    select namefull, position, college, playerprofileurl
    from players order by namefull asc;
'''
collagePlayerDataQuery = '''
    select college, COUNT(*) as numberOfPlayers from players
    group by college order by numberOfPlayers desc
'''

playerAddingQuery = '''
    insert into players (playerid, namefirst, namelast, namefull,position, nflid, college, heightinches, weight, dob, ageatdraft, playerprofileurl)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
'''

playerUpdateQuery = "update players set namefirst = '{}', namelast = '{}', namefull = '{}', position = '{}', nflid = {}, college = '{}', heightinches = {}, weight={}, dob = '{}', ageatdraft = {}, playerprofileurl='{}' where playerid = '{}'"




def getQuery(id):
    theQ="select * from players where playerid = '{}'".format(id)
    liste = manipulateDBWithGivenData2(theQ,id)
    return liste

def playerUpdate(p):
    theQ = playerUpdateQuery.format(
        p.nameFirst,
        p.nameLast,
        p.nameFull,
        p.position,
        p.nflId,
        p.college,
        p.heightInches,
        p.weight,
        p.dob,
        p.ageAtDraft,
        p.playerProfileUrl,
        p.playerId
    )
    onlyQueryDBoperation(theQ)
    return redirect('/stats/players')



def generalPlayerInformation():
    generalInfo = getRequestedDataFromDB(generalInfoQuery)
    collageData = getRequestedDataFromDB(collagePlayerDataQuery)
    return render_template('playerInfo.html' , datas = generalInfo , collages=collageData)

def playerDelete(id):
    theQ = "delete from players where playerid ='{}'".format(id)
    onlyQueryDBoperation(theQ)
    redirect('/stats/players')


def playerAdder(player):
    val = (
        player.playerId,
        player.nameFirst,
        player.nameLast,
        player.nameFull,
        player.position,
        player.nflId,
        player.college,
        player.heightInches,
        player.weight,
        player.dob,
        player.ageAtDraft,
        player.playerProfileUrl
    )

    addGivenData(playerAddingQuery, val)
    updatedPlayerData = getRequestedDataFromDB(generalInfoQuery)
    updatedCollageData = getRequestedDataFromDB(collagePlayerDataQuery)
    return render_template('playerInfo.html' , datas = updatedPlayerData , collages=updatedCollageData)
