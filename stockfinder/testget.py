import time
from stockgetter import *
start = time.time()
print netfonds_price("STL.OSE")
end = time.time()
duration = end - start
print "It took {0} seconds to fetch data from fra netfonds".format(duration)

start = time.time()
print price("STL.OL")
end = time.time()
duration = end - start
print "It took {0} seconds to fetch data from fra yahoo".format(duration)