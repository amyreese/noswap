title: Android is Open
description: I rant about people who say Android isn't open because of Google and carriers
date: 2010-10-19
tags: android, comment, google, mobile, open source
nocrumbs:
---
I am biased.  But hopefully I can still be insightful and argue this point.  This was
sparked by a [thread on Hacker News][androidhn], in which someone commented:

> Android is all but open.

I'm calling this out.  Android, as a software project, is completely, 100%, open.  It's
released by Google with the Apache license, which is recognized by OSI and the FSF as a
Free/Libre, Open Source license.  The Android code itself is freely available, freely
redistributable, and can be compiled and flashed onto any compatible device.

*However*, there is a significant portion of the Android ecosystem that *is not*
"open" by the same definitions above:

* Device drivers for individual phones are open or closed depending on the device
  and the individual chipsets in question, but that is a moot point in my opinion as
  there are plenty of people who use Free desktop operating systems with closed "binary"
  drivers. Therefore I will leave this topic for another discussion.

* All of the Google-branded applications -- including the
  Market, Gmail, and Maps -- are closed-source and must be licensed with Google to be
  included on a phone.  This means that Cyanogen is not allowed to include these apps when
  he releases his amazing CyanogenMod firmware.  Other services that Google then builds on
  top of these closed applications are also closed by nature, including their proprietary
  "push" communication model.

For some purists, this is a major problem, and I would generally agree.  But unlike Apple
and iOS devices, none of these Google-branded apps are "privileged" applications; they
don't get special treatment from Android, and they don't have access to anything that
"normal" applications can't access through the SDK.

But more importantly, these apps are *not* Android, and they are not necessary to
delivering an Android phone or firmware.  Developers can write and release competing or
nearly indentical applications that replace these closed system apps, and indeed, there
are multiple competing "app stores" for Android, with Amazon rumored to be creating yet
another.  There are even better alternatives for Chrome to Phone already available.  And
if you insist on not using -- or have a phone without -- the Android Market, Android is
perfectly capable of "side-loading" software packages, and nobody needs to pay Google
for the rights to do so.

> What is all this proclaimed openness worth if it still boils down to exploiting
> security systems if you want to run that system you just modified?

*That* is the real problem, and in my opinion the blame is firmly with the carriers; not
Google, and certainly not Android.  I specifically purchased a Nexus One because it supports
the ability to flash the phone with unsigned firmware.  I can download the Android source
code, compile it, and flash that resulting firmware to my phone, without needing to root,
exploit, or jailbreak my phone.  I could do that with my Openmoko Freerunner, and I can do
that with my Nexus One.

If enough people insisted on purchasing phones with this capability, then the carriers and
manufacturers would pay attention and deliver. Or perhaps Google should be standing up to
carriers and demanding that all Google-branded and licensed Android phones have this
capability.  But even if they could get away with that demand, they can't enforce it on
all Android devices; the very definition of Free Software allows carriers and manufacturers
to take Android and do what they want with it if they don't like Google's terms.

Maybe the real lesson is that Free Software is a double-edged sword, and if you want
corporations to join in, you have to be willing to play their game too.

[androidhn]: http://news.ycombinator.com/item?id=1806441
