from django.db import models

# Create your models here.
# models.py에 선언된 것은 아직 반영이 되지 않았으므로,
# 최초생성시 makemigrate, 이후 변경은 migrate 구문을 실행해서 갱신합니다.
class Student(models.Model): # 테이블명은 Student다
    name = models.CharField(max_length=100) # name 컬럼은 100글자 제한의 문자 자료형이다.
    age = models.IntegerField() # 나이는 정수이다.
    email = models.EmailField(unique=True) # 이메일은 유일한 값이어야 하고, 이메일 주소 규칙을 따른다.
    created_at = models.DateTimeField(auto_now_add=True) # 입력 시점을 자동으로 필드에 채워준다.

    # print() 구문으로 디버깅시 객체의 이름이 대표값으로 출력됨
    def __str__(self):
        return self.name
