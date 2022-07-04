from django.contrib import admin
from .models import Listjobs, Listblog, Content
# Register your models here.

class Hostlistjob(admin.ModelAdmin):
    list_display = ('title_job', 'date_job')
admin.site.register(Listjobs, Hostlistjob)

admin.site.register(Listblog)

class Hostcontents(admin.ModelAdmin):
    list_display = ('title_content', 'name_content')
    search_fields = ['title_content']
    list_filter = ['title_content']
admin.site.register(Content, Hostcontents)
