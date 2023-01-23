from flask import Flask
from helpers.database.connectDatabase import *
import json
from models.passerModel import * 

int = Flask(__name__)
pass_outcome_stat = '''
    select players.namefirst, players.namelast, pasc, A.passoutcomes from (
    select passer.playerid, Count(passoutcomes) as pasc, passoutcomes from
    passer group by passer.playerid, passoutcomes)
    as A join players on players.playerid = A.playerid order by 1,3;
    '''
average_complete_pass_yards = '''
    select players.playerid, namefirst, namelast, avg_pass from players join
    (select passer.playerid, Avg(passlength) as Avg_pass from passer
    where passoutcomes = 'complete' group by passer.playerid, passoutcomes)
    as PASS on players.playerid = PASS.playerid order by 4 desc;
    '''
qb_wr_duos = '''
    select Qbfirstname, Qblastname, WRfirstname, WRlastname, passlen1, ptd1 from
    ((select QBid, WRidt, (Pl.namefirst)as QBfirstname, (Pl.namelast)
    as Qblastname, passlen1, ptd1 from (select Pa.playerid as QBid, R.playerid
    as WRidt, Sum(Pa.passlength) as passlen1, Sum(Pa.passtd) as ptd1 from passer
    as Pa join receiver R on R.playid = Pa.playid group by Pa.playerid, R.playerid)
    as A join players as Pl on Pl.playerid = Qbid) as T1 join
    (select WRid, Qbidt, (Pl.namefirst) as WRfirstname, (Pl.namelast)
    as WRlastname, passlen2, ptd2 from (select R.playerid as WRid,Pa.playerid
    as QBidt, Sum(Pa.passlength) as passlen2, Sum(Pa.passtd) as ptd2 from passer
    as Pa join receiver R on R.playid = Pa.playid group by Pa.playerid, R.playerid)
    as A join players as Pl on Pl.playerid = WRid) as T2
    on WRidt = WRid and Qbidt = Qbid) as X;
    '''


passerAddingQuery=''' INSERT INTO passer (passId,playerId,teamId,playId,passPosition,passOutcomes,passLength,passComp,passTd,passInt,passIntTd,passSack,passSackYds,passHit,passDef)
values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''



passerUpdateQuery = "UPDATE passer SET playid = '{}', teamid='{}', playerid='{}', passPosition = '{}', passOutcomes = '{}',passLength = {},passComp = {},passTd = {},passInt = {},passIntTd = {},passSack = {},passSackYds = {},passHit = {},passDef ={} where passId = '{}';"
#passerUpdateQuery = '''UPDATE passer SET passLength = {} where passId = '{}';'''

passerFormQuery = "SELECT * from passer where passId = '{}';"


passerDelQ = "DELETE from passer where passId = '{}'"





outcome_stat_list = getRequestedDataFromDB(pass_outcome_stat)
avg_pass_list = getRequestedDataFromDB(average_complete_pass_yards)
qb_wr_duo_list = getRequestedDataFromDB(qb_wr_duos)

def getOutcomeStatJSON():
    return outcome_stat_list


def getAvgPassJSON():
    return avg_pass_list

def getQbWrDuoJSON():
    return qb_wr_duo_list


def getQuery(id):
    val = id
    theQ = passerFormQuery.format(id)
    liste = manipulateDBWithGivenData2(theQ ,val)
    return  liste
   
def passerDelete(id):
    val = id 
    theQ = passerDelQ.format(id)
    print(theQ)
    onlyQueryDBoperation(theQ)
    updatedPasserData= getRequestedDataFromDB(pass_outcome_stat)
    return updatedPasserData


def passerAdder(passer):
    val = (
        passer.passId, 
        passer.playerId,
        passer.teamId, 
        passer.playId,
        passer.passPosition, 
        passer.passOutcomes,
        passer.passLength,
        passer.passComp,
        passer.passTd,
        passer.passInt,
        passer.passIntTd,
        passer.passSack,
        passer.passSackYds,
        passer.passHit,
        passer.passDef
    )
    

    
    manipulateDBWithGivenData(passerAddingQuery ,val)
    updatedPasserData = getRequestedDataFromDB(average_complete_pass_yards)
    return updatedPasserData 


def passerUpdate(passer):
    val = (
        passer.playerId,
        passer.teamId, 
        passer.playId,
        passer.passPosition, 
        passer.passOutcomes,
        passer.passLength,
        passer.passComp,
        passer.passTd,
        passer.passInt,
        passer.passIntTd,
        passer.passSack,
        passer.passSackYds,
        passer.passHit,
        passer.passDef,
        passer.passId  
    )
    
    theQ = passerUpdateQuery.format(
        passer.playerId,
        passer.teamId, 
        passer.playId,
        passer.passPosition, 
        passer.passOutcomes,
        passer.passLength,
        passer.passComp,
        passer.passTd,
        passer.passInt,
        passer.passIntTd,
        passer.passSack,
        passer.passSackYds,
        passer.passHit,
        passer.passDef,
        passer.passId)
    print(theQ)
    onlyQueryDBoperation(theQ)
    updatedReceiverData = getRequestedDataFromDB(pass_outcome_stat)
    return updatedReceiverData