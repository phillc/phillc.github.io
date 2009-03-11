from django.contrib import admin
from unboundedition.blog.models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identity', {
            'fields': ('title', 'slug',),
            'classes': ('adminMain',)
        }),
        ('Organizational', {
            'fields': ('author', 'author_alias',),
            'classes': ('adminMain',)
        }),
        ('Content', {
            'fields': ('intro_text_raw', 'full_text_raw',),
            'classes': ('adminMain',)
        }),
        ('Tags', {
            'fields': ('tags',),
            'classes': ('adminMain',)
        }),
        ('Advanced options', {
            'fields': ('date', 'publish_on', 'publish_end', 'is_published',),
            'classes': ('adminSide',)
        }),
    )

    list_display = ('title', 'date', 'live', 'author',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_filter = ('is_published',)

    class Media:
        css = {
            "all": (
                "css/admin.css",
            )
        }
        js = (
            "admin/tinymce_2/jscripts/tiny_mce/tiny_mce.js",
            "js/admin/blog_admin.js",
            "filebrowser/js/AddFileBrowser.js",
        )