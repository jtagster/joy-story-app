
from django.contrib import admin

# import your model
from collection.models import Post

# set up automated slug creation

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'gratitudeStmt',)
    prepopulated_fields = {'slug': ('title',)}
# and register it
admin.site.register(Post, PostAdmin)
