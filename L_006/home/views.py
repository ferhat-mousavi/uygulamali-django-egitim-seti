from django.http import HttpResponse
from django.shortcuts import render

from home.models import Thread


def threads_list(request):
    context_data = {
        "title": "Forum",
        "threads": Thread.objects.all()
    }
    return render(request,
                  "home/threads_list.html",
                  context=context_data)
