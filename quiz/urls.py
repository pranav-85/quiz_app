from django.urls import path
from . import views
urlpatterns = [
    path('api/questions/', views.QuestionListView.as_view(), name='question-list'),
]