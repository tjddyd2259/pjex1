from bookmark.models import Bookmark # 테이블 조회를 위해 모델 클래스를 임포트 
from django.views.generic import ListView, DetailView # 클래스형 제네릭 뷰를 사용하기 위해 임포트 

class BookmarkLV(ListView):    # 테이블의 레코드 리스트를 보여주기 위한 뷰
    model = Bookmark

class BookmarkDV(DetailView):  # 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한 뷰
    model = Bookmark
