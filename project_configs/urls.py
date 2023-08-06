from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from project_configs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('main_app.urls')),
] #+static(settings.STATIC_URL, document=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = views.error_400
handler404 = views.error_404
handler500 = views.error_500
