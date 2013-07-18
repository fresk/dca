import urllib2
import hashlib
import json
from pprint import pprint
from bs4 import BeautifulSoup

url  = "http://en.wikipedia.org/wiki/List_of_National_Historic_Landmarks_in_Iowa"
url_hash = hashlib.md5(url).hexdigest()
fname = "{0}.html".format(url_hash)


def fetch():
    header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    with open(fname, 'w') as f:
        f.write(page.read())


def parse_row(row):
    cells = row.find_all("td")
    r = {}
    r['name'] = cells[1].a.get('title')

    try:
        img = cells[2].a.img['alt'].replace(" ", "_")
        img_md5 = hashlib.md5(img).hexdigest()
        url = "http://upload.wikimedia.org/wikipedia/commons/"
        r['img_md5'] = img_md5
        r['image'] = url + "{0}/{1}/{2}".format(img_md5[0], img_md5[0:2], img)
    except:
        r['img_md5'] = None
        r['image'] = None

    r['date_decalred'] = cells[3].small.span.string

    r['locality'] = cells[4].a.string

    geo = cells[4].find_all("span", class_="geo")
    if geo:
        r['geo'] = map(float, geo[0].string.split(';'))
    else:
        r['geo'] = [0,0]

    r['county'] = "".join(cells[5].a.strings)
    r['info'] = "".join(cells[6].strings)

    return r

#fetch()
page = open(fname, 'r')
soup = BeautifulSoup(page)
table = soup.find("table", { "class" : "wikitable sortable" })
data = [parse_row(row) for row in table.find_all("tr")[1:]]
json.dump(data, open('landmarks.json', 'w'))



