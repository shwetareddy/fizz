from django.conf.urls import url
from fizzbuzz.views  import FizzBuzzView, FizzBuzzDetailView

urlpatterns = [
    url(r'^fizzbuzz/$', FizzBuzzView.as_view()),
    url(r'^fizzbuzz/(?P<pk>[0-9]+)/$', FizzBuzzDetailView.as_view()),
]