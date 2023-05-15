from django.contrib import admin
from compra_app.models import Proveedor, Producto

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    # Metodos del admin
    list_display = ("id", "nombre", "precio", "stock_actual", "proveedor")
    search_fields = ("nombre", )

class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    # Metodos
    list_display = ("id", "nombre", "apellido", "dni")
    search_fields = ("nombre", )


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)