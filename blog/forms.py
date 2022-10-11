from django import forms
from .models import Post

class PostForm(forms.ModelForm):   #PostForm 폼 변수. forms.ModelForm 모델폼이라는 것을 전달.
  
  class Meta:       #class Meta: 이 폼을 만들기 위해 어떤 model이 쓰이는지 전달.
    model = Post    # Post 모델.
    fields = ('title', 'text',)  # 필드에 title, text만 보여지게..