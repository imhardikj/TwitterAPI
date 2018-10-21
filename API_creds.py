import json

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['CONSUMER_KEY'] = 'tDHKXx4j2wXlm1j4y97FpTFPn'
credentials['CONSUMER_SECRET'] = 'aL92keHuYjydc2K8oXAPfT1cwO4Elr3upLIecYNTfdVEjx59hH'
credentials['ACCESS_TOKEN'] = '1660471136-gTl1XwgI1yVTBCQwhQBAknEhqmeEHKjhXaJyutR'
credentials['ACCESS_SECRET'] = 'iaKFeL2OtS15ddTjFurWeVpUrligzJHJ9PgYqfBkIDAw2'

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)