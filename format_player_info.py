'''
Name of script: format_player_info.py
Description: formats player info that was gathered
				from wikipedia infoboxes
'''

import pandas as pd

players = pd.read_csv('pga-tour-players/player_info.csv')

# fix nationalities
players['nationality'].replace({'{{ZAF}}':'ZAF', '{{AUS}}':'AUS','{{CHL}}':'CHL', '{{KOR}}':'KOR',
                            '{{MEX}}':'MEX', '{{CAN}}':'CAN','{{JPN}}':'JPN', '{{THA}}':'THA',
                            '{{IND}}':'IND', '{{ENG}}':'ENG','{{SCO}}':'SCO', '{{SWE}}':'SWE',
                            '{{ESP}}':'ESP', '{{ARG}}':'ARG','{{DNK}}':'DNK', '{{TWN}}':'TWN',
                            '{{NIR}}':'NIR', '{{BEL}}':'BEL','{{IRL}}':'IRL', '{{ZIM}}':'ZIM',
                            '{{NAM}}':'NAM', '{{WAL}}':'WAL','{{CHN}}':'CHN', '{{FRA}}':'FRA',
                            '{{PRY}}':'PRY', '{{BRA}}':'BRA','{{COL}}':'COL', '{{DEU}}':'DEU',
                            '{{ZWE}}':'ZWE', '{{VEN}}':'VEN','{{MYS}}':'MYS', '{{AUT}}':'AUT',
                            '{{FJI}}':'FJI', '{{ITA}}':'ITA','{{ZMB}}':'ZMB', '{{NZL}}':'NZL',
                            '{{NOR}}':'NOR', 'American':'USA','{{Flagu|Argentina}}':'ARG',
                            '{{flagicon|IRE|1783}} [[Ireland]]':'IRL','{{flagcountry|ZAF|1928}}':'ZAF',
                            '{{TRI}} <br/> {{CAN}}':'TRI/CAN','{{SCO}} <br> {{USA}}':'SCO/USA',
                            '{{ENG}} <br> {{USA}}':'ENG/USA','{{CAN}} <br> {{USA}}':'CAN/USA',
                            '{{CSK}} <br> {{DEU}}':'CSK/DEU','{{IRL}} <br /> {{USA}}':'IRL/USA',
                            '{{NIR}} <br> {{USA}}':'NIR/USA','{{AUS}} <br> {{USA}}':'AUS/USA',
                            '{{SCO}} <br> {{CAN}}':'SCO/CAN','{{SCO}} <br /> {{USA}}':'SCO/USA',
                            '{{USA}} <br> {{KOR}}':'USA/KOR','{{ITA}} <br> {{USA}}':'ITA/USA',
                            '{{SWE}} <br> {{USA}}':'SWE/USA','{{PRI}} <br> {{USA}}':'PRI/USA',
                            '{{ZAF}} <br> {{SVK}}':'ZAF/SVK','{{SCO}} <br> {{flagcountry|USA|1912}}':'SCO/USA'},
                            inplace=True)

players['nationality'].replace(['{{USA}}','{{Flagcountry|United States|1960|size|=|23px}}',
                            '{{flagu|United States}}','{{flagcountry|USA|1912}}'], 'USA', inplace=True) 
                            
players['majorwins'].fillna(0, inplace=True)
players['prowins'].fillna(0, inplace=True)
players['pgawins'].fillna(0, inplace=True)
players['fullname'].fillna(0, inplace=True)
players['college'].fillna('', inplace=True)

# fix height
feet = players['height'].str.split('|', expand=True)[[3,6]]
inches = feet[6].str.split('}', expand=True)[[0]]
height = feet[[3]].join(inches)
height.rename(columns={3:'height_ft',0:'height_in'}, inplace=True)
players = players.join(height)
players.drop(labels='height', axis=1, inplace=True)

# fix weight
weight = players['weight'].str.split('|', expand=True)[[1]]
weight.rename(columns={1:'pounds'}, inplace=True)
players = players.join(weight)
players.drop(labels='weight', axis=1, inplace=True)

# fix birthday
birth = players['birth_date'].str.split('|', expand=True)[[1,2,3]]
year_month = birth[[1,2]]
day = birth[3].str.split('}', expand=True)[[0]]
birthdate = year_month.join(day)
birthdate.rename(columns={1:'year',2:'month',0:'day'}, inplace=True)
players = players.join(birthdate)
players.drop(labels='birth_date', axis=1, inplace=True)
