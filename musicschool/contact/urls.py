from django.urls import include, path
from api.views import v1_urls


urlpatterns = [path("v1/", include(v1_urls))]