
with open('geodata.txt') as geodata:
	data = "["
	for line in geodata:
		data = data + line + ","
	data = data + "]"
	data = data.replace("'", "\"")
	print(data)
