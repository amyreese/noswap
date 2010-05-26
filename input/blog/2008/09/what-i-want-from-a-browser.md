title: What I Want From a Browser
tags: browsers, chrome, firefox, opera
date: 2008-09-23
---
With all the recent talk of Google Chrome and all the other browser options, I find more and more that the love-to-hate Firefox 3.0 is still my best friend, and will not be replaced anytime soon.  However, the major annoyance I've noticed through all the options is that there is always some feature or set of features lacking from every single option, including Firefox, that can be found in the competition.

So for the public record, I'd like to list the set of features that I feel are most important to have in a browser, and how the array of competitors each handle themselves.  Just want to see <a href="#browser-summary">the results</a>?

<ul>
	<li><strong>Bookmark Tagging</strong>: Saving bookmarks into endless hierarchies of folders is extremely tedious and inefficient; the ability to instead tag bookmarks with multiple words allows users much better context for later search and retrieval.  Using a third-party bookmark tagging site shouldn't be necessary anymore;  tagging bookmarks gives such a high return on investment of time and effort that it should be a no-brainer to implement this in any and all browsers.

Mozilla was the first out of the gate with Firefox 3.0's introduction of bookmark tagging, and as an avid user of the feature, coupled with the "Unsorted Bookmarks" option, it is extremely well implemented and dead simple to use.  Click the star in the location bar to mark the page, and click again to add tags, rename the bookmark, or file it into a real location; type the tag name into the location bar (Awesome Bar!), and look through the results for what you want.  As far as I know, none of the other major browsers have added, or plan to add, this functionality; ouch!  Google Chrome gets negative points for not even letting you browse or use your bookmarks: you can only search them.</li>

	<li><strong>Content Synchronization</strong>:  With more and more users connecting to the internet from multiple locations on a regular basis, the task of synchronizing user content is becoming ever more important.  Most importantly, bookmarks must be kept in sync, but things such as saved passwords, cookies, browsing history, and form fields are also up for grabs, and it all must be done securely.  Bookmarking websites have it so easy, but some browsers are really stepping it up lately.

Initially, Firefox was the only one with such a feature, in the form of much-loved Foxmarks plugin, which automatically syncs bookmarks to a remote server, and offers a page to use the bookmarks even from a browser without the plugin.  These days, Foxmarks has been much improved, and works with the bookmark tagging from Firefox 3.0, and now Mozilla has thrown their hat in the ring with the rather ambitious plugin project titled <a href="http://services.mozilla.org">Mozilla Weave</a>, which promises to sync just about everything you can imagine, but is still in beta development.  Opera also rounds out the list with their <a href="http://www.myopera.com">My Opera</a> service, which is rather similar to Foxmarks, except that it's built directly into the core browsing experience; very nice touch.</li>

	<li><strong>Platform Integration</strong>: When I open my browser, it should look like it belongs on my desktop; it should share the same widgets, icons, color schemes, and fonts that I have configured for my environment.

Firefox is really good at this on Mac and Windows, but while the Linux integration still looks really good, it's not perfect, and can stutter on some fancy Gtk+ themes.  Safari, Konqueror, and Epiphany fit perfectly, but only in their target desktops; Konqueror looks out of place on a Gnome desktop, and Opera looks horrid on Linux and doesn't really look right on with Windows either.  Chrome doesn't even try to fit in anywhere (why?).</li>

	<li><strong>Process Separation</strong>: When I have multiple windows or tabs open at the same time, JavaScript executing on one page should have no effect on operation of the browser interface, let alone on other web pages open in the browser.  It shouldn't take one poorly-written AJAX site to prevent the user from using the browser, or from working in another tab.

So far, Chrome is the first and only browser, as far as I know, to implement this correctly.  The way that Google has managed to use a separate process for every single tab, complete with a "task manager" to control errant pages, is phenomenally well put together.  Opera comes in a distant second place, with better performance overall when compared to Firefox and friends, which will often block the user from interacting with any portion of the interface while executing JavaScript.</li>

	<li><strong>Standards Compliance</strong>: When I visit a page that complies with the various HTML, XML, and CSS specifications, it should be rendered the same as on any other browser.  As much as we all know that this will never be true, the harder we try for it, the better we make life for web developers, including me.

This is basically a problem for all browsers, but more of a problem for some than others.  We know all this already...</li>

	<li><strong>Advertisement Blocking</strong>: At a time when online advertising is the lifeblood of the internet (and spam e-mails), the ability to have your browser automagically hide ads from web pages is extremely user-friendly.  It doesn't even need to be installed or turned on by default, but there must be <em>some way</em> to accomplish this task.

Firefox takes the cake here, with an absurdly wonderful and easy to use plugin, <a href="http://adblockplus.org">Adblock Plus</a>, which will automatically update itself with the latest list of ad sites on the internet, and allows the user to customize the list or add their own rules for blocking content.  Sadly, this is only available for Mozilla products.

However, ever time I mention this topic as a benefit for Firefox, I always get adamant Opera users claiming the wonders of Opera's built-in content blocking options, but I just don't see it as coming anywhere close to Adblock Plus;  it requires the user to manually download and edit a file in their Opera profile containing the list of blocked content, and there's no method for automatically updating the list, and if the user wants to block something else, they have to edit that file by hand with no guidance.  This strikes me as an extremely unfriendly process, and is only a partial replacement for Adblock Plus.  Do note however, that a similar system of ad blocking is also available for Konqueror, but no such option is given to Chrome or Safari.</li>

</ul>

<a name="browser-summary"></a>
<h3>Summary to Make That List A Waste of Time</h3>
So here's how I see today's options of browsers, with their best and worst parts:
<ul>
	<li><strong>Mozilla Firefox</strong>: Extremely flexible and powerful with plugins, but a poor performer with many tabs.</li>
	<li><strong>Opera</strong>: Fast and nifty, includes the kitchen sink, poor platform integration, no bookmark tagging.</li>
	<li><strong>Konqueror</strong>: Platform integration done right, extensive protocol support, lacks content-oriented features.</li>
	<li><strong>Google Chrome</strong>: Extremely fast and robust with true process separation, lacks almost every standard browser feature.</li>
	<li><strong>Safari and Epiphany</strong>: Lightweight platform integration, lacking any advanced features.</li>
</ul>

I'm actually not very happy with any of the browser options available; they all have disadvantages when compared to other browsers, and there is no clear leader, especially when you consider that every user has a different set of requirements.

However, Firefox still makes me cry the least while I'm using it, and, with its myriad of plugins, makes my time surfing the web so much more enjoyable, except for when JavaScript makes it sop responding of course.  Probably the best thing Mozilla could do to improve Firefox would be to implement process separation akin to Google Chrome, or at least prevent the UI from becoming unresponsive during heavy JavaScript execution.  If that would happen, I would be absolutely elated.

So the real questions now are:  Where does this leave us?  How far are we towards a better web?  Which browser will get us there the fastest?  What will eventually make all this goofy garbage obsolete?  When will I shut up and let you leave this page?
