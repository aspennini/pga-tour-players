'''
Name of script: get_player_info.py
Description: scrapes the wikipedia infoboxes for all
				players listed in the PGA Tour category
'''

import requests
from bs4 import BeautifulSoup
import lxml.etree
import urllib
import wptools

base_url = 'https://en.wikipedia.org/w/index.php?title=Category:PGA_Tour_golfers&'
url_end = ['from=A','pagefrom=Coles%2C+Gavin%0AGavin+Coles&subcatfrom=A&filefrom=A#mw-pages',
       'pagefrom=Geiberger%2C+Brent%0ABrent+Geiberger&subcatfrom=A&filefrom=A#mw-pages',
       'pagefrom=Jones%2C+Steve%0ASteve+Jones+%28golfer%29&subcatfrom=A&filefrom=A#mw-pages',
       'pagefrom=McRoy%2C+Spike%0ASpike+McRoy&subcatfrom=A&filefrom=A#mw-pages',
       'pagefrom=Riegger%2C+John%0AJohn+Riegger&subcatfrom=A&filefrom=A#mw-pages',
       'pagefrom=Tway%2C+Bob%0ABob+Tway&subcatfrom=A&filefrom=A#mw-pages']

links = []

for n in range(0,len(url_end)):
    url = base_url + url_end[n]
	website_url = requests.get(url).text

	soup = BeautifulSoup(website_url,'lxml')
	soup2 = soup.find('div', class_='mw-category')
	for i in soup2.find_all(name = 'li'):
    	# pull the actual link for each one
    	for link in i.find_all('a', href=True):
        	links.append(link.get('title'))

players = pd.DataFrame()
                                 
for n in range(0, len(links)):	
	so = wptools.page(links[n]).get_parse().data['infobox']
	so1 = {}
	for (key, value) in so.items():
   		# Check if key is even then add pair to new dictionary
   		if key in ['name', 'fullname', 'birth_date', 'height',
             	'weight', 'nationality', 'college', 'yearpro',
             	'prowins', 'pgawins', 'majorwins']:
       		so1[key] = value
    players = players.append([so1])
    
