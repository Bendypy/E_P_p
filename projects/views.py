from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin

from django.core.mail import EmailMessage
from django.shortcuts import render
from .models import Report


# Create your views here.
#واجهةالعرض
class ProjectListView(LoginRequiredMixin, ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 4
    
    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id': self.request.user}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)
        
    
    
    #صنف انشاء  المشروع
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project#حددنا النموزج المستهدف
    form_class = forms.ProjectCreateForm#حددنا الاستمارة
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')#رابط اعادة التوجيه
    
    
    def  form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

#صنف تعديل  المشروع
class ProjectUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = models.Project#حددنا النموزج
    form_class = forms.ProjectUpdateForm#حددنا الاستمارة
    template_name = 'project/update.html'
    
    
    def  test_func(self):
        return self.get_object().user_id == self.request.user.id
   
   
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id]) 
    
    python -m venv venv 
class ProjectDeleteView(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = models.Project  
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_list') 
    
    def  test_func(self):
        return self.get_object().user_id == self.request.user.id
    
class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):#مع تعامل مع عملية انشاء المهمة
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']#نريد post فقط
    
    def  test_func(self):
        project_id  =  self.request.POST.get('project', '')
        return models.Project.objects.get(pk=project_id).user_id == self.request.user.id
    
    
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])
    
    
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']
    
    
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])
    
    



class TaskDeleteView(LoginRequiredMixin ,DeleteView):
    model = models.Task
    
    
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])
    
    
    
def send_report(request):
    if request.method == 'POST':
        sender_email = request.POST['sender_email']
        recipient_email = request.POST['recipient_email']
        report_text = request.POST['report_text']
        report = Report(sender_email=sender_email, recipient_email=recipient_email, report_text=report_text)
        report.save()
        subject = 'New Report'
        body = 'Sender Email: {}\nReport Text: {}'.format(sender_email, report_text)
        email = EmailMessage(subject, body, to=[recipient_email])
        email.send()
        return render(request, 'success.html')
    else:
        return render(request, 'send_report.html')