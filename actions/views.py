from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from workflows.models import Workflow
from actions.models import WorkflowExecution
from actions.services.runner import WorkflowRunner
from .serializers import WorkflowExecutionSerializer


@api_view(["POST", "GET"])
def run_workflow(request, workflow_id):

    workflow = Workflow.objects.get(id=workflow_id)
    runner = WorkflowRunner()
    execution = runner.run(workflow,request.data)

    serializer = WorkflowExecutionSerializer(execution)

    return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(["GET"])
def execution_list(request):

    executions = WorkflowExecution.objects.all()

    serializer = WorkflowExecutionSerializer(executions,many=True)

    return Response(serializer.data)