    class Admin:
        list_display = ('title', 'status', 'publish',)
        list_filter   = ('publish', 'section', 'status', 'author',)
        ordering = ('-publish',)
        search_fields = ('title', 'body',)