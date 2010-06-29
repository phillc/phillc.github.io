---
kind: article
created_at: 2008-07-07
title: "Structure inside a project"
---
A common problem I have had is that too much work was required when I needed to deploy my django project, or if i needed to work on the project on another computer. Subversion has been my friend, but part of the problem is the necessary local settings in each of the projects.

In addition to the overall structure between all my projects, I have developed a few tricks to make handling things inside of a project much easier.

Previously, my template folder and my media folder were in different parent directories. This caused me to need to change several variables in the settings.py (or my [settings_local.py](http://kapsh.com/blog/2008/jul/05/making-django-version-control-friendly/)) of django in each environment that it existed in. However I no longer have to do that.

Inside my settings.py I have this:

    #!python
    import os, sys
    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps')) 

The first two lines figure out the directory that the settings.py lives in
The third line inserts my apps folder to the python path (this works great with my [django directory structure](http://kapsh.com/blog/2008/jul/01/developed-directory-structure/))

Now, the next step for me was to move my template and media directories around. My directory structure for a project is as follows:

-project  
--media   
---css    
---js     
---images  
--templates  
---application template directory 1  
---application template directory 2  
---base.html                         
--apps                               
---app1                              
---app2                              
--settings.py                        
--settings_local.py

So as you can see, my templates folder is in the same directory as my settings.py. My media folder is too. In order to avoid making this a variable too:

    #!python
    MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

    TEMPLATE_DIRS = (
         os.path.join(PROJECT_ROOT, 'templates'),
    )