from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalityTestViewSet

router = DefaultRouter()
router.register(r'personality-tests', PersonalityTestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
