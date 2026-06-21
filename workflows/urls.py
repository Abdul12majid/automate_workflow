from django.urls import path
from .views import workflow_list

urlpatterns = [
    path("", workflow_list, name="workflow-list"),
]