from django.urls import path, include
from rest_framework import routers

from competence.views import CategorieView

router = routers.DefaultRouter()
router.register(f'categories',CategorieView)
urlpatterns = [
    path('',include(router.urls)),
]