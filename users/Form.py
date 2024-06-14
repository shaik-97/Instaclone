#Forms
#=====
#html forms - text input, check box, fill in blaks, drop down
#route it to a url
#recomemded method is POST
#forms makes life easier
from django import forms
from .models import User, UserProfile

class UserSignUp(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta:
        # specifiying some meta info
        model = User
        exclude = ('created on', 'updated_on', 'is_Active')


