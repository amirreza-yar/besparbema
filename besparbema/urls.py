from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flatpages.urls')),
] + static('/static/', document_root=settings.STATIC_ROOT)

handler404 = "flatpages.views.comming_soon"
# handler500 = "flatpages.views.comming_soon"
# handler403 = "flatpages.views.comming_soon"
# handler400 = "flatpages.views.comming_soon"