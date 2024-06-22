from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="website/", permanent=True)),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("breeding_cage/", include("breeding_cage.urls", namespace="breeding_cage")),
    path(
        "mice_repository/", include("mice_repository.urls", namespace="mice_repository")
    ),
    path("mice_requests/", include("mice_requests.urls", namespace="mice_requests")),
    path("projects/", include("projects.urls", namespace="projects")),
    path("stock_cage/", include("stock_cage.urls", namespace="stock_cage")),
    path("strain/", include("strain.urls", namespace="strain")),
    path("system_users/", include("system_users.urls", namespace="system_users")),
    path("wean_pups/", include("wean_pups.urls", namespace="wean_pups")),
    path("website/", include("website.urls", namespace="website")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
