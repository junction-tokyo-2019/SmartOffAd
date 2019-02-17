arr = ["administrative_area_level_1", "art_gallery", "bakery", "bar", "cafe", "clothing_store", "colloquial_area", "department_store", "electronics_store", "establishment", "florist", "food", "grocery_or_supermarket", "hair_care", "health", "home_goods_store", "liquor_store", "locality", "lodging", "meal_takeaway", "museum", "night_club", "park", "point_of_interest", "political", "restaurant", "spa", "store", "travel_agency", "university"]

optionpre="<option "
optionsuf="</option>"

for i in arr:
	here = optionpre + "value=\"" + i + "\">" + i.replace("_", " ") + optionsuf
	print(here)
