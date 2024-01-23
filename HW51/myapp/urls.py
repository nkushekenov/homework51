from django.urls import path
from .views import TaskView
from .metacontroller import  MetaController

urlpatterns = [
    path('task/', TaskView.as_view(), name='task-view'),
    path('', MetaController.as_view(), name='meta-controller'),
]