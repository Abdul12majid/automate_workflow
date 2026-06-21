from rest_framework import serializers
from .models import WorkflowExecution, StepExecution


class StepExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepExecution
        fields = "__all__"


class WorkflowExecutionSerializer(serializers.ModelSerializer):
    steps = StepExecutionSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = WorkflowExecution
        fields = "__all__"