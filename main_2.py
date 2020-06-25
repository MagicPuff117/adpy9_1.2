import hashlib



def get_hash_md5(file:str):
    with open(file, 'rt', encoding= 'utf-8') as f:
        for i in f:
            string = hashlib.md5(i.encode())
        yield string.hexdigest()


if __name__ == '__main__':
    for string in get_hash_md5('countries.json'):
        print(string)