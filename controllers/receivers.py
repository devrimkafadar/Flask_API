from flask import Flask, render_template
from helpers.database.connectDatabase import *
from models.receiverModel import * 

int = Flask(__name__)

#select the player which has highest yards in each season 

mostYards = '''select distinct receiver.playerId, nameFull , totalYard , recposition from receiver join 
(select  playerId ,  SUM(recYards) as totalYard from receiver group by playerId)as A on A.playerId = receiver.playerId   join 
players on players.playerId  = receiver.playerId order by totalYard desc'''

#select the player who has fumble
fumble= '''select nameFull , teams.draftTeam ,recFumble, playId from receiver  
join teams on teams.teamId  =receiver.teamId 
join players on  receiver.playerId = players.playerId where recFumble !=0 ;  '''

#select the player who has the highest yard in each team 
teamYard= '''select distinct  receiver.playerId,players.nameFull , receiver.teamId ,teams.draftTeam, recYards   from  receiver  join 
  (select teamId , MAX(recYards) as TotalYards from receiver group by teamId) as A  on A.teamId = receiver.teamId and receiver.recYards=TotalYards
  join players on players.playerId = receiver.playerId 
  join teams on teams.teamId = receiver.teamId  order by recYards desc;
  '''

#addReceiver = '''INSERT INTO receiver (playId , teamId ,playerId,recPosition ,recYards ,rec, recYac,rec1down,recFumble,recPassDef,recPassInt,recEn) '''


def generalReceiverInformation():
    list= getRequestedDataFromDB(mostYards)
    list2=getRequestedDataFromDB(fumble)
    list3 = getRequestedDataFromDB(teamYard)
    return render_template('receiver.html' , seasonYard=list , fumbleList=list2 , teamYard=list3 )
"""
def getMostYardsJSON():
    list = getRequestedDataFromDB(mostYards)
    return render_template('receiver.html', datas=list)
def getFumbleJSON():
    list2 = getRequestedDataFromDB(fumble)
    return render_template('receiverFumble.html', datas= list2)
def getTeamYardJSON():
    list3= getRequestedDataFromDB(teamYard)
    return render_template('receiverTotalYards.html' , datas=list3)
"""
receiverAddingQuery=''' INSERT INTO receiver (receiverid,playid,teamid,playerid,recposition,recyards,rec,recyac,rec1down,recfumble,recpassdef,recpassint,recen)
values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

receiverDeletingQuery = "DELETE from receiver where receiverid = '{}'"

receiverFormQuery = "SELECT * from receiver where receiverid = '{}'"

receiverUpdateQuery = "UPDATE receiver SET playid = %s,teamid = %s,playerid = %s,recposition = %s,recyards = %s,rec = %s,recyac =%s,rec1down =%s,recfumble = %s,recpassdef = %s,recpassint = %s,recen = %s where receiverid = '{}'"

recUp = "update receiver set playid = '{}', teamid = '{}', playerid = '{}', recposition = '{}', recyards = {}, rec = {}, recyac = {}, rec1down={}, recfumble = {}, recpassdef = {}, recpassint={}, recen={} where receiverid = '{}'"

def getQuery(id):
    val = id
    theQ = receiverFormQuery.format(id)
    return  manipulateDBWithGivenData2(theQ ,val)
   

def receiverAdder(receiver):
    val = (
        receiver.receiverId, 
        receiver.playId,
        receiver.teamId, 
        receiver.playerId,
        receiver.recPosition, 
        receiver.recYards,
        receiver.rec,
        receiver.recYac,
        receiver.rec1Down,
        receiver.recFumble,
        receiver.recPassDef,
        receiver.recPassInt,
        receiver.recEn,
        
    )
    

    
    manipulateDBWithGivenData(receiverAddingQuery ,val)
    updatedReceiverData = getRequestedDataFromDB(mostYards)
    return updatedReceiverData 


def receiverUpdate(updateR):
    val = (
         
        updateR.playId,
        updateR.teamId, 
        updateR.playerId,
        updateR.recPosition, 
        updateR.recYards,
        updateR.rec,
        updateR.recYac,
        updateR.rec1Down,
        updateR.recFumble,
        updateR.recPassDef,
        updateR.recPassInt,
        updateR.recEn, 
    )
    
    print(val)

    #print(recUp)
    
    theQ = receiverUpdateQuery.format(
        updateR.receiverId
    )
    manipulateDBWithGivenData(theQ,val)
    updatedReceiverData = getRequestedDataFromDB(mostYards)
    return updatedReceiverData 

def receiverDelete(id):
    val = id
    theQ = receiverDeletingQuery.format(id)
    onlyQueryDBoperation(theQ)
    updatedReceiverData = getRequestedDataFromDB(mostYards)
    return updatedReceiverData