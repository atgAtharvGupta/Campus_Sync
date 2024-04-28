from django import forms
from Resources.models import Department 

class AddForm(forms.Form):
    
    # Department = forms.CharField(required=False, max_length=128, error_messages={
    #     'required': 'Please write your old password'}, widget=forms.Select(choices=Department,attrs={ 'rows': 2} ))
    Thesis_Name = forms.CharField(required=True, max_length=128,  widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Thesis Name'}))
    Description= forms.CharField(required=True, max_length=1500, widget=forms.Textarea({'class': 'form-control', 'placeholder': 'Description'}))
    Area=forms.CharField(required=True, max_length=128, label="Area/Field", widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Area/Field'}))
    Technology_used = forms.CharField(required=True, max_length=128,  widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Technology used'}))
    Student_Name = forms.CharField(required=True, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Student Name'}))
    Enrollment = forms.CharField(required= True, max_length=64, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Enrollment Number'}))
    # DOS = forms.DateField(required=False, max_length=10, error_messages={
    #     'required': 'Please write your old password'}, widget=forms.DateField({'class': 'form-control','placeholder': 'Date of submission'}))
    Pdf = forms.FileField(required= True, label="Thesis File", widget=forms.FileInput({'class': 'form-control', 'accept': 'text/csv'})) 