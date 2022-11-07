from django.urls import path

from .views import (
    meme_list_view,
    meme_detail_view,
    meme_create_view,
    MeMe_Update_View,
    MeMe_Delete_View,
    
    category_list_view,
    category_create_view,
    
    memefilters_list_view,
    memefilters_create_view,
)

app_name = 'meme'

urlpatterns = [
    path('', meme_list_view, name='meme_list'),
    path('create/', meme_create_view, name='meme_create'),
    
    path('category/', category_list_view, name='meme_category'),
    path('category/create/', category_create_view, name='meme_category_create'),
    
    path('filters/', memefilters_list_view, name='meme_filters'),
    path('filters/create/', memefilters_create_view, name='meme_filters_create'),
    
    #Pk path
    path('<str:pk>/', meme_detail_view, name='meme_detail'),
    path('<str:pk>/update/', MeMe_Update_View.as_view(), name='meme_update'),
    path('<str:pk>/delete/', MeMe_Delete_View.as_view(), name='meme_delete'),
]