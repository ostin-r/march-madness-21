'''
Austin Richards 3/16/21

sub-rank.py uses the sports-reference API, sportsipy to 
create a sub-ranking system based on the teams that a
given team has won against for march madness 2021
'''
from sportsipy.ncaab.teams import Team, Teams
from sportsipy.ncaab.schedule import Schedule

purdue_schedule = Schedule('PURDUE')
for game in purdue_schedule:
    print(game.result)

# TODO: get the game result, if it's a win: get the opponent's rank

# TODO: Adjust the average opponent rank accordingly (add it to a list?)