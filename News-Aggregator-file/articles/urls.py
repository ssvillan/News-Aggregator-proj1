from django.urls import path

from .views import HomePageView


urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"), # as_views() because of class-based views
]
