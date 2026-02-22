from django.urls import path

from main.views import *

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('code_detail/<int:pk>/', CodeDetail.as_view(), name='code_detail')
]