from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Workflow
from .serializers import WorkflowSerializer, WorkflowStepSerializer


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

@api_view(["GET", "POST"])
def workflow_steps(request, workflow_id):

    workflow = get_object_or_404(Workflow, id=workflow_id)
    if request.method == "GET":

        serializer = WorkflowStepSerializer(workflow.steps.all(), many=True)
        return Response(serializer.data)

    data = request.data.copy()
    data["workflow"] = workflow.id

    serializer = WorkflowStepSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_step(request, step_id):

    step = get_object_or_404(WorkflowStep, id=step_id)
    step.delete()
    return Response({"message": "Step deleted."})