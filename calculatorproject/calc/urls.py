from django.urls import path

from calc import views

urlpatterns=[
    path('',views.home),
    path('add',views.addfun,name='add'),
    path('sub',views.subfun,name='sub'),
    path('multi', views.multifun, name='multi'),
    path('div',views.divfun, name='div'),

]