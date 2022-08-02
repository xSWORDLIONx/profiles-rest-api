from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('project-viewset', views.ProjectViewSet, base_name='project-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
