from django.urls import path
from .views.main_view import index,create_employee,edit_employee
from .views.auth_view import login_page

urlpatterns = [
    path('',index, name='index'),
    path('login/',login_page, name='login'),
    path('create/',create_employee, name="create"),
    path('edit/',edit_employee, name="edit")
]
