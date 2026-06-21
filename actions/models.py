from django.db import models
from workflows.models import Workflow, WorkflowStep


class WorkflowExecution(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("running", "Running"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name="executions")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    input_data = models.JSONField(default=dict)
    output_data = models.JSONField(default=dict, blank=True)
    error_message = models.TextField(blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.workflow.name} ({self.status})"


class StepExecution(models.Model):
    STATUS_CHOICES = [
        ("success", "Success"),
        ("failed", "Failed"),
    ]
    execution = models.ForeignKey(WorkflowExecution, on_delete=models.CASCADE, related_name="steps")
    workflow_step = models.ForeignKey(WorkflowStep, on_delete=models.CASCADE )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    input_data = models.JSONField(default=dict)
    output_data = models.JSONField(default=dict)
    error_message = models.TextField(blank=True)
    executed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Step {self.workflow_step.order}"