from django.urls import path
from .views_front import (
    Cookie_standsCreateView,
    Cookie_standsDeleteView,
    Cookie_standsDetailView,
    Cookie_standsListView,
    Cookie_standsUpdateView,
)

urlpatterns = [
    path("", Cookie_standsListView.as_view(), name="Cookie_stands_list"),
    path("<int:pk>/", Cookie_standsDetailView.as_view(), name="Cookie_stands_detail"),
    path("create/", Cookie_standsCreateView.as_view(), name="Cookie_stands_create"),
    path("<int:pk>/update/", Cookie_standsUpdateView.as_view(), name="Cookie_stands_update"),
    path("<int:pk>/delete/", Cookie_standsDeleteView.as_view(), name="Cookie_stands_delete"),
]
