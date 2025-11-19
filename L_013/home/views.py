from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from home.models import Thread


class ThreadListView(ListView):
    model = Thread
    template_name = "home/threads_list.html"
    paginate_by = 4
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Forum Anasayfa"
        return context