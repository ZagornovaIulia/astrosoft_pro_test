from django.urls import path
from .views import PublicApiView
urlpatterns = [
    path('api/', PublicApiView.as_view(), name='unix_api'),
]
