import requests

apiKey = "YOUR_API_KEY_HERE"

def addLocationSuf(lat, lon):
	ret = "location="
	ret = ret + str(lat) + "," + str(lon)
	return ret

def addRadiusSuf(m):
	ret = "radius="
	ret = ret + str(m)
	return ret

def addKeySuf():
	ret = "key="
	ret = ret + str(apiKey)
	return ret

lats = []
lons = []
nearbyReqPrefix = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

with open('output.txt') as openfileobject:
	for line in openfileobject:
		lat, lon = line.split(" ")
		lats.append(float(lat))
		lons.append(float(lon))

sz = len(lats)

for i in range(sz):
	lat, lon = lats[i], lons[i]
	url = nearbyReqPrefix + addLocationSuf(lat, lon) + "&" + addRadiusSuf(2000) + "&" + addKeySuf()
	r = requests.get(url)
	data = r.json()
	for eachPlace in data['results']:
		types = eachPlace['types']
		for eachType in types:
			print(eachType)
	print("random_item_to_block")
