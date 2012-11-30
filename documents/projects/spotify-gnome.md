title: Spotify Gnome Integration
description: With Spotify now available for those of us in the USA, I set about wiring up the Spotify client on Linux to handle Gnome's media keys.
tags: spotify, linux
date: 2011-07-15
menu-parent: 5
menu-position: 57
menu-title: Spotify Gnome
---

Spotify-Gnome is a program that provides Gnome media key support for the
[Spotify Linux client](http://www.spotify.com/us/download/previews/).
It supports the play/pause, stop, next, and previous signals, and is compatible with
both Gnome 2 and Gnome 3.

The Spotify client supports DBus for controlling the player, using the
[MPRIS Specification](http://www.mpris.org/2.1/spec/), but does not listen for basic
media key signals provided by Gnome.  This program acts as a "wrapper" around Spotify
to translate media key signals from Gnome and send them to the Spotify client.


The program is released under the MIT license, and the source code and documentation can be
found on the project's [Github repository](https://github.com/jreese/spotify-gnome) page.

Many thanks to [Mike Houston at kothar.net](http://kothar.net/index.php/blog/30-spotifydbus)
and [Fran Dieguez at Mabishu](http://www.mabishu.com/blog/2010/11/15/playing-with-d-bus-interface-of-spotify-for-linux/)
for their blog postings that pointed me in the right directions to get this implemented.

