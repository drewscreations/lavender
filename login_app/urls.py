from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signin', views.signin),
    path('register', views.register),
    path('validateNewUser', views.validateNewUser),
    path('validateExistingUser', views.validateExistingUser),
    path('logout', views.logout),
    path('users/new', views.addNewUser),
    path('users/edit/<int:my_id>', views.editUser),
    path('validateEditUserName/<int:my_id>', views.validateEditUserName)
]
