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

        current_step = (
            workflow.steps
            .order_by("order")
            .first()
        )

        try:

            while current_step:

                handler = HANDLERS.get(
                    current_step.step_type
                )

                if not handler:
                    raise Exception(
                        f"No handler for '{current_step.step_type}'"
                    )

                result = handler.run(
                    current_step.config,
                    context
                )

                # Condition step
                if current_step.step_type == "condition":

                    StepExecution.objects.create(
                        execution=execution,
                        workflow_step=current_step,
                        status="success",
                        input_data=context,
                        output_data={
                            "result": result
                        },
                    )

                    if result:
                        current_step = current_step.true_step
                    else:
                        current_step = current_step.false_step

                    continue

                # Normal steps
                context = result

                StepExecution.objects.create(
                    execution=execution,
                    workflow_step=current_step,
                    status="success",
                    input_data=input_data,
                    output_data=context,
                )

                current_step = (
                    workflow.steps
                    .filter(
                        order__gt=current_step.order
                    )
                    .order_by("order")
                    .first()
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