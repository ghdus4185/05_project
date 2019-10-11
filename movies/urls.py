from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index),

    # 정보 입력 받기 (Create)
    path('new/', views.form),
    # 정보 생성 (Create)
    path('create/', views.create),
    # 수정 하기(Update)
    path('<int:id>/edit/', views.edit),
    # 상세 보기(Read)
    path('<int:id>/detail/', views.detail),
    # 삭제하기(Delete)
    path('<int:id>/delete/', views.delete),
    path('<int:id>/update/', views.update),
]
