from django.urls import path

from .views import (
    about_list_view,
)

app_name = 'about'

urlpatterns = [
    path('', about_list_view, name='about'),
]