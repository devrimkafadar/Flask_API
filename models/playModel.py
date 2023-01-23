class Play():
    def __init__(self,playId,gameId,quarter,possessionTeamId,nonpossessionTeamId,playType,playType2,gameClock,down,distance,turnover,safety,offensiveYards,netYards,firstDown,scorePossession,scoreNonpossession,homeScorePre,visitingScorePre,homeScorePost,visitingScorePost):
        self.playId = playId
        self.gameId = gameId
        self.quarter = quarter
        self.possessionTeamId = possessionTeamId
        self.nonpossessionTeamId = nonpossessionTeamId
        self.playType = playType
        self.playType2 = playType2
        self.gameClock = gameClock
        self.down = down
        self.distance = distance
        self.turnover = turnover
        self.safety = safety
        self.offensiveYards = offensiveYards
        self.netYards = netYards
        self.firstDown= firstDown
        self.scorePossession = scorePossession
        self.scoreNonpossession = scoreNonpossession
        self.homeScorePre = homeScorePre
        self.visitingScorePre = visitingScorePre
        self.homeScorePost = homeScorePost
        self.visitingScorePost = visitingScorePost