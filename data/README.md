I'm confused about the differences between following datasets:
 - National Register Districts
 - National Register Buildings <-- ( I think this is the one listed as "National Registry of Historic Sites" below)
 - Local Landmarks
 - Historic Sites  <-- have this, pretty sparse but OK
 - National Historic Landmarks


National Registry of Historic Sites **
===========================
* received as spreadshseet
* status:  fully parsed, geocoded, imported ~ 2200 entries
* fields:
  - Property Name
  - Address
  - Address Description
  - County
  - City
  - Date Listed
  - Geo Location (geocoded using google maps lookup)
* notes:  we received a second version of the spreadhseet that also has geolocation in NAD83 mercator coordinates, which may be more accurate than the google query, so we can convert those instead


Barns **
=====
* received as spreadshseet
* status:  fully parsed, geocoded, imported 77 entries
* fields:
  - Property Name
  - Address
  - Address Description
  - Rural Location
  - ID
  - County
  - City
  - Date Listed
  - Geo Location (NAD83, converted to (lat, long))


Cultural & Entertainment Districts
===========================
 - received link to website
 - href: http://www.iowahistory.org/historic-preservation/cultural_districts/list-of-certified-districts.html
 - notes:  website has list of all the district, their names and city.  also has map images showing the regions/districts. we should try to get the coordinates / polygons (points of the stroke/line for the shape) some format so we can draw them ourselves on the map.  I assume this data exists, given the rendered images.  Without it, we either cant display the areas or need to trace them ourselves in a GIS application.


Museum Data *
============
- received link to website
- href: http://www.iowamuseums.org/aspx/museum/search.aspx
- notes: 
  - I think alexander tried contacting spindustry (who made the website) about getting the raw data, but didn't get that far with them.  
  - I've downloaded all the overview data by fetching the search page and extracting the html tables.  Still need to parse the table html, which then gives us the following fields: Museum Name, Type (History, Art, etc..), Region (West, Central, East), and City.  
  - Also includes a link to the museum details page on their website, which I will then also fetch and parse to get additional fields per entry on a per available basis.  
  - Fields usually on detail page are:  Address, Website, Phone, Email, County, Admission (Price / Free / Adults / Children ,etc), Hours and a few paragraphs of description about the museum.
  - Scraping it isn't technically that hard, but I don't want to just throw a scraper at it, and overload their website...that wouldn't be nice, so I'm planning on taking a few everyday ( manually to start with) until I'm sure the scraper doesn't accidentaly download more than it absolutely needs.  Then we can fetch the rest automatically (although we should still throttle it to avoid potential automated security rules to blacklist us.)
    
    
    
Historic Sites
==============
 - received spreadsheet (8 records)
 - href: https://docs.google.com/a/fresklabs.com/spreadsheet/ccc?key=0Ag1wOTpbkRfcdFhkWllrWC1ER09qd0FVZlFQdEt3bkE#gid=0
 - notes:  spreadhseet seems very sparse (maybe google docs conversion?, but dont think so).  Doesnt have column/field titles, but looks liek fields are:
 - fields:
   - Name of Histric Site (e.g. American Gothic House)
   - Address
   - City
   - ZIP code
   
   
National Historic Landmarks in Iowa
===================================
 - recieved: wikipedia link (24 records)
 - href: http://en.wikipedia.org/wiki/List_of_National_Historic_Landmarks_in_Iowa
 - fields:
   - Landmark Name
   - Image (mostly high res)
   - Date declared
   - Locality (City, State + geolocation)
   - County
   - Description (0 - 1 sentence (but most have their own wikipedia page))
   

Underground Railroad Sites
==========================
 - Contact: Doug Jones @ SHSI 
 - received website link
 - href: http://www.iowahistory.org/museum/ugrr-ia/sites.html
 - lists 4 existing "structures" in Iowa, each has its own website


Zoo
===
 - Contact Pearl @ IAC


Arts & Cultural Centers
=======================
 - Contact Pearl @ IAC
 

Opera Houses & Centers
=======================
 - Contact Pearl @ IAC

Theaters
=======================
 - Contact Pearl @ IAC


Science Centers
======================
 - Contact: ??
 
 
Gardens & Botanical Centers
===========================
 - Contact Pearl @ IAC
 

Medal of Honor Recipient Birthplaces
====================================
 - Contact: Susan
  

Famous Iowan Birthplaces
====================================
 - Contact: Jessica R
 

Iowa Award Recipient Birthplaces
====================================
 - Contact: ??
  

Certified Local Governments
====================================
 - Contact: ?? @ SHSI
 

Great Places
====================================
 - Contact: Jessica R
 

Significant Pieces of Land
====================================
 - Contact: ??
 

Scenic Byways
====================================
 - Contact: Jessica R
 
  
Historical Societies & Commissions
====================================
 - Contact: SK
  
 
Ampitheaters & Riverwalks
====================================
 - Contact: IAC
  
 
Oddball Sites
====================================
 - Contact: ??
  
 
Colleges & Universities
====================================
 - Contact: IAC & SHSI
  
 
Farmers Markets
====================================
 - Contact: Matt @ IAC
  
 
Festivals
====================================
 - Contact: ??
  
 
Concerts
====================================
 - Contact: ??
  
 
Cultural Events
====================================
 - Contact: ??
  
 

 
