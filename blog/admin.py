from django.contrib import admin
from blog.models import Post, PostCategory

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass


class PostCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
