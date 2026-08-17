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

# 전체 데이터 삭제하기
# [Other QuerySet methods](https://docs.djangoproject.com/en/6.0/topics/db/queries/?utm_source=chatgpt.com#other-queryset-methods)
# [Use QuerySet.update() and delete()](https://docs.djangoproject.com/en/6.0/topics/db/optimization/#use-foreign-key-values-directly)

from book_list.models import BookList

def delete_all():
    BookList.objects.all().delete()

########################################################################################
########################################################################################

print(BookList.objects.all())
print(len(BookList.objects.all()))

if __name__ == '__main__':
    delete_all()
    