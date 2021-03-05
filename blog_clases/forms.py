from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    
    username = forms.CharField(required=True, 
                                min_length=4, max_length=50,
                                widget=forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'id':'username'
                                    }
                                ))

    first_name = forms.CharField(label='Nombre',
                            required=False, 
                            min_length=4, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'id':'name'
                                }
                            ))

    last_name = forms.CharField(label='Apellido',
                            required=False, 
                            min_length=4, max_length=50,
                            widget=forms.TextInput(
                                attrs={
                                    'class':'form-control',
                                    'id':'last_name'
                                }
                            ))

    email = forms.EmailField(required=True, 
                                widget=forms.EmailInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'example@itat.edu.ve',
                                    }
                                ))

    password = forms.CharField(required=True, 
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class':'form-control',
                                    }
                                ))

    password2 = forms.CharField(required=True, 
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class':'form-control',
                                    }
                                ))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya esta en uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya esta en uso')
        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'La contraseña no coincide')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
        )
        
