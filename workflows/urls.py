from django.urls import path
from .views import workflow_list

urlpatterns = [
    path("", workflow_list, name="workflow-list"),
    path("<int:workflow_id>/steps/", views.workflow_steps, name="workflow-steps"),
    path("steps/<int:step_id>/", views.delete_step, name="delete-step"),
]