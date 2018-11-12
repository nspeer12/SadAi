import json
from pprint import pprint

# open json file
with open('Lyrics_LilPeep.json') as f:
	data = json.load(f)

# create txt file
txt_file = open("lyric_data.txt", "w")

# parse lyrics and print to txt file


x = 0
for i in data["songs"]:
	txt_file.write(data["songs"][x]["lyrics"])
	x+=1

txt_file.close()
