---
title: "asdfasdfas!"
---
Subversion has been my friend ever since I learned about it. However, it took me a while to figure out how to deal with configuration files. For Django, this specifically relates to the settings.py.

Django projects can end up on many different environments. Putting settings.py into source control directly will cause our settings to migrate across all working copies. This is not reasonable, as not every person will have the same environment (not all using mysql, not all using the same directory).

Removing settings.py from version control, and make a seperate settings.py.template file that contains just the basic structure is a solution to that. However, it brings another problem: What if you want to change a used application or a middleware? You would then have to make that change on all working copies.

My solution has been to make a settings_local.py.dist

This file has variables in it like media path, database information, and caching options. You can copy these things straight out of the settings.py (and delete them from settings.py)

This file will go under version control.

Now, in your settings.py, add the line

    #!python
    from settings_local import *

(I added the line to the very bottom of my settings.py)

So, now when a working copy of the project is grabbed, the person behind it can copy settings_local.py.dist to settings_local.py. Inside settings_local.py the environment's details are placed. This file will be ignored from version control.

With this setup, you can add an application or middle ware to settings.py for easy distributing through version control, and it will not affect a workspace's local variables.

