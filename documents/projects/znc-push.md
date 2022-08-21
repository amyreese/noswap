title: ZNC Push
description: Push notification module for ZNC
tags: irc, znc
date: 2011-10-06
parent: projects/index
---

Based around the core conditions and functionality from my [original project][ZNC to Notifo],
ZNC Push is a module for [ZNC][] that will send push notifications to multiple
services for any private message or channel highlight that matches a
configurable set of conditions, including the user's `/away` status, time since
the last notification, number of clients connected to ZNC, and more.  Currently
supported push services include [Boxcar][], [NMA][], [Notifo][], [Pushover][],
[Prowl][], and [Supertoasty][].

The module is released under the MIT license, and the source code and
full documentation can be found on the project's [Github repository][github] page.

[github]: http://github.com/amyreese/znc-push "ZNC Push on Github"
[ZNC]: http://en.znc.in "ZNC, an advanced IRC bouncer"
[ZNC to Notifo]: /projects/znc-notifo/ "ZNC to Notifo"

[Boxcar]: http://boxcar.io
[NMA]: http://notifymyandroid.com
[Notifo]: http://notifo.com
[Pushover]: http://pushover.net
[Prowl]: http://www.prowlapp.com
[Supertoasty]: http://supertoasty.com

