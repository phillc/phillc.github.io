---
title: "Single Page App Refresh Strategy"
date: 2019-09-04
---

In 2015 the company I was working for wanted us to do an overhaul of the
existing UI to give a better user experience. We took it as an opportunity to
explore the landscape of JavaScript frameworks, something I've done many times.
We knew the app would be behind a login, so server side rendering was not
important for SEO, freeing up the search space to nearly anything.

We quickly became enamored by ClojureScript, as we already had been considering
Clojure for a backend rewrite. Around the time, it also felt as though
ClojureScript was picking up steam by piggybacking the popularity surge of
Clojure. I was slightly hesitant because it didn't appear to have support for
inline HTML like vanilla JavaScript with JSX, or even some CoffeeScript extensions.

However, what really impressed us was [this demo of flappy bird written in
ClojureScript](
https://rigsomelight.com/2014/05/01/interactive-programming-flappy-bird-clojrescript.html
). It demonstrated [Figwheel]( https://figwheel.org/ ) for live code reload, use
of an atom to maintain state past live refreshes, and connecting directly to the
REPL via Emacs. The HTML syntax didn't look as bad as I thought it would,
either.

At the time, there were a few examples of applications written in ClojureScript.
The one that sticks out the most in memory is the Circle CI frontend. Not only
was this a complete production proven stack that demonstrated great UX, they
also [wrote many articles about their tech stack](
https://circleci.com/blog/why-we-use-om-and-why-were-excited-for-om-next/ ), and
[spoke at conferences about it]( https://www.youtube.com/watch?v=LNtQPSUi1iQ ).
Their source [code being openly visible]( https://github.com/circleci/frontend )
made it much easier to figure out how to architect a ClojureScript app, and I
say we drew much of our inspiration from them. We ended up choosing Om as our ClojureScript framework because of
this.

In many ways, we ended up with what communities now call a [JAMstack](
https://jamstack.org/). Here is a quick over view of our architecture, before I
get into the refresh strategy. If you have any questions about any specific
bullet point, please reach out.

- Rails backend providing an API using [Transit](
  https://github.com/cognitect/transit-format ) as our format for AJAX requests.
- Passed the Rails CSRF token to the SPA to use in AJAX requests.
- We utilized the authentication and authorization that already existed in our
  on our server side Rails app to wrap our API as well. Logging in via [Devise](
  https://github.com/plataformatec/devise ) allowed our AJAX calls in the same
  session to be authenticated.
- Because we piggybacked authentication, we needed to have the starting point
  of the app served by Rails. We used a wild card route to capture routes of the
  entire namespace of the app to launch the single page app, like so:

{{< codeblock "routes.rb" "ruby" >}}
get '/app/',      to: "spa#page", format: false
get '/app/*page', to: "spa#page", format: false, as: :spa_page
{{< /codeblock >}}

- Routes in the SPA were handled by [Secretary](
  https://github.com/clj-commons/secretary ). We used [Pushy](
  https://github.com/kibu-australia/pushy ), which was a wrapper around
  [Closure's Html5History](
  https://google.github.io/closure-library/api/goog.history.Html5History.html ),
  to intercept all clicks on anchors in the app.
- The ClojureScript app was built using a Gulpfile. The Gulpfile was responsible for
  pulling together dependencies (css, fonts, resize our logo to smaller formats,
  etc.), wrapping the [Leiningen]( https://leiningen.org/ ) commands to build
  the ClojureScript app, minifying the output (even though ClojureScript goes through the google
  closure compiler, minification did have an effect), uploading everything (the
  artifact we called it) into a folder in S3, and pushing new version
  information to heroku.

{{< tabbed-codeblock "gulpfile.js" >}}
<!-- tab javascript -->
gulp.task('publish', ['build-artifact'], function() {
  var headers = {
      'Cache-Control': 'max-age=315360000, no-transform, public'
  };

  var publisher = $.awspublish.create(s3Params());

  var deploySlug = moment.utc().format("YYYYMMDD-HHmmss");
  $.util.log("Publishing", deploySlug);

  gulp.src([destination.minifiedApp,
              destination.dependencies,
              destination.css,
              'resources/public/fonts/**/*',
              'resources/public/images/**/*'],
          { base: 'resources/public/' })
      .pipe($.rename(function(path){
        path.dirname = "spa/" + deploySlug + "/" + path.dirname;
      }))
      .pipe(publisher.publish(headers))
      .pipe($.awspublish.reporter());
  });
<!-- endtab -->
<!-- tab javascript -->
childProcess.spawn('heroku', ['config:set',
                              SPA_ASSETS_SLUG=' + slug,
                              '--app=' + app]);
<!-- endtab -->
{{< /tabbed-codeblock >}}

- The folder name used in S3 was very important, as it was the version name of
  our artifact. We used a combination of date, time, and some other signifiers,
  but it could easily have been just a uuid.
- This version name would then be inserted as an environment variable in the
  Rails app. The Rails app would then use the version name to point to the
  correct artifact.

{{< codeblock "spa.html.erb" "html" >}}
<link href="<%= root_path %>/css/style.css" rel="stylesheet" type="text/css">
<!-- the script tag would be near closing of body tag  -->
<script src="<%= root_path %>/js/spa.min.js"
        type="text/javascript"
        crossorigin="anonymous">
</script>
<script type="text/javascript">window.spa.core.launch_BANG_()</script>
{{< /codeblock >}}
{{< codeblock "spa_controller.rb" "ruby" >}}
def root_path
  "https://our.s3.bucket.url/bucket_name/{ENV['SPA_ASSETS_SLUG']}"
end
{{< /codeblock >}}

- By changing the environment variable, we have effectively deployed a new
  version. We did this with a simple `heroku config:set SPA_ASSETS_SLUG=123`
  assisted by our Gulpfile. This is also a cache buster, as we don't have to
  worry about cache expiration time. If the end user loads the page, we know
  they will end up with the version of our assets at that time.
- We used the same bucket for our pre-production and our production
  environments, allowing us to use the same artifact we test on to be the one
  that the end users receive.
- We did some magic in the HTML to point to a version with Figwheel enabled in
  development. In our automated tests, we used a symlink in our tmp folder to
  point to a compiled version in the SPA app, then mounted a rack app in our
  test environment that serves the JavaScript. This allowed us to test the
  entire stack using RSpec, Capybara, and Poltergeist.

{{< codeblock "config/environments/test.rb" "ruby" >}}
config
  .middleware
  .use Rack::Static,
        :urls => ['/test_spa'],
        :root => "tmp"
{{< /codeblock >}}

Now that the context is laid out, it is time to see how we refreshed a page
after a new deploy in a way that covers most use cases.

All summed up in one quick sentence:

> When we make an ajax request, the api returns the current version name and if
it does not match the version the SPA was loaded with, we treat events on
anchors like a normal link.

By normal, I mean you can either remove your event handlers from all anchors
(the ones in place that prevent a normal link follow, and instead route the
event to your router to handle), or find a way to have code in between the on click
handler of your anchors and instead force the browser to navigate to a new page.

{{< tabbed-codeblock "history.cljs"  >}}
    <!-- tab clojurescript -->
        (set! (.. js/window -location -href) path))
    <!-- endtab -->
    <!-- tab javascript -->
        window.location.href = "{value.of.href}"`
    <!-- endtab -->
{{< /tabbed-codeblock >}}


This effectively makes all GET requests in the SPA force
reload the page.

The environment variable we used to determine the root path in the code above
(SPA_ASSETS_SLUG) is passed to the SPA when it is loaded. The SPA then checks
every request to the API for this version, and if they mismatch, we use the
above strategy.

Our code in Om is quite uninteresting. It was a listener that looked similar to the
ones in [Circle CI's front end's main go loop](
https://github.com/circleci/frontend/blob/c189f3546afe49b64c8ee86d92ff67ed9d2eda78/src-cljs/frontend/core.cljs#L333
), except it was responsible for checking the AJAX responses for version numbers
to compare against the state.

{{< codeblock "core.cljs" "clojurescript" >}}
(defn history-handler [value history-imp app-state-atom]
  (clog "History:" value)
  (let [message (first value)
          args (second value)
          version-mismatch? (get-in @app-state-atom state/version-mismatch?-path)]
      (with-airbrake-logging {:component "history" :action message}
      (if version-mismatch?
          (do
          (clog "Version mismatch. Forcing.")
          (swap! app-state-atom assoc :navigation-point :loading)
          (history/history-event :force args history-imp))
          (history/history-event message args history-imp)))))

...

(go (while true
      (alt!
      ...
      (:history comms) ([v] (history-handler v history-imp app-state))))
{{< /codeblock >}}

Every endpoint in our Ruby API used the same method to render a Transit
response, so it was easy to tack on the current version to every request.

{{< codeblock "base_controller.rb" "ruby" >}}
def render_transit(payload={})
  transit_payload = payload.merge(timestamp: Time.now.to_i,
                                  version: ENV['SPA_ASSETS_SLUG'])

  respond_to do |format|
    format.transit do
      render transit: transit_payload,
              handlers: { Hash => HashWriteHandler.new,
                          ActionController::Parameters => HashWriteHandler.new }
    end
  end
end
{{< /codeblock >}}

This same strategy could be used in

- JQuery by removing event handlers.
- Vue Router with a Guard or by setting catch all route at higher precedence.
- React Router by setting a higher precedence catch all route or somehow
  removing the router components.

This strategy is not perfect. You can still have UI errors due to a mismatch
between a parameter on the client and server side (for example if they haven't
followed any links in a while). It will not work for an SPA that doesn't use
normal links to navigate between components, like Trello. But it would work for
something like a mail client or a social media website. For us it was a tradeoff
between how much effort we were going to put into a strategy to mitigate our UI being
out of sync with our server, and frequency where this type of error could happen.

This strategy can be used in conjunction with other strategies. Perhaps you have
a web socket open to notify your clients browsers that a new version is
available, and have issues with some users' sockets dying and not getting the
update, this can help reduce the quantity of those left behind. Perhaps your
fool proof strategy of waiting a few days for caches to clear and users to
finish with the old version before yanking the old code was still hitting your
exception notifier with UI versions that are weeks old. Either way, this is a
pretty low effort way of handling it.

Thank you to Circle CI for all the content they put out about their app. Thanks
to [Mark Billie]( https://github.com/yaaase ) for proof reading this and helping
me compile a list of interesting points. Thanks to [Brian King](
https://github.com/entrobe ) for working on this project with me and taking off
quickly with this architecture. Also thanks to [Steve Salkin](
https://github.com/sls ) for giving us the support to explore outside of our
comfort zones.

