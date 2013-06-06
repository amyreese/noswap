title: Push Push Push
description: I share some of the growth statistics for ZNC Push and Pushover
date: 2013-06-06
tags: me, znc, thanks, stats
---
One of my favorite projects that I've created has to be [ZNC Push][], a plugin
for [ZNC][] that generates push notifications for IRC highlights and private
messages.  It supports a wide array of push services for all of the major mobile
platforms, and gives the user deep flexibility in choosing how and when to
trigger these notifications.

However, I have very little insight into usage statistics for the plugin.
[Pushover][] is the only service that gives me gross usage data, but
considering ZNC Push supports six other networks as well as custom push URLs,
this only represents an unknown portion of the total usage.  But I will
continue to draw baseless conclusions from it regardless!  *Do note that I
can't see anything more than raw volume of notifications; I do not have access
to who is sending/receiving these, nor the contents of those messages.*

So without further ado, some pretty graphs straight from the Pushover dashboard:

[<img src="/media/push-push-push.png" width="546"/>](/media/push-push-push.png)

**ZNC Push reached a milestone of sending *15,000* push notifications in May
through the Pushover service!**

Push volume has been growing steadily since Pushover support was added, with a
small dip in December and January that is likely attributeable to the holidays
for most users.  May marked the second occasion that ZNC Push has exceeded
the volume "cap", and Pushover has again graciously increased that in support
of this open source project.  At this sort of grawth rate, I would expect the
next volume cap (25,000/mo) will be reached by October at the latest.  I'm
excited to see such growth for a small side project with such a niche use case.

Sometimes, it's amazing to stop and realize just how far this project has come.
What started in January of 2011 as a basic module for the Notifo push service,
has blossomed into a mature system supporting multiple push services and far
more customization options than I had ever envisioned from the beginning.
Knowing that it's being used by so many people, and helping them stay more
connected with their online communities, makes me a very happy engineer.

Many thanks to [Pushover][] for granting such a large volume of free
notifications to ZNC Push.  If you're not already using them for your push
service of choice, I highly recommend them.  They have apps for both
[Android][pushover-android] and [iPhone][pushover-iphone], and they continue
to improve them and add new features over time.

And as always, my eternal appreciation to everyone who has contributed time
and energy to helping me improve the module over the past two and a half
years!  The project wouldn't be where it is today without your support.


[ZNC]: http://znc.in
[ZNC Push]: /projects/znc-push
[Pushover]: https://pushover.net
[pushover-android]: https://pushover.net/clients/android
[pushover-iphone]: https://pushover.net/clients/ios
