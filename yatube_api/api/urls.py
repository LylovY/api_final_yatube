from django.urls import include, path

from .routers import router_v1

app_name = 'api'

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
