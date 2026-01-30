import json
import os
import requests

stats = os.listdir("stats")
deaths = []

session = requests.Session()
print("Getting Death Count....")
for stat in stats:    
    with open("stats/" + stat) as file:
        data = json.load(file)
        # Some stats don't have Deaths so we don't have to make useless requests to the API
        try:
            # Getting Death Counter
            tempCounter = data['stats']['minecraft:custom']['minecraft:deaths']

            # Get Username from UUID
            response = session.get(f"https://api.minetools.eu/uuid/{stat.replace(".json","")}")
            tempName = response.json()['name']

            # Name can sometimes come back as None
            if tempName:
                # Add to Deaths List
                deaths.append({"name": tempName, "deaths": tempCounter})
    
            # Show UUIDs that don't get Usernames
            # if not tempName:
            #     print(f"{tempName}: {stat.replace(".json","")}")
        except:
            # No Deaths or random stat object
            continue

session.close()

for death in deaths:
    print(f"/deathcounter set {death['name']} {death['deaths']}")