class PaperBot:
    def __init__(self):
        self.roundCount = 0
        self.dynamiteRemaining = 100
        self.opponentDynamiteRemaining = 100
        self.drawCount = 0
        self.OpponentChoiceTracker = {}
        for i in range(0, 10):
            self.OpponentChoiceTracker[i] = []
        self.OpponentResponseTracker = {'R':[], 'P':[], 'S':[], 'D':[], 'W':[]}
        self.Response = {'R':'P', 'P':'S', 'S':'R', 'D':'W', 'W':'P'}
        pass


    def make_move(self, gamestate):
        roundList = gamestate['rounds']
        roundList.reverse()

        if self.roundCount == 0 or 1:
            self.roundCount += 1
            return self.randomChoice(gamestate)

        self.roundCount += 1

        previousRound = roundList[0]
        nextPreviousRound = roundList[1]

        self.UpdateTrackers(previousRound, nextPreviousRound)
        self.drawCount = self.setDrawCount(roundList)

        if self.roundCount < 70 or self.roundCount % 10 == 0:
            choice = self.randomChoice(gamestate)
        else:
            self.getBestChoice(previousRound)

        return choice

    def getBestChoice(self, previousRound):
        choice = self.Response[self.SelectLikelyResponce(previousRound)]

        # take into account dynamite limit
        if choice == 'W' and self.opponentDynamiteRemaining == 0:
            choice = 'D'
        if choice == 'D' and self.dynamiteRemaining == 0:
            choice = 'R'

        return choice

    def UpdateTrackers(self, previousRound, nextPreviousRound):
        # track what opponent did in response to draw
        self.OpponentChoiceTracker[self.drawCount].append(previousRound['p2'])
        self.OpponentResponseTracker[nextPreviousRound['p1']].append(previousRound['p2'])
        if previousRound['p1'] == 'D':
            self.dynamiteRemaining -= 1
        if previousRound['p2'] == 'D':
            self.opponentDynamiteRemaining -= 1

    def SelectLikelyResponce(self, previousRound):
        weight = 8
        list = self.OpponentResponseTracker[previousRound['p1']]
        for i in range(0, weight * self.drawCount): # add weight to draw cunt tracking
            list += self.OpponentChoiceTracker[self.drawCount]

        max = 0
        # todo track other likely moves
        for key in self.OpponentResponseTracker.keys():
            if list.count(key) > max:
                mostLikelyMove = key
                max = list.count(key)

        return mostLikelyMove

    def drawSelection(self, gamestate, roundList):

        return 'W'

    def randomNumber(self, gamestate, range, start=0):
        randomHash = hash(str(gamestate))
        randomNumber = randomHash % range
        return randomNumber + start

    def randomChoice(self, gamestate):
        choices = ['R', 'P', 'S']
        choice = choices[self.randomNumber(gamestate, 3)]
        return choice

    def rockPaperScissors(self, gamestate, roundList):
        if self.roundCount < 10: # return random while getting data
            return self.randomChoice()

        choice = 'R'
        return choice

    def setDrawCount(self, roundList):

        draws = 0

        for round in roundList:
            if round['p1'] != round['p2']:
                return draws
            else:
                draws += 1
