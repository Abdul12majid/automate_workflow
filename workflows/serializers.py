from rest_framework import serializers
from .models import Workflow, WorkflowStep


class WorkflowStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowStep
        fields = "__all__"


class WorkflowSerializer(serializers.ModelSerializer):
    steps = WorkflowStepSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Workflow
        fields = "__all__"