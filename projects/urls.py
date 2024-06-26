from django.urls import path

from projects import views
from projects.views import ShowProjectView

app_name = "projects"

urlpatterns = [
    path("add_project", views.add_project, name="add_project"),
    path("list_projects", views.list_projects, name="list_projects"),
    path(
        "show_project/<str:project_name>/",
        ShowProjectView.as_view(),
        name="show_project",
    ),
    path("info_panel/<str:mouse_id>/", views.info_panel, name="info_panel"),
    path(
        "add_mouse_to_project/<str:project_name>",
        views.add_mouse_to_project,
        name="add_mouse_to_project",
    ),
    path("edit_project/<str:project_name>", views.edit_project, name="edit_project"),
]
