from django.urls import path
from app01 import views

urlpatterns = [
    path('articles/<int:year>/' , views.article_year) ,
    path("sql_test" , views.sql_test) ,
    path("get_time" , views.current_datetime) ,
    path("index", views.index) ,


]