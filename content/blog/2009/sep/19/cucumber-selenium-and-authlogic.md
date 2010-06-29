---
kind: article
created_at: 2009-09-19
title: "Cucumber with Selenium and Authlogic"
---
I had some Issues with cucumber/selenium working properly with authlogic. After much searching, I've figured out how to get it all to work properly.

I would get an error like:

    When I follow "Manage pages"                          # features/step_definitions/webrat_steps.rb:19
      ed out after 5000ms (Selenium::CommandError)
      /opt/local/lib/ruby/1.8/timeout.rb:62:in `timeout'
      /opt/local/lib/ruby/1.8/timeout.rb:93:in `timeout'
      (eval):2:in `/^I follow "([^\"]*)"$/'
      features/plain/admin_page.feature:8:in `When I follow "Manage pages"'

      Initially, to setup authlogic to work with regular webrat tests, I had to put the following in my env.rb:

          #!ruby
          require "authlogic/test_case"

          Before do
            activate_authlogic
          end

      After getting it working with webrat, I decided I wanted to test some of my javascript and AJAX with selenium, so I followed [this guide](http://wiki.github.com/aslakhellesoy/cucumber/setting-up-selenium)

      The database_cleaner gem had to be added because you can't use

          #!ruby
           Cucumber::Rails.use_transactional_fixtures

      with selenium, so it had to be removed from the env.rb and placed in the plain.rb. As a result, this ended up in my enhanced.rb

          #!ruby
          require 'database_cleaner'
          Before do
            # truncate your tables here, since you can't use transactional fixtures*
            DatabaseCleaner.strategy = :truncation
            DatabaseCleaner.clean
          end

      and this ended up in my plain.rb

          #!ruby
          require 'database_cleaner'
          DatabaseCleaner.strategy = :truncation
          DatabaseCleaner.clean

      Originally, I had it just in my enhanced.rb as an After block instead of Before, but after further contemplation, I realized that if something goes terribly wrong with the selenium tests, then the database would have bad data in it... So might as well clean it before hand.

      Finally, my problem with authlogic + seleniu, was how I wrote my test. The way it was erroring out made it look like something completely different (the selenium timeout error), but after I watched it a couple times closely, I determined that the test was being sent to the next page before the "button press" was executed.

      Here is the beginning of my test that failed:

          #!ruby
          Scenario: Visit Add Page page
            Given I am logged in
            And I am on "the admin page"
            When I follow "Manage pages"
            And I follow "New Page"

      With a little help from [a post on stack overflow](http://stackoverflow.com/questions/966052/cucumber-selenium-fails-randomly/966998#966998), I got it to work with the following:

          #!ruby
          def user
            @user ||= Factory.create(:user)
          end

          def login
            user
            fill_in "Email", :with => @user.email 
            fill_in "Password", :with => @user.password
            click_button "Login"

            # This is what was added
            if Webrat.configuration.mode == :selenium
              selenium.wait_for_page_to_load
            end
          end

          Given /^I am logged out$/ do
            @current_user_session.destroy if @current_user_session
          end

          Given /^I am logged in$/ do
            visit path_to("the login page")
            login
          end

          When /^I login$/ do
            login
          end

      Notice I had to add the if selenium line in order to get it to work in webrat.

      Something tells me there is a better way to do it... probably overriding the click_button method when selenium is loaded... but I don't know it well enough quite yet to venture that far, I'll probably try it soon though.


      Edit: oh, its a thing with webrat... but installing the newest version didn't fix it for me, then I actually read the [ticket...](https://webrat.lighthouseapp.com/projects/10503/tickets/226-not-waiting-for-page-load-with-selenium) I'll stick with my current solution for now.

      Edit2: Actually the issue is in the visit method, if you can believe that. click_button works fine, as it waits for the page to load before clicking, but the visit method is sent so fast, that because of the way my test is set up, we are sent to the next page either before the login button is pressed, or before the request gets a chance to process... I don't feel like investigating which one it exactly is, because the solution is the same... wait for the next page to load.
