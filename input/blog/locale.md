title: Locale
description: Locale for Android is an excellent application for automating settings changes based on configurable conditions.
tags: android, mobile, comment
date: 2011-04-25
---
Fred Wilson's [recent post][localeavc] on Locale for Android was on Hacker News today, and
although I [commented there][localehn] on why I like Locale, I want to expound on that a bit
further.

I bought the very first Android phone, the T-Mobile G1, when it was first released over two years
ago.  Even then, [Locale][] was big news for the platform, having won the very first [Android
Developer Challenge][adc1].  I have been using it on all my Android phones since then, and I
continue to be impressed by it.

Locale is *the* killer app for Android.  It embodies everything that Android is capable of, and
everything that Apple refuses to allow in iOS.  My phone can now be smart enough that I don't have
to babysit its settings everywhere I go; it knows when to be discreet and when to be secure.  No
other mobile OS can do that.

For a quick background, Locale is an application for automating changes to your phone's settings
based on a configurable set of "situations".  You define a set of "defaults", and then each
situation is comprised of a set of "conditions" and "settings".  When a situation's conditions are
met, the associated settings override the defaults; when the conditions are no longer met, Locale
returns to the default settings.  By combining multiple situations together in a priority list,
your phone can make intelligent decisions, and seamlessly switch between multiple situations as
they become active or inactive.

But what makes Locale even better is that it was designed from the beginning to be extensible.
You can find plugins on the Market that add new conditions and settings.  Because of Android's
ability to share data between applications, these plugins can even go so far as to use context
from, or modify behavior of, other applications installed on your phone.  As an example, the
[Astrid task manager][astrid] allows you to attach a location to your tasks, and integrates with
Locale as a condition when you reach those locations.

But for a more concrete example of just what's possible, I'd like to show you what my current
Locale conditions and settings are.

* **Defaults**: Wifi off, Ringer volume 85%, Vibrate on, Media volume 70%, Password lockscreen on
* **Night** (Time 10pm-7am): Ringer off, Vibrate off
* **Work** (Location): Wifi on, Ringer off, Vibrate on,
* **Headphones** (Headphones connected): Media volume 20%
* **Home** (Location): Wifi on, Ringer volume 100%, Password lockscreen off

The Locale plugins that I use to accomplish this:

* [Locale Password Lock Plug-in][localepassword] by Willem Stoker
* [Locale Media Volume Plug-in][localemedia] by two forty four am
* [Headphones Plug-in][localeheadphones] by two forty four am

Color me happy.


[locale]: http://www.twofortyfouram.com/ "Locale"
[localeheadphones]: https://market.android.com/details?id=com.twofortyfouram.locale.condition.headphones
[localemedia]: https://market.android.com/details?id=com.twofortyfouram.locale.setting.media_volume
[localepassword]: https://market.android.com/details?id=com.willemstoker.PasswordPlugin
[localeavc]: http://www.avc.com/a_vc/2011/04/locale.html "Fred Wilson on Locale"
[localehn]: http://news.ycombinator.com/item?id=2484844 "Why I like Locale"
[astrid]: http://www.weloveastrid.com/ "Astrid"
[adc1]: http://code.google.com/android/adc/adc_gallery/#1 "Android Developer Challenge 1"
