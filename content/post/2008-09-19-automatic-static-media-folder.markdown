---
title: "Automatic Static Media Folder"
date: 2008-09-19
---

Added another shortcut...
I had a config variable in my settings_local file to specify where the media folder was in order to have django static serve it.

This is much easier.
<!--more-->>

urls.py:

{{< highlight python >}}
if DEBUG:
    import os
    media_root = os.path.join(PROJECT_ROOT, 'media')
    urlpatterns += patterns ('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_root}),
    )
{{< / highlight >}}
