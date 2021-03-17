'''
Austin Richards 3/16/21

sub-rank.py uses the sports-reference API, sportsipy to 
create a sub-ranking system based on the teams that a
given team has won against for march madness 2021
'''
import logging as log
import pyinputplus as pyip
from sportsipy.ncaab.schedule import Schedule
log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(message)s')
log.disable(log.CRITICAL)


while True:

    def schedule_rank(team):
        '''
        schedule_rank gets the average opponent rank
        for matches that the given team has won
        '''
        ranks = []
        schedule = Schedule(team)

        for game in schedule:
            opp_rank = game.opponent_rank
            if game.result == 'Win' and opp_rank is not None:
                ranks.append(opp_rank)

        if len(ranks) > 0:
            avg_rank = sum(ranks) / len(ranks)
            log.debug('opponent ranks: ' +  str(ranks))
            log.debug('average rank: ' + str(avg_rank))

            return avg_rank
        
        else:
            return 'no rank'


    def compare_teams(team_A, team_B):
        '''
        prints the schedule_rank of each team
        so the user can decide which team to pick
        '''
        rank_A = schedule_rank(team_A)
        rank_B = schedule_rank(team_B)

        print(f'{team_A} ranking: {rank_A}')
        print(f'{team_B} ranking: {rank_B}')

        return


    team_A = pyip.inputStr('First team? ').upper()
    team_B = pyip.inputStr('Second team? ').upper()

    if team_A == 'quit':
        break

    compare_teams(team_A, team_B)