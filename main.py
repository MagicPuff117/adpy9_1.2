import json
from pprint import pprint
import string
import wikipediaapi


# with open('countries.json', 'r') as f:
#     data = f.read()
#
# countries = json.loads(data)
# # pprint(str(countries))# Дает кол-ва стран
#
# all_countries = countries
#
# CHARS = string.ascii_lowercase
#
#
# # countries = []
# def get_countries():
#     for items in all_countries:
#         return items




class My_Iterator():
    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start - 1
        self.wiki = wikipediaapi.Wikipedia('en')
        # self.url = f'https://wikepedia.org/wiki/{str(country[0]["name"]["official"].lower())}/'
        # self.last_link = []
        # self.chars = string.ascii_lowercase.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['official']
        country_page = self.wiki.page(country)
        country_link = country_page.fullurl
        return country, country_link

<<<<<<< HEAD

        # if len(self.last_link) > 25:
        #     raise StopIteration
        # if not self.last_link:
        #     self.last_link = [self.chars.__next__()]
        # elif self.last_link[-1] == 'z':
        #         self.chars = CHARS.__iter__()
        #         self.last_link.append(self.chars.__next__())
        # else:
        #     self.last_link.append(self.chars.__next__())
        # return f'{self.url}{"".join(self.last_link)}'


#
# for link in My_Iterator(countries):
#     pprint(link)
#
=======
for i in countries_count:
    print(i['name']['official'])

>>>>>>> 1c11fb80d5346604485ee86822c71855adba4914



#
# def get_countries():
#     # countries_names = ' '
#     for names in countries_names:
#         return names


<<<<<<< HEAD
if __name__ == '__main__':
    output_file = open('countries_with_links.txt', 'w', encoding='utf-8')


    for country, item in My_Iterator('countries.json', 0):
        output_file.write(str(country) + '>' + str(item) + '\n')
        print('.', end='', flush=True)
=======

# if __name__ == '__main__':
#
#     pprint(get_countries())
>>>>>>> 1c11fb80d5346604485ee86822c71855adba4914

    output_file.close()




