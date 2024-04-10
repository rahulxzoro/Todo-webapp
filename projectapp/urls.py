from django.urls import path
from . import views
app_name='todo'
urlpatterns = [
    path('',views.todo_list,name='todo_list'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete')

]