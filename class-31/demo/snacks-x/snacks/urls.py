from django.urls import path
from .views import (
    SnackListView,
    SnackDetailView,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView,
    SnackListAPI,
    SnackDetailAPI,
)

urlpatterns = [
    path("", SnackListView.as_view(), name="snack_list"),
    path("<int:pk>/", SnackDetailView.as_view(), name="snack_detail"),
    path("create/", SnackCreateView.as_view(), name="snack_create"),
    path("<int:pk>/update/", SnackUpdateView.as_view(), name="snack_update"),
    path("<int:pk>/delete/", SnackDeleteView.as_view(), name="snack_delete"),

    path('api/v1/', SnackListAPI.as_view(), name='snack_list_api'),
    path('api/v1/<int:pk>', SnackDetailAPI.as_view(), name='snack_detail_api'),
]
