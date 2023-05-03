from django.db import models

from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext as _
# Create your models here.
#الافضل البدء بل الكيانات التي لا تمتلك حقول  علاقات ضمنها
#اذا نعرف صنف جديد يدعى 
class Category(models.Model): #هذا الصنف يرث من الصنق (models.Modles
    name = models.CharField(max_length=255)#الطول الاعظمي 255)#  احد حقول النموزج هذا الحقل اسم النموزج
    
    def __str__(self):# هذه الدالة str تعيد لنا النتيجة عند تحويل الصنف الى سلسة نصية
        return self.name# يمكن ان نعيد الخاصية name الى سلسلة نصية
    

    class  Meta:
        verbose_name = _('المعلمين')    
        verbose_name_plural = _('المعلمين') 
    
    
class ProjectStatus(models.IntegerChoices):# نموزج مساعد  
    PENDING = 1, _('Pending')# المشروع  قيد التنفيذ
    COMPLETED = 2, _ ('Completed') # اكتمل
    POSTPONED = 3, _ ('postponed')# موجل
    CANCELED = 4, _ ('Canceled')# الملغا
#النموزج الثاني
class Project(models.Model):
    title = models.CharField(max_length=255)#  خاصية  المشروعtitle والحقل CharField
    description = models.TextField()#الحقل الثاني الحقل الخاص بوصف المشروع ونواع الحقل  TextField
    status = models.IntegerField(#حقل يعبر عن الحالة من النوع int
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)#DateTimeField لتخزين التاريخ والوقت
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)#العلاقة واحد الى كثيرالنموزج Category
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,#نصرح عن العلاقة بين النموزج والمشروع لكن لسنا بحاجة للتعريف ب الuser فعليا حيث يقدم لنا django لنا ذلك ذلم بشكل ضمني 
         null=True
        )
        
     
     
    def __str__(self):# هذه الدالة str تنعيد لنا النتيجة عند تحويل الصنف الى سلسة نصية
        return self.title
    
    class  Meta:
        verbose_name = _('Project')    
        verbose_name_plural = _('Project') 
    
    
class Task(models.Model):#تصميم النموزج Task
    description = models.TextField()#اولا لدينا وصف المهمى 
    is_completed = models.BooleanField(default=False)#لدينا حقل يعبر عن حالة المهمة 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)#حقل تمثيل العلاقة
    
    def __str__(self):# هذه الدالة str تنعيد لنا النتيجة عند تحويل الصنف الى سلسة نصية
        return self.description
    
    class  Meta:
        verbose_name = _('مهمات')    
        verbose_name_plural = _('مهمات')
    
    
    
class Report(models.Model):
    sender_email = models.EmailField()
    recipient_email = models.EmailField()
    report_text = models.TextField()
    

    
    class Meta:
        
        verbose_name = 'ارسال التقارير'
        verbose_name_plural = 'ارسال التقارير'