---
title: "Ruby multi-dimensional array helper"
layout: post
date: "2009-08-28"
categories: [tech]
---

I needed something to help me get through a multi-dimensional array. So I extended the Array class.

Grab expects an array of coordinates.

{% highlight ruby %}
class Array
  def grab(position)
    value = self.fetch(position.first)
    value = value.grab(position[1..-1]) unless position[1..-1].empty?
    value
  rescue NoMethodError
    raise(IndexError, "Multi Dimensional Array not deep enough")
  end
end
{% endhighlight %}

Then I can do this:

{% highlight ruby %}
>> [[1,2,3],"asdf",[[11,22,33],5,6,7]].grab([2,0,0])
=> 11
>> [[1,2,3],"asdf",[[11,22,33],5,6,7]].grab([2,0,2])
=> 33
>> [[1,2,3],"asdf",[[11,22,33],5,6,7]].grab([2,1])
=> 5
>> [[1,2,3],"asdf",[[11,22,33],5,6,7]].grab([1,0])
IndexError: Not an array.
	from /Users/phillip/Desktop/rworkspace/davisbrandcapital/lib/tagging.rb:73:in `grab'
	from (irb):64
>> [[1,2,3],"asdf",[[11,22,33],5,6,7]].grab([1])
=> "asdf"
>> 
{% endhighlight %}
