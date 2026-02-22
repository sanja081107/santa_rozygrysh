from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from main.models import *


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def home(request):
    context = {'title': 'Главная'}
    return render(request, 'main/index.html', context)

def search(request):
    q = request.GET.get('q')
    if q is not None and q != '':
        codes = Codes.objects.filter(code__startswith=q)[:10]
    elif q == '':
        codes = ''
    context = {'codes': codes}
    return render(request, 'main/search-results.html', context)

class CodeDetail(DetailView):
    model = Codes
    pk_url_kwarg = 'pk'
    context_object_name = 'el'
    template_name = 'main/code_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        el = Codes.objects.get(pk=self.kwargs['pk'])
        context['title'] = f"{el.code}"
        return context
