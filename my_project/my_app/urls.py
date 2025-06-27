from django.urls import path
from .views.main_view import index,create_employee,edit_employee,delete_data
from .views.auth_view import login_page

urlpatterns = [
    path('',index, name='index'),
    path('login/',login_page, name='login'),
    path('create/',create_employee, name="create"),
    path('edit/<int:id>',edit_employee, name="edit"),
    path('delete/<int:emp_id>',delete_data, name="delete")
]

