import json
from pprint import pprint



with open('countries.json', 'r') as f:
    data = f.read()



par = json.loads(data)

# print (len(par)) Дает понимание кол-ва стран


countries_count = par[0:250]

for i in countries_count:
    print(i['name']['official'])




#
# def get_countries():
#     # countries_names = ' '
#     for names in countries_names:
#         return names



# if __name__ == '__main__':
#
#     pprint(get_countries())





