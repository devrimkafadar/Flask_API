class Game:
    def __init__(self,  gameId, season, week, gameDate, gameTimeEastern, gameTimeLocal, homeTeamId, visitorTeamId, seasonType, weekNameAbbr, homeTeamFinalScore, visitingTeamFinalScore, winningTeam):
    
        self.gameId = gameId
        self.season = season
        self.week = week
        self.gameDate = gameDate
        self.gameTimeEastern = gameTimeEastern
        self.gameTimeLocal = gameTimeLocal
        self.homeTeamId = homeTeamId
        self.visitorTeamId = visitorTeamId
        self.seasonType = seasonType
        self.weekNameAbbr = weekNameAbbr
        self.homeTeamFinalScore = homeTeamFinalScore
        self.visitingTeamFinalScore = visitingTeamFinalScore
        self.winningTeam= winningTeam