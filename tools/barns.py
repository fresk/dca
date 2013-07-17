import tablib
import json
import utm

output = []

data = tablib.Dataset()
data.csv = open("data/barns.csv", "r").read()
for place in data.dict:
    uid = place['ID#']
    addr = u"{Property Name}, {Address}, {City}, IA".format(**place)
    geo_loc = utm.to_latlon(float(place['Easting']), float(place['Northing']), int(place['Zone']), 'T')
    place['geo'] = {'lat': geo_loc[0], 'lng':geo_loc[1]}
    output.append(place)

json.dump(output, open("data/barns.json", "w"))








