from django import forms

class NameForm(forms.Form):
    firstName = forms.CharField(label='first name ', max_length=100)
    lastName = forms.CharField(label='last name', max_length=100, required=False)
    picture= forms.ImageField(label='your image', required= False)
    profileVideo = forms.FileField(label='your profile video', required= False)
