from paperbot import PaperBot

gamestate = {'rounds': [{ 'p1' : "R", 'p2' : "D" }, {   'p1' : "W", 'p2' : "S" }]}

bot = PaperBot()
play = bot.make_move(gamestate)

print(play)