from django import forms
class StudentForm(forms.Form):
    firstname=forms.CharField(label="enter firstname",max_length=50)
    lastname=forms.CharField(label="enter last name",max_length=10)
    email=forms.EmailField(label="enter Email")
    file=forms.FileField()