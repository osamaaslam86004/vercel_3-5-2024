from django.urls import path
from Homepage import views
from Homepage.views import HomePageView



urlpatterns = [
    path("", HomePageView.as_view(), name="Home"),
]
