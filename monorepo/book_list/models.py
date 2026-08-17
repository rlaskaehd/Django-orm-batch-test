from django.db import models

# Create your models here.

# title,primary_author,publisher,published_date,list_price,detail_url,author_count
# primary_author을 제외한 타 컬럼에서의 null은 존재할 수 없지만 안정성을 위해 blank=True를 사용하였습니다.
# list_price의 경우 값이 없을 때 NULL이 들어가며 타 컬럼에서는 "" 이 들어갑니다.
class BookList(models.Model):
    title = models.CharField(max_length=100)
    primary_author = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    published_date = models.CharField(max_length=20, blank=True)
    list_price = models.IntegerField(null=True, blank=True)
    detail_url = models.URLField(max_length=200)
    author_count = models.IntegerField()
    
    def __str__(self):
        return self.title

