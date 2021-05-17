from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV  # URLconf에서 뷰 호출하므로 뷰 모듈 관련 클래스 임포트 

app_name = 'bookmark'
urlpatterns = [
    
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/',BookmarkDV.as_view(), name='detail'),    
]