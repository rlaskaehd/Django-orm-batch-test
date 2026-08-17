# Django 초기화

import os
import sys
from pathlib import Path

MONOREPO = Path("/Users/ahh/bootcamp-playground/chapter2/monorepo")

if str(MONOREPO) not in sys.path:

    sys.path.insert(0, str(MONOREPO))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


import django
django.setup()

from book_list.models import BookList

########################################################################################
########################################################################################

import csv

check_limit = 2

with open('../data/books.csv', 'r', encoding='utf-8-sig') as cf:
    dataset = list(csv.DictReader(cf))

print(f'''총 데이터 수:{len(dataset)}''')

########################################################################################
########################################################################################

# 실험 2. 전체 데이터를 한건씩 삽입하기

from book_list.models import BookList

book_list = []

for data in dataset:

    book_list.append(
        BookList(
            title=data['title'],
            primary_author=data['primary_author'],
            publisher=data['publisher'],
            published_date=data['published_date'],
            list_price=data['list_price'],
            detail_url=data['detail_url'],
            author_count=data['author_count'],
        )
    )

BookList.objects.bulk_create(book_list, 100)
print(f'DB에 적재된 rows:{len(BookList.objects.all())}')

########################################################################################
########################################################################################