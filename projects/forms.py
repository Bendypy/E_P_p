from django import forms
from . import models
from django.utils.translation import gettext as _

attrs = { 'class': 'form-control'}

class ProjectCreateForm(forms.ModelForm):#صرحنا عن الصنف والصنف يرث من 
    class Meta:
        model = models.Project#النموزج  المستهدف
        fields = ['category', 'title', 'description']# الحقول المطلوبة
        fields =  {
            'category': _('Category'),
            'title': _('Title'),
            'description': _('Description'),
        }
        widgets = {#خاصية لتحديد الحقول
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs)
        }
        
        
        
        
class ProjectUpdateForm(forms.ModelForm):#صرحنا عن الصنف والصنف يرث من 
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'status']
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'status': forms.Select(attrs=attrs)
        }