#!/usr/bin/python

# ----CALCULATION MODULE----
# Allows complex calculations to be carried out in other programs without having
# to re-write this code.

from math import *

def haversine(start, end):
	lat1, lon1 = start
	lat2, lon2 = end

	# The Haversine formula
	dlon = radians(lon2-lon1)
	dlat = radians(lat2-lat1)

	a = sin(dlat/2) * sin(dlat/2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2) * sin(dlon/2)
	c = 2 * atan2(sqrt(a), sqrt(1-a))

	# 6367 = Radius of the Earth
	distance = 6371 * c
	
	return distance	# (in km)

def decimalCoordinates(lat, lon):
	# Convert the Degrees, Minutes and Seconds returned by the GPS to decimal notation
	myIndex = lat.index("deg")
	latDeg = float(lat[0:myIndex])
	myIndex = myIndex + 4
	latMin = float(lat[myIndex:(myIndex+7)])
	decimalLat = latDeg + (latMin/60)

	myIndex = lon.index("deg")
	lonDeg = float(lon[0:myIndex])
	myIndex = myIndex + 4
	lonMin = float(lon[myIndex:(myIndex+6)])
	decimalLon = lonDeg + (lonMin/60)
	
	decimalCoordinates = [decimalLat, decimalLon]
	return decimalCoordinates

def convertDistance(distance, unit):
	# Convert km to miles or miles to km
	if unit.upper() == "MILES":
		distance = distance * 1.609344
		unit = "km"
	elif unit.upper() == "KM":
		distance = distance * 0.621371192
		unit = "miles"
	result = [distance, unit]
	return result

def calculateSpeed(distance, time):
	speed = float(distance) / float(time)
	return speed

def calories(speed, weight, time):
	# Speed in km/hr, weight in kg & time in hrs
	speed = float(speed)
	weight = float(weight)
	calories = (0.0251*speed**3 - 0.2157*speed**2 + 0.7888*speed + 1.2957) * weight * time
#	VO2 = 3.5 + (speed*0.2) + (speed*0.9)
#	MET = VO2/3.5
#	calories = MET * weight
	return calories

if __name__ == "__main__":
	startN = raw_input('Start North: ')
	startW = raw_input('Start West: ')
	start = [startN, startW]

	#start = ["51deg 35.6589N", "02deg 6.2614W"] 
	decimalStart = decimalCoordinates(start[0], start[1])
	print decimalStart

	endN = raw_input('End North: ')
	endW = raw_input('End West: ')
	end = [endN, endW]
	#end = ["51deg 28.5819N", "02deg 5.7663W"]
	decimalEnd = decimalCoordinates(end[0], end[1])
	print decimalEnd

	output = haversine(decimalStart, decimalEnd)

	outputMiles = convertDistance(output, "km")

	print "Distance between %s and %s:\n%skm \n%s%s" % (decimalStart, decimalEnd, output, outputMiles[0], outputMiles[1])
