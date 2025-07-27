---
title: "Developed Directory Structure"
date: 2008-07-07
---

Over the course of my web development life, I have changed my work flow and directory structure many times. Each time gets a little bit better, but I doubt I will ever finish modifying it, as I am always learning new techniques.

I am presently using [Django](http://www.djangoproject.com) in all of my projects, both at work and as a hobby. Django's ability to easily reuse applications has mad me change my directory structure several time. Finally, I do believe I have settled.

First thing to know, is that both at work and in my pet projects, I am hosting multiple websites on the same apache instance. This is simply because the load behind the website does not justify buying a new slice (I use [slicehost](http://www.slicehost.com) for my hosting needs).

I also make use of several available applications out there, [django comment utils](http://code.google.com/p/django-comment-utils/), [django tagging](http://code.google.com/p/django-tagging/), and [django-registration](http://code.google.com/p/django-registration/) just to name a few (all/most are findable through [django pluggables](http://djangoplugables.com/))

So that being said, I need to have a directory structure capable of handling each one of my projects, all of my own shared applications, and all of the downloaded applications.

Here is what I have come up with.

- projects/  
-- project 1/  
--- apps/      
---- non reusable app 1/  
---- non reusable app 2/  
-- project 2/             
-- project 3/             
---apps                   
---- non reusable app 3/  

- common/  
-- self made reusable app 1/  
-- self made reusable app 2/  

- external/  
-- grabbed reusable app 1/  
-- grabbed reusable app 2/  
-- grabbed reusable app 3/  

Basically, the idea being that I store my projects in the projects folder, with applications made just for that project in the project's application folder.

I put applications that I build that will be used by more than one project into the common folder.

Applications that I have grabbed from other people (comment_utils, tagging, etc) into the external folder.

Then for each virtual host, I add to the python path the projects folder, then reference settings by projectname.settings (from observation, django adds the folder where the settings file is to the python path itsself), and the common folder and the external folder. I also add the projects, external, and common folders to the python path inside of conf file.

That works for apache, but then to get manage.py to work (it doesn't work because none of the python paths are set for it), I edit "/etc/environment" and add the line

{{< highlight bash >}}
PYTHONPATH="/home/username/projects:/home/username/common:/home/username/external"
{{< / highlight >}}

Bingo, now manage.py works.

Now, any time I want to add a new project, I do not have a ton of hassle trying to get the project's manage.py to work, and all my virtual hosts in apache have the same structure!
