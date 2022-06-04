from django import forms
from Hammer.models import Empleado,Empleador,Servicio,Contacto

class Contacto_form(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
    
    nombre = forms.CharField(label='Nombre:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Nombre',
                                    }))
    apellido = forms.CharField(label='Apellido:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Apellido',
                                    }))
    telefono = forms.CharField(label='Teléfono:',max_length=12,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'4421234567',
                                    }))
    email = forms.EmailField(label='Email:',max_length=254,
                                    widget=forms.EmailInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'ejemplo@ejemplo.com',
                                    }))

class Servicio_form(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        
    nombre = forms.CharField(label='Nombre:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Nombre',
                                    }))
    descripcion = forms.CharField(label='Descripción:',max_length=250,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Descripción',
                                    }))
    provincia =forms.CharField(label='Provincia:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Provincia',
                                    }))
    ciudad = forms.CharField(label='Ciudad:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Ciudad',
                                    }))
    empleado = forms.CharField(label='Empleado:',max_length=12,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Nombre del Empleado',
                                    }))
    precio = forms.FloatField(label='Precio:',
                                    widget=forms.NumberInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'100',
                                    }))
        
class Empleado_form(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
    
    nombre = forms.CharField(label='Nombre:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Nombre',
                                    }))
    apellido = forms.CharField(label='Apellido:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Apellido',
                                    }))
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento: ',
                                    widget=forms.SelectDateWidget(years=range(1900,2022),
                                    attrs={
                                        'class':'form-control',
                                    }))
    experiencia = forms.CharField(label='Experiencia:',max_length=2,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Ingrese la experiencia en años',
                                    }))
    provincia =forms.CharField(label='Provincia:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Provincia',
                                    }))
    ciudad = forms.CharField(label='Ciudad:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Ciudad',
                                    }))
    telefono = forms.CharField(label='Teléfono:',max_length=12,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'4421234567',
                                    }))
    email = forms.EmailField(label='Email:',max_length=254,
                                    widget=forms.EmailInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'ejemplo@ejemplo.com',
                                    }))


class Empleador_form(forms.ModelForm):
    class Meta:
        model = Empleador
        fields = '__all__'
    
    nombre = forms.CharField(label='Nombre:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Nombre',
                                    }))
    apellido = forms.CharField(label='Apellido:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Apellido',
                                    }))
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento: ',
                                    widget=forms.SelectDateWidget(years=range(1900,2022),
                                    attrs={
                                        'class':'form-control',
                                    }))
    provincia =forms.CharField(label='Provincia:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Provincia',
                                    }))
    ciudad = forms.CharField(label='Ciudad:',max_length=15,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'Ciudad',
                                    }))
    telefono = forms.CharField(label='Teléfono:',max_length=12,
                                    widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'4421234567',
                                    }))
    email = forms.EmailField(label='Email:',max_length=254,
                                    widget=forms.EmailInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'ejemplo@ejemplo.com',
                                    }))