from django import forms
from compra_app.models import Producto

class CreateNewProduct(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('__all__')  # TRAE TODO

    # Otra menera no recomendable
    # nombre = forms.CharField(label='Nombre del producto', max_length=200)
    # precio = forms.CharField(label='Precio', max_length=200)
    # stockActual = forms.CharField(label='Stock', max_length=200)
    # proveedor = forms.CheckboxSelectMultiple()

class CreateNewSupplier(forms.Form):
    nombre = forms.CharField(label='Nombre del proveedor', max_length=200)
    apellido = forms.CharField(label='Apellido del proveedor', max_length=200)
    dni = forms.IntegerField(label='dni del proveedor', max_value=99999999)