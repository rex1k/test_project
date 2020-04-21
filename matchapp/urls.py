from django.urls import path
from matchapp import views
app_name = 'matchapp'

urlpatterns = [
    path('', views.MatchView.as_view()),
    path('<int:pk>', views.MatchView.as_view())
]