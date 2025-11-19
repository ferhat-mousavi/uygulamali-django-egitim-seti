from django.http import HttpResponse
from django.shortcuts import render

def threads_list(request):
    context_data = {
        "title": "Forum"
    }
    return render(request,
                  "home/threads_list.html",
                  context=context_data)
