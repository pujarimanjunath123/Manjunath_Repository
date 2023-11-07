from django.contrib import admin
from blogapp.models import Post
from blogapp.models import Comment

class PostAdmin(admin.ModelAdmin):
	list_display=['title','slug','author','body','publish','created','updated','status']
	list_filter=('status','author')
	search_fields=('title','body','author')
	raw_id_fields=('author',)
	prepopulated_fields={'slug':('title',)}
	ordering=['status','publish']


class CommentAdmin(admin.ModelAdmin):
	list_display=('name','email','body','created','updated','active')
	list_filter=('active','created','updated')
	list_search=('name','email','body')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
