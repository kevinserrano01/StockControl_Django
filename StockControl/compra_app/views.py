from django.shortcuts import render, redirect
from compra_app.models import Producto, Proveedor
from compra_app.forms import CreateNewProduct, CreateNewSupplier

def productos(request):
    """Trae y muestra todos los productos de la base de datos"""
    productos = Producto.objects.all()
    contex = {
        'productos': productos
    }
    return render(request, 'productos.html', contex)


def crear_producto(request):
    """CREA NUEVO PRODUCTO"""
    if request.method == 'GET':
        return render(request, 'nuevo_producto.html', {
            'formularioProducto': CreateNewProduct()
        })
    else:
        proveedores = Proveedor.objects.all()

        context = {
            'proveedores': proveedores
        }

        nombreProduct = request.POST['nombre']  # guardo el nombre del proveedor
        precioProduct = request.POST['precio']  # guardo el nombre del proveedor
        stockProduct = request.POST['stock_actual']  # guardo el nombre del proveedor
        provedorSeleccionado = request.POST['proveedor']

        Producto.objects.create(nombre=nombreProduct, precio=precioProduct, stock_actual=stockProduct, proveedor_id=provedorSeleccionado)  # Creamos el proveedor en la base de datos
        return render(request, 'nuevo_producto.html', context)

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect("productos")

def proveedores(request):
    """Trae y muestra todos los proveedores de la base de datos"""
    proveedores = Proveedor.objects.all()
    contex = {
        'proveedores': proveedores
    }
    return render(request, 'proveedores.html', contex)


def crear_proveedor(request):
    """CREA NUEVO PROVEEDOR"""
    # print(request.POST) # QueryDict = {} Trae los datos que se guarda en el formulario
    if request.method == 'GET':
        return render(request, 'nuevo_proveedor.html', {
            'formularioProveedor': CreateNewSupplier()
        })
    else:
        nombreProveedor = request.POST['nombre'] #guardo el nombre del proveedor
        apellidoProveedor = request.POST['apellido']  # guardo el nombre del proveedor
        dniProveedor = request.POST['dni']  # guardo el nombre del proveedor
        Proveedor.objects.create(nombre=nombreProveedor, apellido=apellidoProveedor, dni=dniProveedor)  # Creamos el proveedor en la base de datos
        return redirect('proveedores')  # redirecciona a la url con el name='proveedores' en urls.py

def eliminar_proveedor(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    proveedor.delete()
    return redirect("proveedores")