---
title: "Javascript Frameworks"
date: 2013-08-15
---

Back in March, the company I work for was creating a small app and were trying to decide which javascript frame work to use. There was an email chain debating which framework to use. I finally responded, and today a coworker convinced me to post that email:

---

Was debating if I wanted to take the bait, but I love to argue, so I couldn't resist.

I am not a fan of pushing the entire rendering process to the client. I am also no longer a fan of client side routing (hash nor push state). It isn't about CPU power, and browser capabilities. I've used the first six frameworks in todomvc.com and a couple of the others, and the way I grade them is by their testability, maintainability, and productivity. Also to say, I am a big fan of modularization, which can be interpreted as numerous small single purpose apps.

My opinions on the big 4 frameworks:

# Backbone

I love backbone. So easy to get started. So easy to do whatever I want. However, I have a hard time believing that it can be scaled to a team size without some hard core discipline, and structure.

Backbone models and collections are freaking awesome, out of all client side frameworks I have dealt with, dealing with data is absolutely the easiest in Backbone. However, it is quickly negated by its shitty controllers/routers/ViewModel layer (if you haven't heard of a ViewModel, I think you should look up the MVVM - model view view/mode pattern). Backbone intentionally leaves this to you. I've browsed a lot of random open source projects on github that use backbone and everywhere I look there is a different way to organize things, and it feels chaotic. If you value the same things about code as I do, that is testability, modularity, readability, etc, you have to come up with your own scheme that hopefully fits all your needs. Backbone's intentional shortcomings are picked up by some frameworks that are built on top of it, like Marionnette... but man I hate frameworks on frameworks.

Finally the view. Not the view you know of from rails, I'll call that the template. The view object. I don't mind how they bind data or events, but ugh, the lack of templating kills me. You have to compile your own template (not a big deal, jquery and underscore provide decent templating functions), and inject that into DOM via some helper methods (Urghhh). So if you have a collection, and render a list, then behind the scenes modify a model/the collection, you have to go delete your own element and replace it in the right spot. I found it manageable until I rendered a form, and tried to modify the same view with some view changes, and it became hell.

# Angular

My first attempts at angular were thwarted by horrific documentation, and my second attempt was painful because they were in progress of updating their horrific documentation to actually document the version they released. Oh and (at the time) an incredibly intimidating dependency injection strategy. They have matured and now the documentation isn't completely rubbish and the dependency injection thing actually makes sense. I am currently using angular for my side project.

Angular is painfully verbose. They provide a dependency injection framework that has you declaring random variables everywhere with eye blistering $ signs (I guess that is because I usually use coffeescript these days). However, I am a big fan of DI, and out of all the frameworks, I believe Angular is the only one that really tries to solve such a problem.

Another awesome thing about angular is it is designed to be able to be tested from the ground up. Even with the angular documentation was shit, I gave angular those attempts because they actually tested their own code with a massive test suite, and showed you how to use it, and it looked half decent. You will be surprised how many projects in the javascript community (well, any open source community really) that become popular don't even have a unit test suite, or a really pointless shitty one (*cough* meteor *cough*). Part of being testable is being modular, and angular skews that axis very high.

Angular provides no model layer... it lets you use any plain old javascript object. A freedom, but given that is was so opinionated every where else (or rather, provided structure every where else), this is a let down.

My last point is the way that angular binds its data. This has been an internal battle for me for quite some time; data and event binding via pseudo html attributes vs declared event observers and interpolation. They are very different styles. I wouldn't necessarily choose a framework because of how they bind events, but there are some tradeoffs that I have seen some highly philosophical and argumentative developers will fight over, but I'm not going to get into that here.

# Ember

Now that ember has successfully separated its image from sprout, I think ember is very solid. Solid models/events, solid and high profile team behind it, solid (IMHO) way to declare templates, sensible view models, not bad collections. The only thing keeping me from constantly using ember js is its tight integration with handlebars (my use case for these frameworks don't align with that kind of templating, I'll explain in a sec).

# Knockout

Last time I tried knockout, it felt like they were cramming ajax down my throat... they seem much better about that now. It has an awkward and sometimes ridiculously verbose ways of doing things. Was built by microsoft, the inventors of MVVM... was built by microsoft so I don't give it a serious look.

# Here are some random thoughts:

I'm done with client side routing for a while, it is annoying to deal with. You have to intercept all links, and redirect it back to your own router. You have to make sure that if you fill out a form, go to another page, come back to the form that the form is emptied. If one page breaks you may have just made the user stuck without any kind of indication that they are used to. You have to basically reinvent http status codes. Github can't even get it right (if you hit the back button too fast while browsing code, you can end up on a page different from what is in your url bar. This happens to me all the time and annoys the crap out of me.) With pushstate you have to make sure every page works if you hit the refresh button.

Rendering html has been solved before, and optimized. Think about all the compression web severs do, think about how browsers do progressive loading. Think about how in our ajax world we had to reinvent so many things (spinners, status codes, etc.)


On my current side project I chose angular. There is only one reason I chose it over the others, and that is because of how it binds data/events. I don't know about you, but I love haml/jade. The way I like to work when I have a scenario where I have dynamic client views is to have the server do as much rendering as possible, and then provide a template for whatever needs to be dynamic. This means using haml/jade on the server, and then feeding that into the templating mechanism of my mvvm framework. The syntax of handlebars is not easily compatible with any whitespace based markup language. With angular I can have the server side compile jade, and leave in the data binding syntax of angular.

like this (jade):

    p(class="{{className}}) foo {{bar}} #{baz}

If baz was a variable set to "qux" on the server, that would compile to

    <p class="{{className}}>foo {{bar}} qux</p>

and then angular would pick those {{ }} up later for templating.


This fits well with my two of my three favorite features in rails; forms and routes.

form_for is such a time saver in my opinion, and I miss rails routes every time I try something that isn't rails. With this scheme in a rails environment, you get to use your form_for or your *_path methods on the server, then let the client do work after. I have gotten this to work before, I don't remember exactly, but I believe you can trick rails into taking odd parameters into url helpers...

if this were my haml:

    %p= post_path("{{post_id}}")

and you had post declared as a resource, you would get

    <p>/posts/{{post_id}}</p>

which can be fed into a templating engine. I think you can do the same with form_for and stuff too.

However, my choices are for my personal side project, where I know where everything is... have to remember that different factors come into play when you are in a team.

K, I'm done rambling... I didn't even get into testability, but whatever.

---

Fast forward to today. We use hamlc + Backbone.js + marionette, and jasmine. Looks like github finally fixed their back button problem. My url_for trick doesn't work with certain characters in certain versions of rails. I learned that angular is very ugly when trying to deal with events over sockets due to the lack of the model. Backbone is painful with relational data (especially many to many).
