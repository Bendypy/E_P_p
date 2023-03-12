from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.
class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'
    
    
    
class ProjectCreateView(CreateView):
    model = models.Project#حددنا النموزج
    form_class = forms.ProjectCreateForm#حددنا الاستمارة
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')#رابط اعادة التوجيه
    







