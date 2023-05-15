from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # adminKev - adminKev
    path('compras/', include('compra_app.urls')) # Disponible todas las urls de la aplicacion compra_app
]
