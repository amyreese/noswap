title: Me, PHP and MantisBT
description: I stop using PHP, and step down as developer for MantisBT
date: 2012-06-06
tags: me, mantisbt, php
comments: yes
---
I've been spending time migrating my server from Ubuntu 10.04 to Arch Linux,
and in the process I thought very deeply about every PHP application installed
on the old server.  Five out of the six PHP apps were only there to support the
one that really stood on its own: [MantisBT][], my long-standing bug tracker of
choice.

Now, I've been a core developer, and de facto release manager, for the project
for many years -- since I was still in university and getting paid by my
then-employer to contribute features and plugins that they wanted to use for
their engineering team.  Those plugins, like [Source Integration][], wouldn't be
free without me fighting to license and release them for the community.  And
I wouldn't be where I am today without the experience and help I received in
turn from the very same community.

I know I haven't been as involved in the project these days as I would like to
be; there is an endless list of features and improvements to make to both the
core system and the array of plugins I've created for it.  Some great community
members have stepped up and filled my place at times, while I have at least
tried to stay active on the mailing lists and in the IRC channels.  I've still
guided and cut the last couple releases, but I haven't played a part in shaping
the future of the project.

There are multiple competing visions charting new paths for the aging project,
with conflicting goals and revision histories, and it really needs a stronger
leader to take the reins and guide the project to its next milestones.  I'm
unfortunately not the person to fill this role, for many reasons.  Maybe a few
years ago it would have been better timing.

Lately, I've come to the realization that I can no longer bring myself to work
with PHP for personal projects.  I don't like the syntax, I don't like where
the language is heading, I don't like how much memory and CPU it requires to
run on a web server, and I just spend the whole time wishing I was writing
Python code instead.

This blog hasn't run on PHP or a database for just over a year now, and with my
MantisBT install being used mainly for projects I don't have the time or will
to work on, it just seems to be dead weight.  Github can serve my needs well
enough for the few remaining projects I work on, and without needing a
complicated setup on my end.  Turning off MantisBT means I no longer need
MySQL, PHPMyAdmin, APC, or even mod\_php at all.  The remaining apps can easily
be replaced with external services.

So basically, this is me announcing what I've already been practicing for many
months now: I will no longer be a developer for Mantis Bug Tracker, but I will
remain involved as a mentor for other core developers, or for those seeking
some advice on my plugins or creating their own.  I won't be maintaining any
of my plugins, but I will look at and accept pull requests until someone else
wants to step up as maintainer.  I will be removing MantisBT from my site, but
will keep a database dump in case I ever need to reference it in the future.

This is not me withdrawing from open source; I have many other projects that
I've been working on, most of which are written in Python or C++.  I find them
more enjoyable to deal with, and most importantly, they allow me to break out
of the realm of writing web applications.  IRC, as old as it is, has been my
point of intrigue lately, and is at the core of my current
["pet" project](http://github.com/amyreese/pyranha).

Regardless of language, you can still find me on [Github](https://github.com/amyreese),
where all my toys are available for the public to point and laugh at.  And as
always, I will answer questions on Freenode as "amyreese", or via email, although
there may sometimes be a long delay before I can reply.

Thank you to everyone who's contributed to MantisBT or its plugins, and thank
you to everyone who helped me on the way to where I'm going.

[MantisBT]: http://www.mantisbt.org
[Source Integration]: http://github.com/mantisbt-plugins/source-integration

