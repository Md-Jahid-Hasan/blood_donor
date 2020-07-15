from django import forms
from .models import User
from django.contrib.auth import authenticate


class LoginForm(forms.ModelForm):
    password = forms.CharField(label="Your Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password',
                                                                                        'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email',
                                            'type': 'email'}),
        }

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            user = User.objects.filter(email=email)
            print(user)
            if len(user) == 0:
                raise forms.ValidationError("No User Exists")
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class CreateUserForm(forms.ModelForm):
    # password = forms.CharField(label="Your Password",widget=forms.PasswordInput(attrs={'placeholder':'Enter Password',
    #                                                                                     'class': 'form-control'})),
    password1 = forms.CharField(label='Retype Your Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Retype Password',
                                                                  'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_of_birth', 'password')


        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email',
                                            'type': 'email'}),
            'first_name': forms.TextInput(attrs={'label': "Enter Your First Name",
                                                 'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'label': 'Enter Last Name',
                                                'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Enter Your Password',
                                                   })
        }

    def clean(self):
        pas1 = self.cleaned_data['password']
        pas2 = self.cleaned_data['password1']

        if pas1 != pas2:
            raise forms.ValidationError("Password Dosen't match")

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            if len(User.objects.filter(email=email)) != 0:
                raise forms.ValidationError("Olreday Exists")
        return email



