title: Mantis Bug Tracker
parent: projects/index
pages: "'tags' in page and 'mantisbt' in page['tags']"
template: posts.html
---
As a core developer for the [Mantis Bug Tracker][mantisbt], I've implemented many various features for the
application, including the plugin system introduced with the 1.2.0 release of MantisBT.  Using this
intimate knowledge, I've created an array of plugins, from simple tasks of integrating web analytics to
the complex task of generalized source control integration.

## Source Control Integration

My premiere plugin set, this package provides a generalized framework for integrating source control
repositories within the normal MantisBT workflow.  Building on that framework are a set of integration
plugins that implement individual VCS tools, and translate that data into the framework's generalized
data types.  Once translated, the framework can act on those datasets in many ways to improve the workflow
in MantisBT, or to better inform developers and team members when looking at issues.

[Read more...](/projects/source-integration/)

## Other Plugins

* [Announcements][announce] -- Plugin to allow privileged accounts to create and post announcements that
  can be shown to users on a global or per-project basis, and allow users to dismiss individual messages.

* [Inline History][inline] -- Allow individual users to view isse history elements inline with the issue
  notes, rather than being in separate data blocks.

* [Product Matrix][pvm] -- Alternate method for defining a set of products, each with a hierarchical set
  of versions, and allowing individual issues to track its status against multiple product versions at the
  same time, without the need for cloning issues.

* [Snippets][] -- Define global or per-user text snippets that can be pasted into the text box when
  creating a note on any issue.

* [Timecard][] -- Potential replacement for the built-in time tracking feature with new features including
  the option to specify an estimated time requirement for each issue, and then view time statistics on a
  per-project basis.

* [Google][ga], [Piwik][], [Clicky][], and [Woopra][] analytics integrations.

[mantisbt]: http://www.mantisbt.org/ "Mantis Bug Tracker"
[mantisforge]: http://git.mantisforge.org/ "MantisForge"
[announce]: http://git.mantisforge.org/w/announce.git "Announcement Plugin"
[inline]: http://git.mantisforge.org/w/inline-history.git "Inline History Plugin"
[pvm]: http://git.mantisforge.org/w/product-matrix.git "Product Matrix Plugin"
[snippets]: http://git.mantisforge.org/w/snippets.git "Snippets Plugin"
[timecard]: http://git.mantisforge.org/w/timecard.git "Timecard Plugin"

[ga]: http://git.mantisforge.org/w/google-analytics.git "Google Analytics Plugin"
[piwik]: http://git.mantisforge.org/w/piwik.git "Piwik Analytics Plugin"
[clicky]: http://git.mantisforge.org/w/clicky.git "Clicky Analytics Plugin"
[woopra]: http://git.mantisforge.org/w/woopra.git "Woopra Analytics Plugin"
