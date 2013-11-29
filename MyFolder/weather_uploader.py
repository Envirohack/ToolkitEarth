import pymongo
from pymongo import MongoClient
import urllib2
import re


base_url = 'http://opendap.bom.gov.au:8080/thredds/catalog/nmoc/access-sy-fc/ops/surface/latest/'
usock = urllib2.urlopen(base_url)
data = usock.read()
usock.close()
#print(data)

DATE_RE = re.compile(r"^(?P<type>ACCESS-SY_[\d]{10})\s+")

for line in data.split('\n'):
	m = DATE_RE.match(line)
	if (m):
		line = line[m.end():m.end()+4]
		print line
		break

"""
for i in range(37):
	url = 'http://opendap.bom.gov.au:8080/thredds/dodsC/nmoc/access-sy-fc/ops/surface/2013112618/ACCESS-SY_2013112618_%03d_surface.nc.ascii?accum_prcp[0:1:0][141:1:165][45:1:69],sfc_temp[0:1:0][141:1:165][45:1:69]' % i
	usock = urllib2.urlopen(url)
	data = usock.read()
	usock.close()
	print(data)
"""

"""
connection = MongoClient("ds053638.mongolab.com", 53638)
db = connection["toolkit_earth"]
# MongoLab has user authentication
db.authenticate("rdengate", "envirohacK_427")


MetarObj = {}
MetarObj['Test'] = 'Test Document'

collection = db.weather_at_point
collection.insert(MetarObj)
print('written to DB')

lat = [-35.048, -35.084, -35.12, -35.156, -35.192, -35.228, -35.264, -35.3, -35.336, -35.372, -35.408, -35.444, -35.48, -35.516, -35.552, -35.588, -35.624, -35.66, -35.696, -35.732, -35.768, -35.804, -35.84, -35.876, -35.912]
lon = [148.62, 148.656, 148.692, 148.728, 148.764, 148.8, 148.836, 148.872, 148.908, 148.944, 148.98, 149.016, 149.052, 149.088, 149.124, 149.16, 149.196, 149.232, 149.268, 149.304, 149.34, 149.376, 149.412, 149.448, 149.484]
"""