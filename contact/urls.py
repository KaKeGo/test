from django.urls import path

from .views import (
    contact_list_view,
)

app_name = 'contact'

urlpatterns = [
    path('', contact_list_view, name='contact'),
]
