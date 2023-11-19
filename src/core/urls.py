from typing import Any
from rest_framework.routers import DefaultRouter
from .views import DataModelViewSet

router = DefaultRouter()
router.register(r"datas", DataModelViewSet)

urlpatterns: list[Any] = [] + router.urls
