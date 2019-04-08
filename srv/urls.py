from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'fiboData$',views.fiboData, name='fiboData'),
]