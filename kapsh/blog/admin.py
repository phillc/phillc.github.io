from django.contrib import admin
from kapsh.blog.models import Entry

class EntryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identity', {
            'fields': ('title', 'slug',),
            'classes': ('adminMain',)
        }),
        ('Organizational', {
            'fields': ('author', 'categories',),
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
            'fields': ('shown_date', 'publish_on', 'publish_end', 'is_published',),
            'classes': ('adminSide',)
        }),
    )

    list_display = ('title', 'shown_date', 'is_published', 'author',)
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

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.save()

admin.site.register(Entry, EntryAdmin)
