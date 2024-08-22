from django.urls import path
from sales import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
