from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'Programmers', views.ProgrammerViewSet)
router.register(r'Aprendiz', views.AprendizViewSet)

urlpatterns = [
    path('', include(router.urls)),
]