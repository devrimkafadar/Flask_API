from flask import Flask ,render_template
from helpers.database.connectDatabase import *
from models.gameModel import *
import numpy as np

int = Flask(__name__)

#select the team which has highest score in each season 
mostScorer = '''select   T1.season , T4.Scores , T2.draftTeam as HomeTeam , T2.homeTeamFinalScore , T3.draftTeam as VisitorTeam ,T3.visitingTeamFinalScore from games as T1 Join 
 (select gameId ,homeTeamId , homeTeamFinalScore ,draftTeam from games join teams on games.homeTeamId =teams.teamId )as T2 on (T1.gameId = T2.gameId) Join 
 (select gameId , visitorteamId , visitingTeamFinalScore , teams.draftTeam from games join teams on games.visitorTeamId = teams.teamId ) as T3 on(T1.gameId = T3.gameId) join 
 (select gameId, season , Max(homeTeamFinalScore + visitingTeamFinalScore) as Scores from games group by season,gameId )as T4  on  (T1.gameId = T4.gameId)  join 
 (select season  , Max(homeTeamFinalScore + visitingTeamFinalScore) as scoreCount from games group by season) as T5 on T4.season =T5.season and T4.Scores = T5.scoreCount order by 1'''


mostWinner ='''select K.season, K.winningTeam, teams.draftTeam ,TotalWin from (select A.season, A.winningTeam, Count(A.winningTeam) as TotalWin from games as A group by A.season, A.winningteam) as K join 
(select B.season, MAX(TotalWin) as maxC from (select A.season, A.winningTeam, Count(A.winningTeam) as TotalWin from games as A group by A.season, A.winningTeam) as B group by B.season) as E on E.season = K.season and E.maxC = K.TotalWin
join teams on K.winningTeam = teams.teamId order by 1''' 


mostVisitor ='''select distinct games.visitorTeamId ,B.totalGoal ,teams.draftTeam from games join 
(select visitorTeamId , SUM(visitingTeamFinalScore) as totalGoal from games group by visitorTeamId)as B on B.visitorTeamId= games.visitorTeamId join teams on games.visitorTeamId = teams.teamId order by B.totalGoal desc'''


def generalGameInformation():
    list = getRequestedDataFromDB(mostScorer)
    list2 = getRequestedDataFromDB(mostWinner)
    list3= getRequestedDataFromDB(mostVisitor)
    return render_template('games.html', scorerList = list , winnerList =list2 , visitorList=list3)

    







gamesAddingQuery=''' INSERT INTO games (gameId,season,week,gameDate,gameTimeEastern,gameTimeLocal,homeTeamId,visitorTeamId,seasonType,weekNameAbbr,homeTeamFinalScore,visitingTeamFinalScore,winningTeam)
values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

gamesDeletingQuery = "DELETE from games where gameId ={}"

gamesFormQuery = "SELECT * from games where gameId = '{}'"

gamesUpdateQuery = "UPDATE games SET season = %s,week = %s,gameDate = %s,gameTimeEastern = %s,gameTimeLocal = %s,homeTeamId = %s,visitorTeamId = %s,seasonType = %s,weekNameAbbr = %s,homeTeamFinalScore = %s,visitingTeamFinalScore = %s,winningTeam = %s where gameId = '{}'"

gameDelQ = "DELETE from games where gameId = '{}'"

def gameAdder(games):
    val = (
        games.gameId ,
        games.season, 
        games.week,
        games.gameDate, 
        games.gameTimeEastern,
        games.gameTimeLocal, 
        games.homeTeamId,
        games.visitorTeamId,
        games.seasonType,
        games.weekNameAbbr,
        games.homeTeamFinalScore,
        games.visitingTeamFinalScore,
        games.winningTeam
        
    )


    
    
    addGivenData(gamesAddingQuery ,val)
    updatedReceiverData = getRequestedDataFromDB(mostScorer)
    return updatedReceiverData 


def getQuery(id):
    val = id
    theQ = gamesFormQuery.format(id)
    liste = manipulateDBWithGivenData2(theQ ,val)
    return  liste
   

def gameDelete(id):
    val = id 
    theQ = gameDelQ.format(id)
    print(theQ)
    manipulateDBWithGivenData(theQ,val)
    updatedReceiverData= getRequestedDataFromDB(mostScorer)
    return updatedReceiverData

def gamesUpdate(games):
    val = (
         
        games.season, 
        games.week,
        games.gameDate, 
        games.gameTimeEastern,
        games.gameTimeLocal, 
        games.homeTeamId,
        games.visitorTeamId,
        games.seasonType,
        games.weekNameAbbr,
        games.homeTeamFinalScore,
        games.visitingTeamFinalScore,
        games.winningTeam,
        
    )
    
    theQ = gamesUpdateQuery.format(games.gameId)
    manipulateDBWithGivenData(theQ ,val)
    updatedReceiverData = getRequestedDataFromDB(mostScorer)
    return updatedReceiverData