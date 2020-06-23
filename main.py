import json
from pprint import pprint
import string
import wikipediaapi


# with open('countries.json', 'r') as f:
#     data = f.read()


class My_Iterator():
    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start - 1
        #self.wiki = wikipediaapi.Wikipedia('en')


    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['official']
        country_page = 'https://en.wikipedia.org/wiki/'  #self.wiki.page(country)
        country_link = country_page + country.replace(' ', '') #country_page.canonicalurl
        return country, country_link



if __name__ == '__main__':
    output_file = open('countries_with_links.txt', 'w', encoding='utf-8')


    for country, item in My_Iterator('countries.json', 0):
        output_file.write(str(country) + '  >  ' + str(item) + '\n')
    print('Ссылки созданы')  # end='', flush=True)



    output_file.close()







