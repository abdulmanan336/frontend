
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('form', views.form, name='form'),
    path('view/<id>', views.view, name='view'),
    path('del/<id>', views.del_contact, name='del'),
    path('search', views.search, name='search'),
]
