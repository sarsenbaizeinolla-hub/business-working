from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Админ-панель остается отдельно
    path('', include('dashboard.urls')), # Все остальные страницы через ваше приложение
]