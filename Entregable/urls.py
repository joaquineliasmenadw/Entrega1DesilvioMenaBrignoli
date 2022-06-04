from django.contrib import admin
from django.urls import path, include
from Entregable.views import index

urlpatterns = [
    path('', include('Hammer.urls')),
    path('admin/', admin.site.urls),
    path('Hammer/', include('Hammer.urls')),
]
