title: Source Integration Triage
description: I list common problems and solutions for source integration users.
tags: mantisbt, source integration
date: 2011-06-30
---
When users are having troubles with setting up the source integration plugin with their repositories, I've
found that there is a common set of pain points.  I'm going to list them here, along with their respective
solutions, in hopes that users can more easily find the fixes in the future.  This post will be updated as
new tips or advice arrive.

#### General

*	Linking changesets to issues requires commit messages to match the regular expressions specified in the
	source integration configuration page.  By default, phrases like "fixes #123" or "resolved #123, #123"
	are supported, in present, past, singular, and plural forms.

*	Remote checkin must be enabled for use by post-commit hooks that don't use an API key to authenticate,
	and must list the IP addresses or blocks for any repository server that will push commit data to Mantis.

*	Remote imports must be enabled for use by cronjob-based scripts that will trigger Mantis to pull in new
	changeset data for a given repository.

#### Subversion

*   Your web server needs to have the SVN client binaries installed, and they must be accessible by the
	account that your web server uses.  Similarly, if the binaries are in a directory that's not included in
	your web server's default path, you will need to specify the directory path in your source integration
	configuration.  On Linux, this is usually `/usr/bin` or `/usr/local/bin` -- on Windows, something like
	`c:/path/to/subversion/bin` is likely required.

*	For Windows servers, you may also need to enable the "Windows start" source integration option.

*	Make sure that the individual repository URL that you use for Mantis is the same URL you would use to
	checkout the repository when using an SVN client.

*	When using repositories that require authentication, make sure the username and password you enter in
	Mantis has read access to the entire repository.

*	If your repositories are hosted using HTTPS/SSL, and your server is using self-signed certificates, you
	will need to have SVN version 1.6 or newer installed, and you will need to enable the "Trust all SSL
	certs" option from source integration.

*	If your commit messages contain UTF-8 or other non-ASCII characters, or your system's locale is not set
	to "en_US", then you may need to look at issue [#93][issue-93] and [#130][issue-130] on my bug tracker
	for help modifying your server or SourceSVN plugin to use an appropriate encoding or locale.

#### Git

*	If using Gitweb, versions newer than 1.6 may not work correctly, as the Gitweb plugin is scraping HTML
	from the viewer, and changes to the HTML structure will break the Gitweb plugin.  The version of Gitweb
	in use on [MantisForge][] is known to work with the plugin.

*	Using Github with private organization repositories is not yet supported.  Private repositories for
	normal user accounts, however, *is* supported.  Enter the username and API key from any Github account
	with access to the repository, and it should import correctly.

*	Using branches other than "master" will require you to modify the individual repository configuration in
	Mantis to list any branches that you want to be imported.

[issue-93]: http://leetcode.net/mantis/view.php?id=93
[issue-130]: http://leetcode.net/mantis/view.php?id=130
[MantisForge]: http://git.mantisforge.org
