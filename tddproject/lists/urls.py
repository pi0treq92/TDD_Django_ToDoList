from django.urls import path
from lists.views import view_list, new_list, index_page, new_item

app_name = 'lists'

urlpatterns = [
    path('new', new_list, name='new_list'),
    path('<int:pk>/', view_list, name='view_list'),
    path('<int:pk>/new_item', new_item, name='new_item'),
]