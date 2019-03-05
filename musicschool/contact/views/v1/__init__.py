from .contact import ContactViewSet
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"contacts", ContactViewSet)

v1_urls = router.urls