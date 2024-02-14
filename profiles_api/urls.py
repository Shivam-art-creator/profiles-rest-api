

from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

# Create a router instance
router = DefaultRouter()

# Register the HelloViewSet with the router
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)


# Define urlpatterns for your Django application
urlpatterns = [
    # Define a path for a regular Django view
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),

    # Include the URLs generated by the router
    path('', include(router.urls)),
]

