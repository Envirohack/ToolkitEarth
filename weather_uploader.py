"""
This connects to the envirohack database which is hosted on mongolab, and uploads new data from 
http://opendap.bom.gov.au (overwriting old data). It is meant to be connected to a cron job which will 
update the database once per day.
"""

import pymongo
from pymongo import MongoClient
import urllib2
import sys
import re

connection = MongoClient("ds053638.mongolab.com", 53638)
db = connection["toolkit_earth"]
# MongoLab has user authentication
db.authenticate("rdengate", "envirohacK_427")


def parseLines(lines, index, precip, temperature):
    trackingPrcp = False
    trackingTemp = False
    for line in lines:
        if line.strip() == 'accum_prcp.accum_prcp[1][25][25]':
            trackingPrcp = True
            continue
        if trackingPrcp == True:
            if line.strip() == 'accum_prcp.time[1]':
                trackingPrcp = False
                continue
            if line.strip() == '':
                continue
            row = line.split(',')
            key = row.pop(0);
            rowIndex = re.search('\[\d+\]\[(\d+)\]',key).group(1)
            row = [float(value.strip()) for value in row]
            precip["%s_%s" % (i, rowIndex)] = row
        if line.strip() == 'sfc_temp.sfc_temp[1][25][25]':
            trackingTemp = True
            continue
        if trackingTemp == True:
            if line.strip() == 'sfc_temp.time[1]':
                trackingTemp = False
                continue
            if line.strip() == '':
                continue
            row = line.split(',')
            key = row.pop(0);
            rowIndex = re.search('\[\d+\]\[(\d+)\]',key).group(1)
            row = [float(value.strip())-273.15 for value in row]
            temperature["%s_%s" % (i, rowIndex)] = row


def readfile(usock, lon, lat, i, precipitationDict, temperatureDict):
    contents = usock.read()
    lines = contents.split("\n")
    parseLines(lines, i, precipitationDict, temperatureDict)


def writeToDatabase(lonList, latList, precipitationDict, temperatureDict, datetime):
    for lt, lat in enumerate(latList):
        for ln, lon in enumerate(lonList):
            precipThroughTimeList = []
            tempThroughTimeList = []
            for i in range(37):
                lonRow = precipitationDict["%s_%s" % (i, lt)]
                precipThroughTimeList.append(lonRow[ln])
                lonRow = temperatureDict["%s_%s" % (i, lt)]
                tempThroughTimeList.append(lonRow[ln])
            recordDict ={
                "_id": "%s_%s" % (lon, lat),
                "precipitation": precipThroughTimeList, 
                "temperature": tempThroughTimeList,
                "location": {
                    "type": "Point",
                    "coordinates": [
                        lon,
                        lat
                    ]
                },
                "datetime": datetime
            } 
            db.weather_at_point.update({"_id": "%s_%s" % (lon, lat)}, recordDict, True)

def getDate():
    base_url = 'http://opendap.bom.gov.au:8080/thredds/catalog/nmoc/access-sy-fc/ops/surface/latest/'
    usock = urllib2.urlopen(base_url)
    data = usock.read()
    usock.close()

    for line in data.split('\n'):
        match = re.search(r"ACCESS-SY_(\d+)_", line)
        if (match):
            return match.group(1)


if __name__ == "__main__":
    lat = [-35.048, -35.084, -35.12, -35.156, -35.192, -35.228, -35.264, -35.3, -35.336, -35.372, -35.408, -35.444, -35.48, -35.516, -35.552, -35.588, -35.624, -35.66, -35.696, -35.732, -35.768, -35.804, -35.84, -35.876, -35.912]
    lon = [148.62, 148.656, 148.692, 148.728, 148.764, 148.8, 148.836, 148.872, 148.908, 148.944, 148.98, 149.016, 149.052, 149.088, 149.124, 149.16, 149.196, 149.232, 149.268, 149.304, 149.34, 149.376, 149.412, 149.448, 149.484]

    precipitationDict = {}
    temperatureDict = {}

    date = getDate()

    for i in range(37):
        url = 'http://opendap.bom.gov.au:8080/thredds/dodsC/nmoc/access-sy-fc/ops/surface/' + date + '/ACCESS-SY_' + date + '_%03d_surface.nc.ascii?accum_prcp[0:1:0][141:1:165][45:1:69],sfc_temp[0:1:0][141:1:165][45:1:69]' % i
        usock = urllib2.urlopen(url)
        readfile(usock, lon, lat, i, precipitationDict, temperatureDict)
        usock.close()
    writeToDatabase(lon, lat, precipitationDict, temperatureDict, date)


