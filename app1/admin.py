from django.contrib import admin

# Register your models here.
from .models import Course, Tag
admin.site.register(Course)
admin.site.register(Tag)