from django.shortcuts import render
from django.views import View
from .models import Listjobs, Content, Listblog
from django.core.paginator import Paginator, EmptyPage
# Create your views here.


class Indexjob(View):
    def get(self, request):
        name = Listjobs.objects.all()

        p = Paginator(name, 10)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        contents = {'name': page}
        return render(request, 'indexjob.html', contents)

class Indexlibra(View):
    def get(self, request):
        name_blog = Content.objects.all()
        tit_blog = Listblog.objects.all()

        contents = {'name_blog': name_blog, 'tit_name': tit_blog}

        return render(request, 'index.html', contents)