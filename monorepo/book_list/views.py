from django.shortcuts import render
from django.core.paginator import Paginator

from .models import BookList
# Create your views here.


def books_list(request):
    books = BookList.objects.order_by("id")
    paginator = Paginator(books, 25)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        'books/list.html',
        {
            "books": page_obj.object_list,
            "page_obj": page_obj,
        }
    )
