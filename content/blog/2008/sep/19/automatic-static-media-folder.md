---
kind: article
created_at: 2008-09-19
title: "Automatic static media folder"
---
Added another shortcut...
I had a config variable in my settings_local file to specify where the media folder was in order to have django static serve it.

This is much easier.

urls.py:

    #!python
    if DEBUG:
        import os
        media_root = os.path.join(PROJECT_ROOT, 'media')
        urlpatterns += patterns ('',
            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_root}),
        )