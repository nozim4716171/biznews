from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username= forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Parol',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Parolni takrorlang',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        
    def clean_password2(self):
        pass1 = self.cleaned_data['password1']
        pass2 = self.cleaned_data['password2']
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('Ikkala parol bir-biriga mos kelmadi.')
        return pass2
    

        
        
    
    
    