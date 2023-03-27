from django import forms

from inicioApp.models import Usuario


class formulariouser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}
