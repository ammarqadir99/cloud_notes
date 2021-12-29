from django.urls import path, re_path
from . import views

from rest_framework import routers


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    re_path('task-list/?', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('task-create/', views.taskCreate, name="task-Create"),
    # path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    re_path('task-update/(?P<pk>\w+)/?$', views.taskUpdate, name="task-update"),
    # re_path(r'^(?P<slug>\w+)/$', indexView.as_view() ,name = 'index'),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]

