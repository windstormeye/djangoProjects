from django.contrib import admin
from .models import ReadNum, ReadDetails


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')


@admin.register(ReadDetails)
class ReadNumDetailsAdmin(admin.ModelAdmin):
    list_display = ('date', 'read_num', 'content_object')
