from django import forms
from django.core import validators
class TopicForm(forms.Form):
    tname=forms.CharField(max_length=100,validators=[validators.MinLengthValidator(3)])
    tage=forms.IntegerField(validators=[validators.MaxValueValidator(22)])
    mob=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])