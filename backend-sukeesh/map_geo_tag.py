import json

arr = ["administrative_area_level_1", "art_gallery", "bakery", "bar", "cafe", "clothing_store", "colloquial_area", "department_store", "electronics_store", "establishment", "florist", "food", "grocery_or_supermarket", "hair_care", "health", "home_goods_store", "liquor_store", "locality", "lodging", "meal_takeaway", "museum", "night_club", "park", "point_of_interest", "political", "restaurant", "spa", "store", "travel_agency", "university"]

lats = []
lons = []


with open('output.txt') as openfileobject:
	for line in openfileobject:
		lat, lon = line.split(" ")
		lats.append(float(lat))
		lons.append(float(lon))

i = 0
sub_data = {}
thisDict = {}
for cat in arr:
	thisDict[str(cat)] = 0
sub_data["lat"] = float(lats[i])
sub_data["long"] = float(lons[i])
data = []

tmp = []

with open('test.txt') as openData:
	for cats in openData:
		key = str(cats)
		key = key.replace("\n", "")
		tmp.append(key)

for key in tmp:
	if key == "random_item_to_block":
		print(sub_data)
		i = i + 1
		if i == 929:
			break

		for catlol in arr:
			thisDict[str(catlol)] = 0

		sub_data.clear()

		sub_data["lat"] = float(lats[i])
		sub_data["long"] = float(lons[i])
		continue
	
	scores = []
	thisDict[key] = thisDict[key] + 1
	for typs in arr:
		scores.append(thisDict[typs])
	
	sub_data["scores"] = scores


