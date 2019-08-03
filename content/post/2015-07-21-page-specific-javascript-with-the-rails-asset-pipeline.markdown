---
title: "Page Specific JavaScript With the Rails Asset Pipeline"
date: 2015-07-21
---

I've been using a pattern for loading javascript for specific pages that I would like to share. I have been using it for the past three years across many projects, and has proven to be durable.

It was created in response to three patterns that I saw and disliked.

- Using `javascript_include_tag` to bring in page specific javascript
- Keying javascript off of a html element id `if ($("#some_div")) { ... }`
- Inline javascript

I found all these solutions to be inadequate because they required extra web requests, didn't take advantage of js compression, had javascript overhead of checking the page for contents, didn't allow the use of coffeescript, or left javascript scattered around the project. The Rails Asset Pipeline solves all those problems.

My solution is to use a JavaScript object to wrap pages, which I will call Page Objects.

A Page Object looks like this:

```coffeescript app/assets/javascripts/app/pages/home_page.js.coffee
window.APP.HomePage = class HomePage
  constructor: (options) ->
    @data = options["data"]

  bind: ->
    @bindThing()
    @bindOtherthing()

  bindThing: ->
    otherSomething(@data)

  bindOtherthing: ->
    otherSomething()
```

Every Page Object is applied to window.APP, has a `bind` method which will run any page specific code, and lives in app/assets/javascripts/app/pages. You will see why in a moment. The constructor is optional.

We bring this into our asset pipeline like so:

```coffeescript app/assets/javascripts/application.js
//= require ./app/init
//= require_tree ./app/objects
//= require_tree ./app/pages
```

Our pages are assigned to `window.APP`, which needs to be initialized before the page objects are loaded. Because requiring javascript files must happen at the top of your file, before any executable javascript is written, we must move the initialization of `window.APP` to another file.

```coffeescript app/assets/javascripts/app/init.js
window.APP = {}
```

Now, we want to have rails instantiate one of these objects, and call our `bind` method for us.

```ruby app/helpers/application_helper.rb
module ApplicationHelper
  def load_javascript_class(javascript_class, options = nil)
    content_for :page_javascript do
      javascript_tag "$(function(){ (new window.APP.#{javascript_class}(#{options.to_json})).bind(); })"
    end
  end
end
```

```haml app/views/layouts/application.html.haml
!!!5
%html{lang: "en"}
  %body
    = render 'layouts/header'
    = yield
    = render 'layouts/footer'
    = yield :page_javascript
```

The last part of it is to call it from your view

```haml app/views/home/index.html.haml
- load_javascript_class "HomePage", data: ["foo", "bar"]

.container
  .row
    %h3 List:
```

With this pattern, you can have page specific javascript while utilizing the asset pipeline of rails. This solution also solves the problem of how to get data from rails to your javascript. You can see in the helper that if you pass in a second argument to `load_javascript_class` that it will take it, and turn it into json for your page object's constructor.

You may have noticed that I also have a app/objects required in the application.js. I do this to create objects that may be shared between pages. I tend to use a similar pattern as page objects, and instantiate/delegate to them from a page object.

Some sites need to have two sets of javascript, perhaps for very different sections of the site, like an admin area. You can change the helper to be

```ruby app/helpers/application_helper.rb
def load_javascript_class(namespace, javascript_class, options = nil)
  content_for :page_javascript do
    javascript_tag "$(function(){ (new window.#{namespace.to_s.upcase}.#{javascript_class}(#{options.to_json})).bind(); })"
  end
end
```

The first parameter is now where on `window` to look for your objects. Perhaps you add a line in init.js for `window.ADMIN = {}` and then load objects from there with `load_javascript_class :admin, "SomePage"`. This pattern should be flexible from there.

This pattern has solved most my issues for the past few years. I am sure there is a different pattern to use for projects with turbolinks, but I will continue to bring this pattern into all other projects because of the utility it provides.
