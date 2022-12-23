from django.urls import path
from . import views
urlpatterns = [
path('<int:pk>/', views.view_lists, name='view_lists'),
path('<int:pk>/add_item', views.add_item_to_list, name='add_item_to_list'),
path('new', views.new_list,              name='new_list')
]