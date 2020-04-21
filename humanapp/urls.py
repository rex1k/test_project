from django.contrib import admin
from django.urls import path
from humanapp import views
app_name = 'humanapp'

urlpatterns =[
    path('', views.HumanView.as_view()),
    path('<int:pk>', views.HumanView.as_view())
]