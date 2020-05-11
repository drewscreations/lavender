from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/admin',views.index),
    path('/data', views.data),
    path('/addData', views.addDataPage),
    path('/api/data/new', views.validateNewData)
]
