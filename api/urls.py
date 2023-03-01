from django.urls import path
from . import views

urlpatterns = [
    path('scrapp',views.viewCalender),
]