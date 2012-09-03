file = open('stocklist.txt','r')
lines = file.readlines()
ticker_name_pair ={}
for line in lines:
	tickerdata = line.split('\t')
	ticker_name = str(tickerdata[0])
	ticker_name_pair[ticker_name] = tickerdata[1]
print ticker_name_pair