from paperbot import PaperBot

gamestate = {'rounds': [{ 'p1' : "a", 'p2' : "R" }, { 'p1' : "D", 'p2' : "a" }]}
gamestate1 = {'rounds': [{}]}

bot = PaperBot()
bot.roundCount += 3
play = bot.make_move(gamestate1)

print(play)