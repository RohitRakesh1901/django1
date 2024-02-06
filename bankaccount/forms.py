from django import forms
class inputform(forms.Form):
    name=forms.CharField(max_length= 255,label="Enter your name")
    dob = forms.DateField(label="Select your date of birth")
    sin = forms.IntegerField(label="Enter your Social Insurance Number")
