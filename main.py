import json
from modules.book import Book
from modules.dvd import Dvd
from modules.catalog import Catalog

f = open('files/catalog.json')
data_json = json.load(f)

dvds = []
books = []

for item in data_json:
    if item['source'] == 'dvd':
        dvds.append(
            Dvd(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                actors=item['actors'],
                directors=item['directors'],
                genre=item['genre']
            )
        )
    elif item['source'] == 'book':
        books.append(
            Book(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                issbn=item['issbn'],
                authors=item['authors'],
                dds_number=item['dds_number']
            )
        )

catalog_all = [books, dvds]
# input_search = 'infinity'
print(">================= Selamat datang di Library Item =================<")
print("Silahkan Cari Item yang anda inginkan (misal 'Infinity' atau 'harry')")
input_search = input("Search : ")
result = Catalog(catalog_all).search(input_search)
print("Berikut adalah hasil pencarian dari :", input_search)
for index, result in enumerate(result):
    print(f'result ke {index+1} | {result}')
