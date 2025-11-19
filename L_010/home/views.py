from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from home.models import Thread


class ThreadListView(View):
    def get(self, request, *args, **kwargs):
        context_data = {
            "title": "Forum",
            "threads": Thread.objects.all()
        }
        return render(request,
                      "home/threads_list.html",
                      context=context_data)