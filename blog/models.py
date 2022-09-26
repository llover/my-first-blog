from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): #클래스(객체, 모델) 정의 Post는 모델변수의 이름으로 첫글자는 반드시 대문자여야 함. models는 장고 모델을 의미함으로써, Post가 db에 저장되어야 함을 의미.
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #Foreignkey는 다른 모델에 대한 링크.
  title = models.CharField(max_length=200) # CharField 글자수 제한 텍스트.
  text = models.TextField() #TextField 글자수무제한 텍스트
  created_date = models.DateTimeField(default=timezone.now) # DateTimeFiel 날짜와 시간
  published_date = models.DateTimeField(blank=True, null=True)
  
  def publish(self): #def는 함수선언, publish는 method
    self.published_date = timezone.now()
    self.save()
    
  def __str__(self): #  str를 호출.  제목 텍스트 
      return self.title
  

# Create your models here.
