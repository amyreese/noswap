title: Mantis Bug Tracker
menu-parent: 5
menu-position: 51
menu-title: Mantis Bug Tracker
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

[mantisbt]: http://www.mantisbt.org/ "Mantis Bug Tracker"
[mantisforge]: http://git.mantisforge.org/ "MantisForge"
[bugtracker]: http://leetcode.net/mantis/ "LeetCode.net Bugtracker"
[sourcerepo]: git://git.mantisforge.org/source-integration.git "Source Integration Repository"
