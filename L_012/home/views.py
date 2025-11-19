from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from home.models import Thread


class ThreadListView(View):
    def get(self, request, *args, **kwargs):
        threads = Thread.objects.all()
        paginator = Paginator(threads, 4)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context_data = {
            "title": "Forum Anasayfa",
            "page_obj": page_obj
        }
        return render(request,
                      "home/threads_list.html",
                      context=context_data)