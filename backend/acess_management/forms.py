from django import forms

class YourForm(forms.Form):
    id = forms.IntegerField(label='ID')
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    phone = forms.IntegerField(label='Phone')
    gender = forms.CharField(max_length=10, label='Gender')
    address = forms.CharField(max_length=255, label='Address')
    city = forms.CharField(max_length=100, label='City')
    salary = forms.IntegerField(label='Salary')