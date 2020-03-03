import glob
import json

#open the json files
<<<<<<< HEAD
with open('data\cities.json', "r") as infile:
    cities = json.load(infile)
with open('data\libraries.json', "r") as infile:
=======
with open('cities.json', "r") as infile:
    cities = json.load(infile)
with open('libraries.json', "r") as infile:
>>>>>>> a45f55011fc258a00c0a414f02870fe015ae069b
    libraries = json.load(infile)

#create combined dict and combine them

combined = {}
for i in range(len(cities)):
    combined_books = 0
    for j in range(len(libraries)):
        if (cities[i]['name'] == libraries[j]['city']):
            combined_books += libraries[j]['books']
        
    combined[cities[i]['name']] = {
        "population": cities[i]["population"],
        "books": combined_books
    }

#write to a new json file
with open('combined.json', 'w') as f:
    json.dump(combined, f)