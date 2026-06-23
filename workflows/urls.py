from django.urls import path
from . import views

urlpatterns = [
    path("", views.workflow_list, name="workflow-list"),
    path("<int:workflow_id>/steps/", views.workflow_steps, name="workflow-steps"),
    path("steps/<int:step_id>/", views.delete_step, name="delete-step"),
]