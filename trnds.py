try:
    import json
except ImportError:
    import simplejson as json

import csv

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '1660471136-gTl1XwgI1yVTBCQwhQBAknEhqmeEHKjhXaJyutR'
ACCESS_SECRET = 'iaKFeL2OtS15ddTjFurWeVpUrligzJHJ9PgYqfBkIDAw2'
CONSUMER_KEY = 'tDHKXx4j2wXlm1j4y97FpTFPn'
CONSUMER_SECRET = 'aL92keHuYjydc2K8oXAPfT1cwO4Elr3upLIecYNTfdVEjx59hH'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

india_trends = twitter.trends.place(_id=23424848)

#print(json.dumps(world_trends, indent=4))

i=0
with open('trnds.txt','a') as obj:
    while i<10:
        obj.write(india_trends[0]['trends'][i]['name']+'\n')
        i=i+1

with open('trnds.txt') as obj:
    for line in obj:
        print(line)