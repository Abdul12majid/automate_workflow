from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Workflow
from .serializers import WorkflowSerializer


@api_view(["GET", "POST"])
def workflow_list(request):

    if request.method == "GET":
        workflows = Workflow.objects.all()
        serializer = WorkflowSerializer(workflows, many=True)
        return Response(serializer.data)

    serializer = WorkflowSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)