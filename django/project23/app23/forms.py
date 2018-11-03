from django  import forms
class EmployeeForm(forms.Form):
    sno = forms.IntegerField(label="enter no")
    name = forms.CharField(label="enter the name", max_length=50)
    cno = forms.IntegerField(label="enter contact no")
    file = forms.FileField()
