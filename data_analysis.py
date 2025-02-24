import glob
import json

#open the json files
def combined_function():
    with open('data/cities.json', "r") as infile:
        cities = json.load(infile)
    with open('data/libraries.json', "r") as infile:
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
    with open('data/combined.json', 'w') as f:
        json.dump(combined, f) 
        
combined_function()