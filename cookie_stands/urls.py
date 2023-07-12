from django.urls import path
from .views import Cookie_standsList, Cookie_standsDetail

urlpatterns = [
    path("", Cookie_standsList.as_view(), name="Cookie_stands_list"),
    path("<int:pk>/", Cookie_standsDetail.as_view(), name="Cookie_stands_detail"),
]
