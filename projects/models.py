from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.
#اذا نعرف صنف جديد يدعى 
class Category(models.Model): #هذا الصنف يرث من الصنق (models.Modles
    name = models.CharField(max_length=255)#الطول الاعظمي 255)#  احد حقول النموزج هذا الحقل اسم النموزج
    
    def __str__(self):# هذه الدالة str تنعيد لنا النتيجة عند تحويل الصنف الى سلسة نصية
        return self.name# يمكن ان نعيد الخاصية name الى سلسلة نصية
    
    
class ProjectStatus(models.IntegerChoices):# نموزج مساعد  
    PENDING = 1, 'Pending'
    COMPLETED = 2, 'Completed'
    POSTPONED = 3, 'postponed'
    CANCELED = 4, 'Canceled'

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(#حقل يعبر عن الحالة من النوع int
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)#DateTimeField لتخزين التاريخ والوقت
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)#العلاقة واحد الى كثيرالنموزج Category
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE)#نصرح عن العلاقة بين النموزج والمشروع لكن لسنا بحاجة للتعريف ب الuser فعليا حيث يقدم لنا django لنا ذلك ذلم بشكل ضمني 
    
     
     
    def __str__(self):# هذه الدالة str تنعيد لنا النتيجة عند تحويل الصنف الى سلسة نصية
        return self.title
    
    
    
class Task(models.Model):#تصميم النموزج Task
    description = models.TextField()#اولا لدينا وصف المهمى 
    is_completed = models.BooleanField(default=False)#لدينا حقل يعبر عن حالة المهمة 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)#حقل تمثيل العلاقة
    
    def __str__(self):# هذه الدالة str تنعيد لنا النتيجة عند تحويل الصنف الى سلسة نصية
        return self.description
    
    
    
    
    

    
    