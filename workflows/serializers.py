from rest_framework import serializers
from .models import Workflow, WorkflowStep


class WorkflowStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowStep
        fields = "__all__"


class WorkflowSerializer(serializers.ModelSerializer):

    webhook_url = serializers.SerializerMethodField()

    class Meta:
        model = Workflow
        fields = "__all__"

    def get_webhook_url(self, obj):
        return f"/api/webhook/{obj.webhook_key}/"