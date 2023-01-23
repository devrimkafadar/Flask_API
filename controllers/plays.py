from flask import Flask
from helpers.database.connectDatabase import *
import json
from models.playModel import * 

int = Flask(__name__)
number_of_results_by_quarter = '''
    select quarter, playtype2, Count(playtype2) from
    plays group by quarter, playtype2 order by 1,3;
    '''
max_avg_yards_getting_in_a_down_by_a_team = '''
    select tt.draftteam, down_glob, max_yards from teams as tt join (select
    D.possessionteamid, down_glob, max_yards from ( 
    (select B.down as down_glob, Max(avg_yards) as max_yards from
    (select draftteam, A.down, avg_yards from (select pl.possessionteamid, pl.down, Avg(pl.netyards)
    as avg_yards from plays as pl group by pl.possessionteamid, pl.down)
    as A join teams on teams.teamid = A.possessionteamid) as B group by B.down)
    as T1 join 
    (select pl.possessionteamid, pl.down, Avg(pl.netyards) as avg_yards from
    plays as pl group by pl.possessionteamid, pl.down)
    as T2 on down_glob = T2.down and T1.max_yards = T2.avg_yards) as D)
    as E on E.possessionteamid = tt.teamid;
    '''
most_yards_taken_on_distance_by_a_team = '''
       select draftteam, D.distance, m_net from (select B.distance, C.possessionteamid, m_net from
    (select distance, MAX(s_net2) as m_net from 
     (select distance, SUM(netyards) as s_net2, possessionteamid from 
      plays group by distance,possessionteamid) as A group by distance) as B join 
      (select distance, SUM(netyards) as s_net, possessionteamid from
       plays group by distance,possessionteamid) as C on 
       B.distance = C.distance and B.m_net = C.s_net) as D join teams on
       D.possessionteamid = teams.teamid order by 2;
    '''

playerAddingQuery=''' INSERT INTO plays (playId,gameId,quarter,possessionTeamId,nonpossessionTeamId,playType,playType2,gameClock,down,distance,turnover,safety,offensiveYards,netYards,firstDown,scorePossession,scoreNonpossession,homeScorePre,visitingScorePre,homeScorePost,visitingScorePost)
values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''


playsUpdateQuery = "UPDATE plays SET gameId = %s,quarter = %s,possessionTeamId = %s,nonpossessionTeamId = %s,playType = %s,playType2 = %s,gameClock = %s,down = %s,distance = %s,turnover = %s,safety = %s,offensiveYards = %s,netYards = %s,firstDown = %s,scorePossession = %s,scoreNonpossession = %s,homeScorePre = %s,visitingScorePre = %s,homeScorePost = %s,visitingScorePost = %s where playId = '{}'"

playsFormQuery = "SELECT * from plays where playId = '{}'"


playDelQ = "DELETE from plays where playId = '{}';"




results_by_quarter = getRequestedDataFromDB(number_of_results_by_quarter)
max_avg_yards_down = getRequestedDataFromDB(max_avg_yards_getting_in_a_down_by_a_team)
most_yards_by_distance = getRequestedDataFromDB(most_yards_taken_on_distance_by_a_team)

def getQuarterResultsJSON():
    return results_by_quarter


def getMaxAvgYardsDownJSON():
    return max_avg_yards_down

def getMostYardsDistanceJSON():
    return most_yards_by_distance

def getQuery(id):
    val = id
    theQ = playsFormQuery.format(id)
    liste = manipulateDBWithGivenData2(theQ ,val)
    return  liste
   


def playAdder(play):
    val = (
        play.playId, 
        play.gameId,
        play.quarter, 
        play.possessionTeamId,
        play.nonpossessionTeamId, 
        play.playType,
        play.playType2,
        play.gameClock,
        play.down,
        play.distance,
        play.turnover,
        play.safety,
        play.offensiveYards,
        play.netYards,
        play.firstDown,
        play.scorePossession,
        play.scoreNonpossession,
        play.homeScorePre,
        play.visitingScorePre,
        play.homeScorePost,
        play.visitingScorePost
    )
    
    manipulateDBWithGivenData(playerAddingQuery ,val)
    updatedPlayerData = getRequestedDataFromDB(most_yards_taken_on_distance_by_a_team)
    return updatedPlayerData


def playDelete(id):
    val = id 
    theQ = playDelQ.format(id)
    print(theQ)
    onlyQueryDBoperation(theQ)
    updatedPlayData= getRequestedDataFromDB(most_yards_taken_on_distance_by_a_team)
    return updatedPlayData


def playUpdate(play):
    val = (
        play.gameId,
        play.quarter, 
        play.possessionTeamId,
        play.nonpossessionTeamId, 
        play.playType,
        play.playType2,
        play.gameClock,
        play.down,
        play.distance,
        play.turnover,
        play.safety,
        play.offensiveYards,
        play.netYards,
        play.firstDown,
        play.scorePossession,
        play.scoreNonpossession,
        play.homeScorePre,
        play.visitingScorePre,
        play.homeScorePost,
        play.visitingScorePost
        
    )
    
    theQ = playsUpdateQuery.format(play.playId)
    manipulateDBWithGivenData(theQ ,val)
    updatedReceiverData = getRequestedDataFromDB(most_yards_taken_on_distance_by_a_team)
    return updatedReceiverData