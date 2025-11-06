book = {}
book['tom']={
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': '39393939'
}

book['bob']={
    'name': 'bob',
    'address': '1 red street, NY',
    'phone': '23232323'
}

import json
s= json.dumps(book)
with open("C://data//book.txt", "w") as f:
    f.write(s)