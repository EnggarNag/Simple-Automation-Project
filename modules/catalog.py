from modules.book import Book
from modules.dvd import Dvd


class Catalog():
    def __init__(self, catalog):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_search.lower() in item.title.lower():
                    if type(item) is Dvd:
                        list_result.append(
                            f'Title: {item.title}'
                            f' | Genre: {item.genre}'
                            f' | Type Catalog: DVD'
                            )
                    elif type(item) is Book:
                        list_result.append(
                            f'Title: {item.title}'
                            f' | DDS Number: {item.dds_number}'
                            f' | Type Catalog: Book'
                            )
        return list_result
