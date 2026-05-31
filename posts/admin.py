from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from bloggers.models import Blogger
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blogger', 'comments_count', 'likes_count', 'post_date', 'is_published')
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    list_filter = ['blogger']
    search_fields = ['title', 'text', 'blogger__name']
    list_per_page = 20

    readonly_fields = ['comments_count', 'likes_count', 'blogger']

    #برای اینکه خودش بلاگر را ست کند در سایت متد زیر را استفاده میکنیم
    def save_model(self, request, obj, form, change) -> None:
        obj.blogger = Blogger.objects.filter(user = request.user).first()
        return super().save_model(request, obj, form, change)
    
    # هر ادمینی که وارد میشود با متد زیر فقط پست های خودش برای آن نمایش داده میشود
    def get_queryset(self, request):
        qs= super(PostAdmin , self).get_queryset(request)

        if request.user.is_superuser:
            return qs
        
        return qs.filter(blogger__user = request.user)

admin.site.register(Post , PostAdmin)
