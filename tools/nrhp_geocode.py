import tablib
import json
import slugify
import os.path
from pygeocoder import Geocoder
output = []

data = tablib.Dataset()
data.csv = open("data/nrhp.csv", "r").read()
for place in data.dict:
    slug = slugify.slugify(place['Property Name']+" "+place['City'])
    fname = u"data/nrhp/{0}.json".format(slug)
    if os.path.exists(fname):
        print u"skipping existing record: {Property Name}".format(**place)
        output.append( json.load(open(fname, 'r')) )
        continue
    print u"geocoding: {Property Name}".format(**place)
    addr = u"{Property Name}, {Address}, {City}, IA".format(**place)
    place['geo'] = Geocoder.geocode(addr).raw
    json.dump(place, open(fname, "w"))
    output.append(place)

json.dump(output, open("data/nrhp.json", "w"))







