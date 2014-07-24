---
title: "Javascript State Machine"
layout: post
date: "2009-10-14"
categories: [tech]
---

[I wrote a simple Javascript State Machine.](http://github.com/phillc/Javascript-State-Machine)

It is intended for keeping track of what the current state is for my heavy AJAX app at work.

I also learned a lot about OO in javascript without using jQuery or the prototype framework, by using prototypes. I wanted to do that so that it would be framework independent.

Below is a simple example of how I use the state machine, and shows a bit of how I connected it with [Really Simple History](http://code.google.com/p/reallysimplehistory/)


I have included in this example some comments to show my thinking throughout, and perhaps how to use it.

{% highlight javascript %}
Site.prototype = new StateMachine();
Site.prototype.states = {
    Begin: {
        enter: function(){
            // do some animation
        },
        exit: function(){
            // hide some stuff
        }
    },
    Page: {
        enter: function(){
            // show some page
        },
        exit: function(){
            // hide it
        },
        change: function(page){
            // example of some event
            this.pages.change_page(page);
            // events can call events
            this.handleEvent('setURL');
        },
        setURL: function(){
            //example of how I integrate with really simple history
            dhtmlHistory.add(['pages'].concat(this.pages.current_page.split('/')).join('.').toLowerCase());
        }
    }
};

// These are some call backs I used for debugging with firebug to ensure
// that events were firing
Site.prototype.beforeEvent = function(name){
    console.log('begin event: ', name);
}
Site.prototype.afterEvent = function(name){
    console.log('end event: ', name);
}
Site.prototype.beforeStateChange = function(to, from){
    console.log('begin state change to: ', to, ' from: ', from);

    // as an example of intercepting, I can stop a state from changing by returning false
    if(to == 'Page' && this.pages.blocker == 'Page'){
        // some logic
        return false;
    }
    return true;
}
Site.prototype.afterStateChange = function(to, from){
    console.log('end state change to: ', to, ' from: ', from);
}

// The actual defenition. Instance vars can be set in it.
function Site(){
    this.pages = new Page();
}

// global scope, so that it can be accessed globally (as it wouldn't normally
// be because the scope that I actually instantiate it inside prorotype's window onload)
var Davis; 


// Once again, just an example of how I integrate it with Really Simple History
function historyChange(newLocation, historyData) {
    var hash = newLocation.split('.');
    var newState = hash.shift().capitalize();
    if(newState == '') newState = 'Begin';
    if(Davis.changeState(newState))
    {
        if(hash.length > 0) Davis.handleEvent('change', hash.join('/'));
    }
}

// This window observe for onload is prototype specific... But you can achieve the same other ways.
Event.observe(window, 'load', function() {
    Davis = new Site(); // my requirements need me to initialize after load

    // Really Simple History stuff
    dhtmlHistory.initialize(historyChange);
    historyChange(dhtmlHistory.currentLocation || '');
});
{% endhighlight %}

While implementing this, I also learned a bit about bookmarking and enabling the back button of ajax states. Really Simple History has worked ok for me, but it has some quirks... some of which I haven't solved yet (especially in IE) and those bugs may be above.

I also got my first dose of unit testing in javascript... and found some really cool library to assist in the development called [newjs](http://newjs.rubyforge.org/) . However, at the time of this writing, the unit tests are not up to the current code, as a lot has changed... I will deal with that later.

Anyway, while my implementation surely isn't the best in the world, I hope someone can find use from it.

[http://github.com/phillc/Javascript-State-Machine](http://github.com/phillc/Javascript-State-Machine)
