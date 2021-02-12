from django import forms
from .models import user,perrito

class UserForm(forms.ModelForm):
    class Meta:
        model=user
        widgets = {
        'Clave': forms.PasswordInput(),}
        fields=('Email','Nombre','FechaNacimiento','Telefono','Usuario','Clave','Rut')
    
class PerritoForm(forms.ModelForm):
    class Meta:
        model=perrito
        fields=('Foto','Nombre','Raza','Descripcion','Estado')



