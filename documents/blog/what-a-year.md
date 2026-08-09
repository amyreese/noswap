title: What a Year...
date: 2026-08-08
tags: me, pycon, excavacon
sig: '<i class="fa fa-truck-pickup"></i>'
---

The past year or so has truly been a decade. Many things that probably should
have deserved a post of their own at the time, but not for the state of the
world and what I've been dealing with...

<div class="thumbnails">
    <img alt="What a week, meme from 30 Rock" src="/media/what-a-week.png"/>
</div>

I generally don't like talking about myself — part of the reason this site goes
untouched for so long, I don't know what I even want to say. I know I live
an incredibly privileged life, so talking about me, even my problems, makes
me feel... guilty? Perhaps normalizing this discussion is part of the solution.

So I apologize for this long simmering catharsis, but I promise you there's some
good news waiting for you [at the end](#what-a-year-ending), though if you
follow me on [socials](https://amethyst.cat), you may already know the basics.

---

#### January 2025

I got a "meets most" performance rating for the previous year at Meta, due to a
combination of factors, including pivoting from planned projects to assist IG
in rolling out Ruff formatting, getting excluded from meetings in which other
teams assigned me work but never informed me, a new manager not caring about
why my developer tooling work was important, and my own general distaste for
chasing "shiny" projects. All of my peer feedback was glowing, but I've
learned the hard way at Meta that positive peer feedback rarely affects your
final performance rating.

I was moved onto a different developer tooling project that AI teams *did*
want, but between needing to learn Rust, and what I had planned for March,
there wouldn't be much time for me to make progress on that project's goals.
All the while, I was periodically receiving emails from my manager that felt
like they were building a [PIP](https://en.wikipedia.org/wiki/Performance_improvement#Performance_Improvement_Plans_(PIPs))
without actually putting me on a PIP. I've been through one many years ago
at <strike>Facebook</strike> Meta, successfully passed it, and saw a promotion
on the other side. But everything changed after the layoffs in 2021.

#### March 2025

I had GC surgery from one of the best doctors in the business, paid in full
by Meta and MZ, a month before my 40th birthday. 💃 🎉  It was the best present
I could have ever asked for.

The hardest part was dealing with the literal insanity the pain killers put
me through in the first few days, but once I was down to just ibuprofen,
the healing process went really smoothly. I took two months off work for
recovery, spent a lot of time on the couch and with friends, and came back
just in time for PyCon US.

#### May 2025

PyCon US! The second year in Pittsburgh, and it felt otherwordly to finally be
there as *me*. I gave a reprisal of [my "Or Else!" talk](https://pyvideo.org/pycon-us-2025/or-else-an-exploration-of-obscure-control-flow.html)
from North Bay Python, marking the first time I'd been on stage at PyCon US
under my true name, and the only speaker who included an emoji in their name 😹.

<div class="thumbnails">
    <img width="217" alt="My PyCon US speaker card" src="/media/pycon-2025-speaker.png" />
</div>

The talk went well — certainly better than the technical disaster of my 2022
appearance — though the audience was far less engaged in my shenanigans than
the beautiful folks at NBPy.

I also talked to a friend and former coworker about my concerns over where
Meta was heading, and applied for a new job after 13 years working at MPK...

I then finished out May participating in my first-ever endurance road race,
as a driver for the ["Electric Turtle"](https://www.caranddriver.com/features/a65177882/ev-lemons-endurance-racing/)
team running a 2018 Chevy Bolt in the 25 hour [Lemons](https://24hoursoflemons.com/)
race at Thunderhill. Temperatures reached well over 100°F in the shade, but the
car provides a unique driving challenge, including how we "tow charge" during
each race, and I've gone back for three more races with them since.

#### July 2025

At the start of the month, after an amazingly humanizing interview process,
I accepted an offer from [Astral](https://astral.sh) with plans to join them in
August, working on the Ruff linter. I was excited to work on a small team again,
and even moreso to work at a small company, without planning my life around
six month performance review cycles and repeatedly convincing managers that
what I worked on was important enough to keep me around.

I did not tell anyone at Meta.

At the end of the month, I got my final performance review from Meta — the
feeling was mutual. I didn't even get to say farewell to my team mates before
being locked out of internal tools, though of course we had side channels where
I could finally give them the good news:

<div class="thumbnails">
    <img width="448" alt="I've been officially terminated y'all" src="/media/terminated-2025.png" />
</div>


#### August 2025

I had three weeks of gardening leave, and promptly caught COVID on day one. 💀

I'd managed to avoid it for five years, until my luck ran out. This was during
the "razor blade throat" era, but thankfully it wasn't severe, almost certainly
the result of diligently seeking out every round of vaccine I could
get my shoulders into.  It still turned those three weeks into unending
exhaustion and discomfort.

In the background of all this, the relationship with my spouse was slowly
disintegrating. After twenty years of loving and affectionate marriage,
we were in couples therapy.

#### October 2025

They started working again, for the first time in over a decade. Therapy ended
due to scheduling conflicts. They admitted to me that they had been cheating on
me with someone from our car club. I'd never had a panic attack before.

Through this, I was somehow shipping bug fixes and small features in Ruff, 
including some major refactoring to treat fatal panics as diagnostics alongside
lint errors. I would lose a morning or afternoon here and there to grief.
That became the new normal.

I began planning and design to implement new system for "ranged" suppression
comments. For so many reasons, this would take longer — and involve more
back-and-forth discussions and code review — than any of us had ever expected.

#### November 2025

The Astral team traveled to New York City for semi-annual planning, and I got
to finally meet my team mates in person. They were all lovely and so welcoming,
and it provided a glimpse of what the Python Foundation team used to feel like
at Meta. We even trudged through the bitter Brooklyn cold to get ice cream
after a team dinner.

<div class="thumbnails">
    <img alt="Astral folks bundled up in the cold eating ice cream" src="/media/nyc-2026-icecream.jpeg"/>
</div>

As luck had it, my former team from Meta was also in town the same week, so
I packed a fancy dress for the trip to join them at a very nice restaurant in
Manhatten. It was the perfect opportunity to spend time with friends that I
rarely got to see in person after the remote work diaspora.

#### December 2025

The first pieces of range suppressions became available in Ruff's preview mode.
Matching `# ruff:disable` and `# ruff:enable` comments could be used to cover
arbitrary blocks of code, using a new comment syntax that would finally be
distinct from other linters.

Meanwhile, my spouse told me they wanted to try living on their own, and would
start looking for places in the new year. I had another panic attack. I couldn't
believe there wasn't a way to turn things around, to save our marriage. 

They were upset that I got them presents, because then they felt obligated to
get me something in return. I spent most of Christmas day alone while they
celebrated with the other one and his mother.
I was trying everything I could to convince them to stay,
to try and find a way forward together.

#### January 2026

I shipped the remaining pieces of block-level range suppressions, mostly focused
on consolidating overlapping diagnostics, and improving performance of the new 
system. It was scheduled to get stabilized with the next major release
in February.

That project had taken too long to get shipped though, and I was given a choice
between quitting with severance, or being put on a PIP. I chose the PIP. The
acceptance criteria was getting Markdown code block formatting implemented and
shipped. I got the feature prototyped and merged by the end of the month.

My spouse said the words "when I'm gone".

#### February 2026

The next major release of Ruff shipped, stabilizing the range suppression
system, and bringing the Markdown code block formatting to preview mode.
I would then ship support for the feature in the LSP, improve the parser
and code block language detection, and support `pycon` interactive console
style, achieving the stretch goals of the PIP within three and a half weeks.

I wouldn't get a definitive resolution until my manager got back from a
month-long vacation, so I started working on the next project in our shared
backlog: replacing Flake8-style error codes with human readable rule names.
While the prototype was simple and straightforward, finding the right way to
ship this feature to users was not; there was major overlap with other pending
work, including the new default rule set, and potential changes to configuration.

LLM generated issues and pull requests were beginning to take a toll on my love
for open source. Being part of such a big project was absolutely overwhelming,
and constantly trying to decide whether contributions — and contributors — were
legitimate or just slop was an unwanted tax on both my time and my emotions.

#### March 2026

I officially passed the PIP. And then Charlie told us that he accepted an
acquisition offer, from [OpenAI][] of all companies.

[OpenAI]: https://www.msn.com/en-in/news/world/sam-altman-a-pathological-liar-experts-suggest-openai-in-wrong-hands/ar-AA20zW4s

<div class="thumbnails">
    <a href="https://toots.n7.gg/@amethyst/116251209745359081">
        <img width="630" alt="Screenshot of toot from me saying 'Fuck'" src="/media/fuck.png"/>
    </a>
</div>

Even worse, because I was still "new" to Astral, I would have to interview
with OpenAI for my own job — coding, systems design, and behavioral. We were
given space to spend a couple weeks focusing on interview prep, and I
legitimately tried to prepare, even though I was extremely conflicted about
the entire situation. I did mock interviews for all three types, though no
one could truly prepare for the behavioral.

The public announcement did give me some interesting conversations
[at PyCascades](https://toots.n7.gg/@amethyst/116257518939980849) though.
And of course, Vancouver was incredible as always.

<blockquote class="mastodon-embed" data-embed-url="https://toots.n7.gg/@amethyst/116275669726660433/embed" style="background: #FCF8FF; border-radius: 8px; border: 1px solid #C9C4DA; margin: 0; max-width: 540px; min-width: 270px; overflow: hidden; padding: 0;"> <a href="https://toots.n7.gg/@amethyst/116275669726660433" target="_blank" style="align-items: center; color: #1C1A25; display: flex; flex-direction: column; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Roboto, sans-serif; font-size: 14px; justify-content: center; letter-spacing: 0.25px; line-height: 20px; padding: 24px; text-decoration: none;"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32" height="32" viewBox="0 0 79 75"><path d="M63 45.3v-20c0-4.1-1-7.3-3.2-9.7-2.1-2.4-5-3.7-8.5-3.7-4.1 0-7.2 1.6-9.3 4.7l-2 3.3-2-3.3c-2-3.1-5.1-4.7-9.2-4.7-3.5 0-6.4 1.3-8.6 3.7-2.1 2.4-3.1 5.6-3.1 9.7v20h8V25.9c0-4.1 1.7-6.2 5.2-6.2 3.8 0 5.8 2.5 5.8 7.4V37.7H44V27.1c0-4.9 1.9-7.4 5.8-7.4 3.5 0 5.2 2.1 5.2 6.2V45.3h8ZM74.7 16.6c.6 6 .1 15.7.1 17.3 0 .5-.1 4.8-.1 5.3-.7 11.5-8 16-15.6 17.5-.1 0-.2 0-.3 0-4.9 1-10 1.2-14.9 1.4-1.2 0-2.4 0-3.6 0-4.8 0-9.7-.6-14.4-1.7-.1 0-.1 0-.1 0s-.1 0-.1 0 0 .1 0 .1 0 0 0 0c.1 1.6.4 3.1 1 4.5.6 1.7 2.9 5.7 11.4 5.7 5 0 9.9-.6 14.8-1.7 0 0 0 0 0 0 .1 0 .1 0 .1 0 0 .1 0 .1 0 .1.1 0 .1 0 .1.1v5.6s0 .1-.1.1c0 0 0 0 0 .1-1.6 1.1-3.7 1.7-5.6 2.3-.8.3-1.6.5-2.4.7-7.5 1.7-15.4 1.3-22.7-1.2-6.8-2.4-13.8-8.2-15.5-15.2-.9-3.8-1.6-7.6-1.9-11.5-.6-5.8-.6-11.7-.8-17.5C3.9 24.5 4 20 4.9 16 6.7 7.9 14.1 2.2 22.3 1c1.4-.2 4.1-1 16.5-1h.1C51.4 0 56.7.8 58.1 1c8.4 1.2 15.5 7.5 16.6 15.6Z" fill="currentColor"/></svg> <div style="color: #787588; margin-top: 16px;">Post by @amethyst@n7.gg</div> <div style="font-weight: 500;">View on Mastodon</div> </a> </blockquote> <script data-allowed-prefixes="https://toots.n7.gg/" async src="https://toots.n7.gg/embed.js"></script>

Oh, and I was voted to be the newest board member for the
[Bay Area Python Association](https://bapya.org), the group that runs and
oversees the PyBay conference, as well as the SFPython, BayPIGgies, and
Pyninsula meetup groups.

#### April 2026

The interviews happened. Coding and systems seemingly went off without a hitch,
though the behavioral turned out to really be asking "how AI pilled are you".
While I'm not sure if it was the behavioral or the PIP that did me in, I did not
receive an "offer" from OpenAI — the only engineer to not receive one. I'm sad
to have missed the paycheck, but I'm glad I wasn't given the option to work at
another soulless megatech, particularly that one.

With the deal closing at the end of the month, I was free to work on whatever
I wanted to. I took the time to build on top of the range suppression system,
adding statement-level `# ruff: ignore` and file-level `# ruff: file-ignore`
suppressions types, truly giving Ruff its own identity from `# noqa`.

The company gathered in Montreal for one last outing as an independent team —
I dubbed it my farewell tour — and yet again Canada delivered beautiful weather,
and excellent public transit. I rode more trains in one short week than I do
in most years. The week was bittersweet, knowing it was the last time I could
call such an excellent group of colleagues my team mates.

I got home just in time for my favorite regional barn cat conference,
<strike>ExcavaCon</strike> [North Bay Python](https://pyvideo.org/events/north-bay-python-2026.html).
The talks were excellent — clearly because I helped pick them — and cats were
everywherew both in person and in slides, and the ice cream selfie included
many amazing friends.

The next day I celebrated my 41st birthday, and the day after that the Astral
acquisition deal closed, leaving me as a free agent for the first time in over
fourteen years.

<blockquote class="mastodon-embed" data-embed-url="https://toots.n7.gg/@amethyst/116489297733781352/embed" style="background: #FCF8FF; border-radius: 8px; border: 1px solid #C9C4DA; margin: 0; max-width: 540px; min-width: 270px; overflow: hidden; padding: 0;"> <a href="https://toots.n7.gg/@amethyst/116489297733781352" target="_blank" style="align-items: center; color: #1C1A25; display: flex; flex-direction: column; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Roboto, sans-serif; font-size: 14px; justify-content: center; letter-spacing: 0.25px; line-height: 20px; padding: 24px; text-decoration: none;"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32" height="32" viewBox="0 0 79 75"><path d="M63 45.3v-20c0-4.1-1-7.3-3.2-9.7-2.1-2.4-5-3.7-8.5-3.7-4.1 0-7.2 1.6-9.3 4.7l-2 3.3-2-3.3c-2-3.1-5.1-4.7-9.2-4.7-3.5 0-6.4 1.3-8.6 3.7-2.1 2.4-3.1 5.6-3.1 9.7v20h8V25.9c0-4.1 1.7-6.2 5.2-6.2 3.8 0 5.8 2.5 5.8 7.4V37.7H44V27.1c0-4.9 1.9-7.4 5.8-7.4 3.5 0 5.2 2.1 5.2 6.2V45.3h8ZM74.7 16.6c.6 6 .1 15.7.1 17.3 0 .5-.1 4.8-.1 5.3-.7 11.5-8 16-15.6 17.5-.1 0-.2 0-.3 0-4.9 1-10 1.2-14.9 1.4-1.2 0-2.4 0-3.6 0-4.8 0-9.7-.6-14.4-1.7-.1 0-.1 0-.1 0s-.1 0-.1 0 0 .1 0 .1 0 0 0 0c.1 1.6.4 3.1 1 4.5.6 1.7 2.9 5.7 11.4 5.7 5 0 9.9-.6 14.8-1.7 0 0 0 0 0 0 .1 0 .1 0 .1 0 0 .1 0 .1 0 .1.1 0 .1 0 .1.1v5.6s0 .1-.1.1c0 0 0 0 0 .1-1.6 1.1-3.7 1.7-5.6 2.3-.8.3-1.6.5-2.4.7-7.5 1.7-15.4 1.3-22.7-1.2-6.8-2.4-13.8-8.2-15.5-15.2-.9-3.8-1.6-7.6-1.9-11.5-.6-5.8-.6-11.7-.8-17.5C3.9 24.5 4 20 4.9 16 6.7 7.9 14.1 2.2 22.3 1c1.4-.2 4.1-1 16.5-1h.1C51.4 0 56.7.8 58.1 1c8.4 1.2 15.5 7.5 16.6 15.6Z" fill="currentColor"/></svg> <div style="color: #787588; margin-top: 16px;">Post by @amethyst@n7.gg</div> <div style="font-weight: 500;">Yesterday was my last day at Astral, as the acquisition by OpenAI closed. It's unfortunate that my time there was short, but I'm proud of what I've accomplished...</div> </a> </blockquote> <script data-allowed-prefixes="https://toots.n7.gg/" async src="https://toots.n7.gg/embed.js"></script>

#### May 2026

This was the beginning of my "early retirement" moment. I was blessed with
a healthy financial runway courtesy of my tenure at Meta, which while not
enough to enable an *actual* retirement, gave me the space to take time off and
not rush into an immediate job search, though I did apply for a couple roles
at the PSF. 

Unfortunately, I was forced to spend a significant amount of energy harrassing
Astral/OpenAI to get my COBRA insurance set up, and I'm still *extremely*
unhappy about everything relating to that, but that is perhaps better to be
shared with friends over a drink or two, so I can rant about it accordingly.

I went to PyCon US, mercifully still on Astral's dime, thanks to the good graces
of Charlie and prebooked travel reservations. I took the Coast Starlight train
from San Jose to Long Beach, in the company of a friend, though the mood
for the week was killed before I even boarded the train. The night before
leaving, my spouse had informed that they wanted to start talking to lawyers...
and somehow thought it better to tell me before the conference rather than
after. I almost didn't even go at all.

This colored most of my week there, making for one hell of a roller coaster
of emotions. If I looked or acted out of character, this is why. I'm sorry.
Though, as always, I appreciated the opportunity to catch up with old friends,
meet new people, and this year most of all, it was therapeutic to bask in the
sunlight of Long Beach — literally. I made a habit of
[swimming in the rooftop pool every night](https://toots.n7.gg/@amethyst/116593697809947445)
until it closed. I'm glad I went.

<div class="thumbnails">
    <img alt="Me basking in the bay window of the hotel in Long Beach" src="/media/pycon-2026-basking.jpeg" />
</div>

Thankfully I did not need to give a talk this year, so instead, I volunteered
where I could: registration, the information desk, and the PSF booth to name
a few. I also hosted an LGBTQ+ Social open space again, which was well stocked
with plenty of excellent people, and I attended a number of other open spaces,
including one about space! I visited the aquarium with some friends, and I
attended a rooftop happy hour overlooking the
[Long Beach street circuit](https://en.wikipedia.org/wiki/Long_Beach_Street_Circuit)
before realizing that I'd literally walked past the circuit's iconic fountain
section the day before without even realizing it! 😅

The journey home was once again on the Coast Starlight, though this time alone.
I managed to successfully "bid" for a roomette, giving me a more private space
to take in the scenery while thinking about the week and zoning out to some
podcasts and youtube videos. Once again, the views were spectacular, and I even
took a turn at [#train tooting](https://toots.n7.gg/@amethyst/tagged/train).

<blockquote class="mastodon-embed" data-embed-url="https://toots.n7.gg/@amethyst/116603622686740071/embed" style="background: #FCF8FF; border-radius: 8px; border: 1px solid #C9C4DA; margin: 0; max-width: 540px; min-width: 270px; overflow: hidden; padding: 0;"> <a href="https://toots.n7.gg/@amethyst/116603622686740071" target="_blank" style="align-items: center; color: #1C1A25; display: flex; flex-direction: column; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Roboto, sans-serif; font-size: 14px; justify-content: center; letter-spacing: 0.25px; line-height: 20px; padding: 24px; text-decoration: none;"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32" height="32" viewBox="0 0 79 75"><path d="M63 45.3v-20c0-4.1-1-7.3-3.2-9.7-2.1-2.4-5-3.7-8.5-3.7-4.1 0-7.2 1.6-9.3 4.7l-2 3.3-2-3.3c-2-3.1-5.1-4.7-9.2-4.7-3.5 0-6.4 1.3-8.6 3.7-2.1 2.4-3.1 5.6-3.1 9.7v20h8V25.9c0-4.1 1.7-6.2 5.2-6.2 3.8 0 5.8 2.5 5.8 7.4V37.7H44V27.1c0-4.9 1.9-7.4 5.8-7.4 3.5 0 5.2 2.1 5.2 6.2V45.3h8ZM74.7 16.6c.6 6 .1 15.7.1 17.3 0 .5-.1 4.8-.1 5.3-.7 11.5-8 16-15.6 17.5-.1 0-.2 0-.3 0-4.9 1-10 1.2-14.9 1.4-1.2 0-2.4 0-3.6 0-4.8 0-9.7-.6-14.4-1.7-.1 0-.1 0-.1 0s-.1 0-.1 0 0 .1 0 .1 0 0 0 0c.1 1.6.4 3.1 1 4.5.6 1.7 2.9 5.7 11.4 5.7 5 0 9.9-.6 14.8-1.7 0 0 0 0 0 0 .1 0 .1 0 .1 0 0 .1 0 .1 0 .1.1 0 .1 0 .1.1v5.6s0 .1-.1.1c0 0 0 0 0 .1-1.6 1.1-3.7 1.7-5.6 2.3-.8.3-1.6.5-2.4.7-7.5 1.7-15.4 1.3-22.7-1.2-6.8-2.4-13.8-8.2-15.5-15.2-.9-3.8-1.6-7.6-1.9-11.5-.6-5.8-.6-11.7-.8-17.5C3.9 24.5 4 20 4.9 16 6.7 7.9 14.1 2.2 22.3 1c1.4-.2 4.1-1 16.5-1h.1C51.4 0 56.7.8 58.1 1c8.4 1.2 15.5 7.5 16.6 15.6Z" fill="currentColor"/></svg> <div style="color: #787588; margin-top: 16px;">Post by @amethyst@n7.gg</div> <div style="font-weight: 500;">View on Mastodon</div> </a> </blockquote> <script data-allowed-prefixes="https://toots.n7.gg/" async src="https://toots.n7.gg/embed.js"></script>

<a name="what-a-year-ending"></a>

#### July 2026

The owner of [Electric Turtle](https://www.caranddriver.com/features/a65177882/ev-lemons-endurance-racing/),
the Lemons racing team I drive for,
got me in touch with a local startup that he had invested in. It's a hardware
company, building a really cool product squarely targeted at my own interests.
They were looking for someone to join their small software team to help prepare
the product to attract further investment and bring it into production.

I had a couple chats with the CEO, and then they invited me to come onsite,
take a look at the product first hand, and do some light interviews with their
engineers and the other cofounder. It was a really great experience, and
everyone there was quite friendly and excited to meet me. The last interview
with the cofounder had me nervous though, as he asked about how I use "AI".
I did my best to answer truthfully — I just don't — and explain how I feel
about LLMs, and why I don't find them helpful, although I skipped most of my
usual rant about ethics. 😅 I went home at least satisfied that I'd been honest,
and would earn the job on my own terms.

The week before this, my spouse stayed the night at their new place, a single
rented room further away from where they work. They haven't lived here since
then. It still hurts that they feel that is better than the house and life
we spent all these years building together. 
It's now just me and the cat in a house full of reminders.

#### Now

I got email from the startup CEO. He asked when was a good time for a phone call.
I could only assume this was for a soft letdown.
But I'm extremely excited to announce that they made me an offer, and that I've
accepted their offer!

Starting on Monday morning, I'll be the newest engineer working at
[Telo Trucks](https://www.telotrucks.com/). 😸

<div class="thumbnails">
    <a href="/media/telo-2026-city.jpg">
        <img alt="" src="/media/telo-2026-city.jpg" />
    </a>
</div>

The Telo MT1 is a battery electric mini-truck the size of a modern Mini Cooper,
and yet still seats four adults, has a 5' bed, and is
[rated to tow over 3 tons](https://youtu.be/pLU4RdnI_Xk).
Again, firmly targeted at this Bay Area car chick who desperately wants a small
EV that can tow her sports car to the track while carrying a full set of extra
wheels and all of her track day gear. If that sounds interesting to you too,
then you can [reserve your own Telo MT1](https://build.telotrucks.com/) for
just $152.

I'm looking forward to working on a combination of backend services, in-car
components, and perhaps even a mobile app. Anything I can to help bring this
lovely little truck to serial production. I've never worked on anything like
this before, and that's honestly kind of exhilarating.
I'm optimistic for once.

Thank you for listening.
