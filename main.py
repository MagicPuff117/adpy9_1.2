import json
from pprint import pprint



with open('countries.json', 'r') as f:
    data = f.read()



par = json.loads(data)

# return (par[0]['name']['official'])

def get_countries():
    while True:
        for countries_names in par[0]['name']['official']:
            # i = par[0]['name']['official']
            return countries_names



if __name__ == '__main__':

    pprint(get_countries())





