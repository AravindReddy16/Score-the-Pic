from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainPage,name="mainpage"),
    path('count/<str:id>/',views.count,name="count"),
]