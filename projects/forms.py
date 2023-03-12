from django import forms
    
from . import models



class ProjectCreateForm(forms.ModelForm):#صرحنا عن الصنف والصنف يرث من ()
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        widgets = {
            'category': forms.Select(),
            'title': forms.TextInput(),
            'description': forms.Textarea()
        }