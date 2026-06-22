from django.utils import timezone
from actions.handlers import HANDLERS
from actions.models import (
    WorkflowExecution,
    StepExecution,
)


class WorkflowRunner:

    def run(self, workflow, input_data=None):

        input_data = input_data or {}

        execution = WorkflowExecution.objects.create(
            workflow=workflow,
            status="running",
            input_data=input_data,
        )

        context = input_data.copy()

        try:

            for step in workflow.steps.all():

                handler = HANDLERS.get(
                    step.step_type
                )

                if handler:

                    context = handler.run(
                        step.config,
                        context
                    )

                StepExecution.objects.create(
                    execution=execution,
                    workflow_step=step,
                    status="success",
                    input_data=input_data,
                    output_data=context,
                )

            execution.status = "completed"
            execution.output_data = context
            execution.completed_at = timezone.now()
            execution.save()

        except Exception as e:

            execution.status = "failed"
            execution.error_message = str(e)
            execution.completed_at = timezone.now()
            execution.save()

        return execution