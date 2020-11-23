import pandas as pd
from elopy import *

df = pd.read_csv('data/scores.csv')

results = pd.DataFrame(columns=["week","winner","loser"])

c = 0

for i in df.Week.unique():
    week_df = df.loc[df['Week'] == i]
    
    week_df.sort_values('Score')

    for winner in week_df.index:
        for loser in week_df.loc[week_df['Score'] < week_df.loc[winner].Score].index:
            results = results.append(pd.DataFrame({'week': [i], 'winner': [week_df.loc[winner].Team], 'loser': [week_df.loc[loser].Team]}, index = [c]))
            c += 1

# results.to_csv('data/results.csv')

imp = Implementation()

for team in df.Team.unique():
    imp.addPlayer(team)

for i in results.index:
    win_team = results.loc[i].winner
    lose_team = results.loc[i].loser
    imp.recordMatch(win_team, lose_team, winner=win_team)
    print(imp.getRatingList())
