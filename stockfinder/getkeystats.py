import time
import urllib2
from BeautifulSoup import BeautifulSoup
def getkeystats(ticker):
	url_start ="http://www.bloomberg.com/quote/"
	url_end = ":NO/key-statistics"
	url = url_start + ticker + url_end
	html = urllib2.urlopen(url) 
	soup = BeautifulSoup(html)
	t = soup.findAll('table')
	key_stats = {}
	data = []
	#linje = 0
	for table in t:
		rows = table.findAll('tr')
		for tr in rows:
			#print tr
			cols = tr.findAll('td')
			for td in cols:
				#Uncomment these lines when debugging to obtain a variables index in the data-list
				'''
				print "Linje nr"
				print linje
				'''
				print td.findAll(text=True)
				data.append(td.findAll(text=True))
				#linje = linje +1 
	key_stats['PB']=float(data[39].pop())
	key_stats['PS']=float(data[40].pop())
	#key_stats['EBITDA']=float(data[44].pop())
	key_stats['EPS']=float(data[48].pop())
	key_stats['PE']=float(data[51].pop())
	return key_stats