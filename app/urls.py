from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    # url(r'fiboData$',views.fiboData, name='fiboData'),
]