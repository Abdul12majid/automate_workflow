from django.db import models


class Workflow(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WorkflowStep(models.Model):

    STEP_TYPES = [
        ("extract_data", "Extract Data"),
        ("create_record", "Create Record"),
        ("send_email", "Send Email"),
        ("generate_report", "Generate Report"),
        ("http_request", "HTTP Request"),
    ]

    workflow = models.ForeignKey(
        Workflow,
        on_delete=models.CASCADE,
        related_name="steps"
    )

    order = models.PositiveIntegerField()

    step_type = models.CharField(
        max_length=50,
        choices=STEP_TYPES
    )

    config = models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

        unique_together = (
            "workflow",
            "order",
        )

    def __str__(self):
        return f"{self.workflow.name} - Step {self.order}"