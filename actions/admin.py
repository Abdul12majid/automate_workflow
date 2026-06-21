from django.contrib import admin
from .models import WorkflowExecution, StepExecution


@admin.register(WorkflowExecution)
class WorkflowExecutionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "workflow",
        "status",
        "started_at",
        "completed_at",
    )


@admin.register(StepExecution)
class StepExecutionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "execution",
        "workflow_step",
        "status",
        "executed_at",
    )