from django.urls import path

from home.views import ThreadListView

urlpatterns = [
    path('', ThreadListView.as_view(), name='threads_list')
]