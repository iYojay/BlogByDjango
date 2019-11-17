from django.contrib import admin

from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
   list_display = ['title', 'created_time', 'modified_time', 'category', 'author']   ## 后台清单界面出现的内容
   fields = ['title', 'body', 'excerpt', 'category', 'tags']     ## 后台编辑界面出现的内容

   # 添加文章时候，自动补全作者
   def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)