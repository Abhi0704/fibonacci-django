from django.contrib import admin
from django.urls import path

from fibprint.views import MyView

urlpatterns = [
    path('home',MyView.as_view()),
]
