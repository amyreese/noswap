title: IRC, My Way
description: I describe my IRC setup, how I chat on the go, and how I use my IRC client to chat on AIM and Google Talk.
tags: article, irc, chat, znc
date: 2011-09-13
nocrumbs:
comments: yes
---
This is a post I've been meaning to write for a long time.  I have a rather
complicated setup involving multiple layers, but the end result is amazing.
I maintain a 24/7 presence on the internet -- on multiple IRC servers and
instant messaging services -- and I can send and receive messages from any
computer or device I happen to be using at the time.

From any SSH client, I can seamlessly pick up my IRC session where I last left
it, regardless of where I started that session.  Similarly, I can connect with
my phone's IRC client, get a short backlog of recent conversations, or answer
pending private messages.  When I'm not already engaged in a conversation, I
get near-instant notification on my phone and desktop, allowing me to respond
at my leisure and from any location.  I never miss a private message because
I was connected from the wrong place, other users always see a single nick,
and I get a central, searchable history of every channel and private message.

With this sort of setup, I gain a lot of freedom -- to deal with conversations
on my terms -- and convenience.  It's served me well for a couple years, and
I've enjoyed IRC much more since putting it all together.  For each layer, I'll
detail the tasks it covers, the software I've chosen, and give a copy of any
configuration files or options needed to replicate my environment.

<!-- endexcerpt -->

### IRC Bouncer

This layer is what allows you to maintain a persistent presence on IRC networks,
independent of what IRC client you use.  It connects directly to the IRC server,
acting as a proxy for your client connections.  Commands and messages from your
client are passed to and from the client and remote IRC server, but the benefit
is really in what happens when your client disconnects.

Instead of closing your connection to the IRC network, a bouncer will keep the
connection open, gathering a buffer of recent channel and private messages. When
your client reconnects, it can then replay those messages to your client,
allowing you to catch up on conversations that happened while your client was
offline.  Of course, this relies on your bouncer being able to continue
running when you're offline, and is greatly facilitated by having a server or
shell account to run from, but if you leave your home PC on all the time, you
can run it there too.

Some bouncers have more features than others, but my personal preference is
[ZNC][].  It supports multiple users and/or IRC networks, has a nice C++ API
for writing extension modules, and has a friendly web interface for setting
preferences and managing user accounts.  It also supports SSL on both sides of
the connection, allowing me to remain confident that nobody can eavesdrop on my
private conversations.

ZNC makes a distinction between global modules and user modules.  I personally
use the global fail2ban module for security from brute-force login attempts.
For each user, I generally enable the chansaver, log, and perform modules.
I also set channel buffer sizes to 100, and prepend timestamps -- without the
seconds -- so that I have plenty of context when connecting to the bouncer.

For my purposes, I build ZNC from upstream source releases so that I can apply
a [query buffering patch](https://gist.github.com/1206300); this patch forces
ZNC to buffer incoming private messages, even if a client is already connected.
This allows me to catch up on private messages when connecting from my mobile
client, while my desktop client is still running.  Without the patch, private
messages are only buffered if no client is connected; it works for some, but
I prefer it otherwise.

If you want to build ZNC with this patch, download a release tarball, and use
the following commands, substituting the release version where necessary:

    $ tar xf znc-0.200.tar.gz
	$ cd znc-0.200
	$ wget https://raw.github.com/gist/1206300/7d7024a9b1cbdae711d619e91500ea96060960b5/znc-query-buffering.patch
	$ patch -p1 < znc-query-buffering.patch
	$ ./configure --prefix=/usr/local --enable-extra
	$ make && make install


### Instant Message Bridge

In order to have a single location for all asynchronous chat, I use [Bitlbee][]
to bridge the gap between ZNC and instant messaging services, including AIM and
Google Talk.  Bitlbee acts a lot like an IRC bouncer, except that it implements
multiple chat protocols, and exposes them all as a single, private IRC network.

Online "buddies" show up as nicks in the main channel, devoiced when away.
Conversations can show up in a single main IRC channel or as private messages,
depending on your preferences, while group chats happen in named channels.
IM users don't know that you're using an IRC client to chat with them, and
conversations feel just like any other IRC network.

In my setup, I have ZNC connect to Bitlbee, so that it maintains a permanent
presence, and centralizes the history logs from both IRC and all the IM
networks into a single directory.  It also allows ZNC modules to operate on IM
conversations too, but more on that later.

### IRC Clients

My primary desktop client is [Irssi][].  It's an excellent terminal-based
client, with support for multiple networks, split windows, custom scripts, and
themes. My [custom theme](https://gist.github.com/1207039) is designed for use
with the dark on white Tango color scheme in Gnome Terminal, and my
[configuration](https://gist.github.com/1207051) creates a second highlight
window using the [highlightwin script](http://scripts.irssi.org/html/hilightwin.pl.html)
to give highlights a prominent display.

Where my usage departs from the norm, however, is that instead of running Irssi
on each machine that I want to chat from, I run it on a server, inside of a
persistent [Screen][] session.  This means that Irssi is also running 24/7, and
I can use any machine with an SSH client to connect to the server and attach to
the existing session.  When I get to work in the mornings, or get back home in
the evenings, I just type `irc` into a terminal, and I have Irssi back on the
screen, exactly as I left it.

To accomplish this, I set up a custom `.screenrc`, a server-side shell script,
and a shell alias that turns a local `irc` command into a series of automated
actions.  They log me in to the remote server, set up my environment, and
either attach to screen, or start a new session in case it's not already
running.  For those unfamiliar with the use of Screen, there's a great guide
for [Irssi and Screen][IrssiScreen] written by Matt Sparks that covers the
basics pretty well.

~/bin/screen-irc

    #!/bin/sh

    keychain ~/.ssh/id_rsa
    . ~/.keychain/`hostname`-sh

    screen -Rd irssi -c ~/.screenrc.irssi -p 1

~/.screenrc.irssi

    source ${HOME}/.screenrc

    #windows
    screen -t root
    screen -t irssi irssi
    screen -t user

~/.alias

	alias irc='ssh -t jreese@dyson bin/screen-irc'

On my phone and tablet, I can use the [ConnectBot][] SSH client to connect to
Irssi, but that tends to be less efficient on a device with an on-screen
keyboard; the hotkeys aren't as natural, even with the excellent
[Hacker's Keyboard][hackerskeyboard] installed, and it's not as finger friendly
when scrolling through the backlog.

Instead, I generally prefer to use [AndChat][], a native IRC client for Android.
It supports multiple networks, SSL connections, and works great both on phones
and on tablets with Honeycomb.  When it connects, ZNC sends its buffer of recent
conversations, and I can proceed to chat without anyone knowing or caring that
I've switched to a mobile device.  When I get back to a terminal, I can pick
up on my conversations without any interruption, and all of my mobile chat is
still logged by ZNC.


### Notifications

For times where I'm not paying attention to IRC, I want to be notified when
someone starts talking to me or mentions my name, but traditional on-screen
notification bubbles aren't workable in this setup, so I needed something
better suited to a mobile environment.  This is where ZNC's support for
extension modules is really handy.

I wrote the module [ZNC to Notifo](/projects/znc-notifo) to fill this gap.
It uses a set of configurable conditions to determine when a highlighted
message should trigger a notification, and then sends those notifications
using the excellent service [Notifo][], which in turn uses a push service to
forward those notifications to my phone and my desktop.

With some tweaking to the module options, I have it set so that it never
sends notifications when more than one client is connected -- i.e. AndChat
plus Irssi -- and gives enough lag time after my last messages that I'm not
bombarded with phone notifications:

    +------------------------+------------------------------------------------------------------------------------------------------------+
    | Option                 | Value                                                                                                      |
    +------------------------+------------------------------------------------------------------------------------------------------------+
    | away_only              | no                                                                                                         |
    | channel_conditions     | client_count_less_than and highlight and last_active and (last_notification or replied) and nick_blacklist |
    | client_count_less_than | 2                                                                                                          |
    | highlight              |                                                                                                            |
    | idle                   | 0                                                                                                          |
    | last_active            | 300                                                                                                        |
    | last_notification      | 3600                                                                                                       |
    | message_length         | 100                                                                                                        |
    | message_uri            |                                                                                                            |
    | nick_blacklist         |                                                                                                            |
    | query_conditions       | client_count_less_than and last_active and (last_notification or replied) and nick_blacklist               |
    | replied                | yes                                                                                                        |
    | username               | jreese                                                                                                     |
    +------------------------+------------------------------------------------------------------------------------------------------------+

Unfortunately, with the recent news of [Notifo shutting down](http://blog.notifo.com/notifo),
I will likely be modifying this module to support multiple notification
services, although I'm still not sure of one that fully replicates Notifo's
feature set or platform support.  A [Prowl][] client for Android would be the
closest and most favorable solution to me, although it seems that the
[development has stalled](http://forums.cocoaforge.com/viewtopic.php?f=45&t=20765).
[Notify My Android](http://nma.usk.bz/) also seems a good option, as it's based
on the Prowl API, but is similarly limited to a single platform.

### Alternatives

There are many options for the discerning IRC user.  There are plenty of
clients, both terminal-based and graphical, and many different bouncers to be
found.  For those who may disagree with my preferences, I would like to give a
few alternatives to investigate.

[IRC Junkie][bouncercompare] has a comparison of IRC bouncers, and lists
multiple options, although they agree that ZNC is their favorite.  [psyBNC][]
tends to be the most popular after ZNC, but they list it in third place.

[Weechat][] is a good alternative to Irssi, featuring a large range of plugin
capabilities, and it seems better suited for users with large terminal windows,
due to its ability to display nick and channel lists.  For those who prefer a
GUI, the venerable [XChat][] is a great fit for a Gnome desktop, while
[Quassel][] fits well on a KDE desktop.  Quassel even features its own form of
IRC bouncer for connecting multiple Quassel clients to a single connection.

For viewers on the iOS side of the fence, [Colloquy][] is the most popular
IRC client that I've seen in use, but any generic client should work fine,
and ZNC will smooth out the constant reconnections required of iOS apps.
Colloquy can handle both the IRC client and push notifications, but for those
with a different IRC client, [Prowl][] is also available.  Both services
already have modules available for ZNC, though lacking the high level of
configuration in my Notifo module.

If you have any further suggestions, or if you have questions about my setup,
feel free to share them in the comments.


[AndChat]: http://www.andchat.net/
[BitchX]: http://www.bitchx.com/
[Bitlbee]: http://www.bitlbee.org
[BouncerCompare]: http://www.irc-junkie.org/2009-12-22/irc-bouncer-comparison/ "IRC bouncer comparison"
[Colloquy]: http://colloquy.info/
[ConnectBot]: http://code.google.com/p/connectbot/
[HackersKeyboard]: https://market.android.com/details?id=org.pocketworkstation.pckeyboard
[Irssi]: http://irssi.org/
[IrssiScreen]: http://quadpoint.org/articles/irssi "A Guide to Efficiently Using Irssi and Screen"
[Notifo]: http://notifo.com
[Prowl]: http://www.prowlapp.com/
[psyBNC]: http://www.psybnc.at/
[Quassel]: http://quassel-irc.org/
[Screen]: http://www.gnu.org/s/screen/
[Weechat]: http://www.weechat.org/
[XChat]: http://xchat.org/
[ZNC]: http://wiki.znc.in

