import bs4 as bs
import urllib.request

clan = 'gx'

wotlife = 'https://en.wot-life.com/eu/clan/' + clan

url = urllib.request.urlopen(wotlife).read()

soup = bs.BeautifulSoup(url,'lxml')

players = []
bloat = []

for p in soup.find_all('a'):
	if p.text == ' Other':
		break
	bloat.append(p.text)

bloat.append(' Other')

for p in soup.find_all('a'):
	if p.text == ' World of Tanks Profile':
		break
	if p.text not in bloat + players:
		players.append(p.text)

players.sort(key=lambda str: str.lower())

#print(players)