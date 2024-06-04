from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView
from django.conf.urls.static import static
from django.conf import settings
=======
>>>>>>> add-page-generator-model

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path("redoc/", SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/v1/', include('apps.page_generator.urls')),
=======
    path('api/v1/page-generator/', include('apps.page_generator.urls'))
>>>>>>> add-page-generator-model
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
