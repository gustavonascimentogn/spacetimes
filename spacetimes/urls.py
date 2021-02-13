from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

# API REST
from apps.arquivos.api.views import ArquivoViewSet
router = routers.DefaultRouter()
router.register(r'arquivos', ArquivoViewSet)




urlpatterns = [
    path('', include('apps.core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('arquivos/', include('apps.arquivos.urls')),

    #API REST
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
