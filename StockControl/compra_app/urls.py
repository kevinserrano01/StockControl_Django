from django.urls import path
from . import views

urlpatterns = [
    path('productos/listado/', views.productos, name='productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/eliminar/<int:producto_id>', views.eliminar_producto, name='eliminar_producto'),
    path('proveedores/listado/', views.proveedores, name='proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/eliminar/<int:proveedor_id>', views.eliminar_proveedor, name='eliminar_proveedor'),
]