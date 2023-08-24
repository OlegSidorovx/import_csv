from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ImportedFileViewSet, FileDataView, UserViewSet


router = DefaultRouter()
router.register(r'imported-files', ImportedFileViewSet, basename='importedfile')
router.register(r'file-data', FileDataView, basename='filedata')
router.register(r'users', UserViewSet)
router.register(r'imported-files', ImportedFileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
