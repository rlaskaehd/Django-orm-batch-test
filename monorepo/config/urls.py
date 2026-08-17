"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from students.views import students_list
from book_list.views import books_list

# urlpatterns에 접속 주소를 지정한다면, 해당 주소로 사용자가 접속했을 때, 
urlpatterns = [
    path('admin/', admin.site.urls),

    # 127.0.0.1:8000/students 접속시 2번째 파라미터로 넣은 함수르 실행한다.
    path('students/', students_list,name='students_list'),

    path('books/', books_list, name='books_list'),
]
