from django.urls import path

from . import views

urlpatterns = [
    path("executions/", views.execution_list,name="execution-list"),
    path("run/<int:workflow_id>/", views.run_workflow, name="run-workflow"),
]