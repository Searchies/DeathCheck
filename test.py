import json
deaths = []
deaths.append({"name": "search", "deaths": "6"})
deaths.append({"name": "ash", "deaths": "7"})

for death in deaths:
    print(death['name'] + death['deaths'])
    