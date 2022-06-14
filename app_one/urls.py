from django.urls import path
from . import views


urlpatterns =[


    path('',views.index),
    path('create-movie',views.createMovie),
    path('list',views.list),
    path('info/<int:movieid>',views.info),




]



    
