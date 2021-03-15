# Course 4
# Python for Data Science, AI & Development
# 13 - Introduction to API

#APIs

#!pip install nba_api

#Pandas is an API

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict   

import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)
type(df)

df.head()

df.mean()

#REST APIs

from nba_api.stats.static import teams
import matplotlib.pyplot as plt
#https://pypi.org/project/nba-api/

nba_teams = teams.get_teams()

nba_teams[0:3]

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()

df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors

id_warriors=df_warriors[['id']].values[0][0]
#we now have an integer that can be used   to request the Warriors information 
id_warriors

from nba_api.stats.endpoints import leaguegamefinder
# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
# gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
# gamefinder.get_json()

# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
# games = gamefinder.get_data_frames()[0]
# games.head()

! wget https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl

file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()

games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']

games_home.mean()['PLUS_MINUS']

games_away.mean()['PLUS_MINUS']

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()

#Calculate the mean for the column PTS for the dataframes games_home and  games_away:
games_home.mean()['PTS']

games_away.mean()['PTS']

