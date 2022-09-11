from django import forms
from django.forms import *
from .models import *


class TodoForm(ModelForm):
    class Meta:

        model = TodoModel
        fields = '__all__'