from django.shortcuts import render
from django.http import response
from django.http import HttpResponse
# 같은 폴더에 위치한 models.py 내부의 Student 클래스를 import 해야 Student 테이블의 데이터를 가져올 수 있음
from .models import Student


# Create your views here.

# 서버주소/students 접속시 실행해줄 함수
# 접속시 수행해줄 로직을 작성하는 함수는 Request는 필수 파라미터로 적혀야 함.
def students_list(request):
    """ 파이썬에서는 특성을 함수 선언부 다음줄에 설명해 줍니다. 
    HttpResponse는 응답을 text로 보내줍니다."""
    # return HttpResponse("/students 접속 연결 확인")

    # Student.objects.all() -> SELECT * FROM student;와 동일
    students = Student.objects.all()

    # print() 구문은 화면이 아니라 콘솔에 찍어줍니다.
    print('DB 데이터 모두 가져옴')

    # render(request, 결과하면.html, {화면에 쓸 변수명: 화면으로 보낼 데이터})
    # root/templates/list.html이 타겟이 된다.
    # 다만 이렇게 루트 폴더 하위 templates에 넣으면 무슨 용도로 쓰는건지 부정확하기 때문에 
    # 실제로는 개별 App  폴더 하위에 templates폴더를 하나 더 생성합니다.
    # 어플리케이션명/list.html로 어떤 app이 쓰는 파일인지 명확해집니다.
    return render(request, 'students/list.html', {'students':students})