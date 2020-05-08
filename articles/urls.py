from django.contrib import admin
from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.details, name='details'),
    path('add_article/', views.add_article, name='add_article'),
]
