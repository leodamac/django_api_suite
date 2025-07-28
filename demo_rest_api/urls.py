from django.urls import path
from . import views


urlpatterns = [
    path("index/", views.DemoRestApi.as_view(), name="demo_rest_api_resources"),
    path("index/<str:id>/", views.DemoRestApi.as_view(), name="demo_rest_api_detail"),

]
# This file defines the URL patterns for the demo_rest_api application.