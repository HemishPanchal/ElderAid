from django import forms
from elder_services.models import user_info
# Signup form using Django's built-in user model
class SignupForm(forms.ModelForm):
    class Meta:
        model = user_info
        fields = ("uname","pwd")  # Password fields handled automatically

    def __init__(self,*args,**kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)
        self.fields['uname'].label="Username"    
        self.fields['pwd'].label="Password"
        self.fields['pwd'].widget = forms.PasswordInput()  # 👈 make input type="password"

class LoginForm(forms.ModelForm):
    class Meta:
        model = user_info
        fields = ("uname","pwd") 

    def __init__(self,*args,**kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields['uname'].label="Username"    
        self.fields['pwd'].label="Password"
        self.fields['pwd'].widget = forms.PasswordInput()  # 👈 make input type="password"
    