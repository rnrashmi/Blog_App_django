from django.contrib import admin
from BlogApp.models import Post,Comment



class PostAdmin(admin.ModelAdmin):

    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','created','publish')
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','body')
    raw_id_fields=('author',)

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','active','updated')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
