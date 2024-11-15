from . import views
from django.urls import path

urlpatterns=[
    path('',views.calculator,name='calculator'),
    path('res/',views.result,name='result')
]