from django.urls import path

from . import views


urlpatterns = [
    path('api/v1/task/list/', views.TasksList.as_view()),
    path('api/v1/task/create/', views.TaskCreate.as_view()),
    path('api/v1/task/<int:pk>/delete/', views.TaskDelete.as_view()),
    path('api/v1/task/<int:pk>/update/', views.TaskUpdate.as_view()),
]
