from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .views import TaskView

class MetaController(APIView):
    def get(self, request):
        task_view = TaskView()
        return task_view.get(request)

    def post(self, request):
        task_view = TaskView()
        return task_view.post(request)