import json
from pathlib import Path
from django.core.management import BaseCommand
from catalog.models import Product, Category


# python3 -Xutf8 manage.py dumpdata catalog > catalog.json
# python -Xutf8 manage.py dumpdata catalog.product -o products.json
# python -Xutf8 manage.py dumpdata catalog.category -o categories.json

class Command(BaseCommand):


    @staticmethod
    def json_read_categories():
        """получаем данные из фикстуры с категориями"""
        with open('categories.json', 'r', encoding="utf-8") as f:
            categories = json.load(f)
            print(categories)





if __name__ == "__main__":
    Command.json_read_categories()