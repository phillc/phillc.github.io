---
kind: article
created_at: 2009-08-18
title: "e-Text Editor"
---
Was attempting to compile e-text editor on ubuntu 9.10 (yea yea, I know... my right to complain about broken packages disappears since its alpha) just to try it out, but had a sick number of errors ranging from "Cannot compile wxWidgets" to "Cannot compile WebKit".

Finally, after trying multiple ways of compiling wxWidgets, I figured out the real error was

    "./include/wx/gsocket.h:40: error: using typedef-name ‘GSocket’ after ‘class’"
    
    
So I applied a patch I found at [http://trac.wxwidgets.org/ticket/10883](http://trac.wxwidgets.org/ticket/10883) to the wxwidgets folder. and it suddenly worked.

edit: I turned out that I also had to update glib. glib version 2.20 did it for me.