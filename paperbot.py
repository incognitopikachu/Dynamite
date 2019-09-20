import random


class PaperBot:
    def __init__(self):
        self.dynamitesRemaining = 100
        self.roundCount = 0
        pass

    def Update(self, choice):
        if choice == 'D':
            self.dynamitesRemaining -= 1
        return

    def getRoundCount(self, roundList):
        return len(roundList)

    def make_move(self, gamestate):
        roundList = gamestate['rounds']
        self.roundCount = self.getRoundCount(roundList)
        drawCount = self.drawCount(roundList)

        if drawCount == 0:
            choice = self.rockPaperScissors(roundList)
        else:
            choice = self.drawSelection()

        # self.Update(choice)

        return choice

    def drawSelection(self, gamestate):
        return

    def randomChoice(self):
        choices = ['R', 'P', 'S']
        choice = choices[random.randint(0, 2)]
        return choice

    def rockPaperScissors(self, roundList):
        if self.roundCount < 10: # return random while getting data
            return self.randomChoice()

        choice = 'R'
        return choice

    def drawCount(self, roundList):

        draws = 0
        roundList.reverse()

        for round in roundList:
            if round['p1'] != round['p2']:
                return draws
            else:
                draws += 1
