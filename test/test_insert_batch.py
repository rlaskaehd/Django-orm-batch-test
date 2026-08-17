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

import time
from book_list.models import BookList
from delete_data import delete_all

batch_list = [10, 50, 100, 500, 1000, 5000, 10000, 50000, None]

for batch in batch_list:
    for i in range(1, 11):
        book_list = []

        # 시간 측정 시작
        start_total = time.perf_counter()

        # 인스턴스 생성

        start_make_instance = time.perf_counter()

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

        end_make_instance = time.perf_counter()

        # 전체 데이터 삽입
        start_insert = time.perf_counter()

        BookList.objects.bulk_create(book_list, batch)

        end_insert = time.perf_counter()

        # 시간 측정 종료
        end_total = time.perf_counter()

        print(f"인스턴스 생성 소요시간: {end_make_instance - start_make_instance:.6f}초")
        print(f"DB 삽입 소요시간: {end_insert - start_insert:.6f}초")
        print(f"총 소요시간: {end_total - start_total:.6f}초")

        insert_size = batch
        repeat_no = i
        instance_build_seconds = end_make_instance - start_make_instance
        insert_seconds = end_insert - start_insert
        total_seconds = end_total - start_total
        avg_row_insert_sec = None

        with open("result/result.csv", "a", newline="", encoding="utf-8") as result_file:
            writer = csv.writer(result_file)
            writer.writerow(
                [
                    insert_size,
                    repeat_no,
                    instance_build_seconds,
                    insert_seconds,
                    total_seconds,
                    avg_row_insert_sec
                ]
            )

        print(f'삭제 전: {len(BookList.objects.all())}')
        delete_all()
        print(f'삭제 후: {len(BookList.objects.all())}')

########################################################################################
########################################################################################