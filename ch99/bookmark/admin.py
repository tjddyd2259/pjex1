from django.contrib import admin
from bookmark.models import Bookmark

@admin.register(Bookmark)  # admin 사이트에 등록
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')

# admin.site.register(Bookmark, BookmarkAdmin)
# BookmarkAdmin 클래스는 Bookmark 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지를 정의하는 클래스 