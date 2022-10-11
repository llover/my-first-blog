from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #blog.views.post_detail는 뷰경로,  blog는 디렉토리, viwes는 views.py파일명, post_detail은 view이름.
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
# pk는 데이터베이스의 각 레코드 식별 기본키(primary key), post모델에서 기본키를 지정하지 않았기 때문에 pk라는 필드를 추가해 새로운 블로그 게시물이 추가될 때 1,2,3 등으로 식별되도록 ..
#post 객체의 다른 필드에 엑세스하는 것과 같은 방식으로 post.pk를 작성하여 기본키에 엑섹스되도록 한다.