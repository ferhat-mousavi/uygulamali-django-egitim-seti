from django.contrib import admin

from home.models import Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'score', 'created_at', 'updated_at')
    ordering = ('-created_at',)
