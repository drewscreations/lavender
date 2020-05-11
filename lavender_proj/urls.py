from django.urls import path, include

urlpatterns = [
    path('', include('login_app.urls')),
    path('dashboard', include('dashboard_app.urls'))
]
