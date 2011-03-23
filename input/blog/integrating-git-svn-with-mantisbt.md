title: Integrating Git and SVN with the Mantis Bug Tracker
tags: git, github, mantisbt, plugins, source integration, svn
date: 2009-01-07
nocrumbs:
---
With the ongoing work towards a 1.2 release, the <a href="http://www.mantisbt.org">Mantis Bug Tracker</a> features a brand new plugin and event system, which will allow users to implement entirely new features for MantisBT without ever needing to touch any of the core codebase.  It's a very extensible system, and allows plugin authors to implement only what they need, while still allowing advanced plugins as much flexibility as possible.  Plugins can be as small as a single file with 20 lines of code, or as large as entire hierarchies of files, pages, with their own API's.

As the core developer of the new plugin system, I have been working on a variety of plugins. In particular, I have created a vastly improved method of integrating source control repositories within MantisBT.  The plugin package is named, aptly enough, Source Integration, and implements a generic framework that will allow integration with multiple repositories, each potentially using any source control systems available, simply by creating an extension plugin for each new tool.  Currently, I have implemented integration packages for both Git and Subversion, my two source control tools of choice.

The Source Integration package tracks repository information based on a series of changesets, each of which may have a list of affected files.  The data representation is generic enough to cover version control concepts used by all types of tools, from the ubiquitous CVS and Subversion, to modern distributed tools like Git and Hg.  However, the system takes the stance of implementing as few details as possible, so it relies on existing repository-viewing tools for tasks such as viewing commit diffs, file contents, tree browsing, etc.  Extension plugins handle translating tool-specific information, like history logs or checkin data, into the generalized data objects used by the framework.  Extensions also generate URL's for viewing files and diffs, but everything else is handled automatically by the core framework.

The true benefit of the Source Integration package lies in the amount of repository integration that it implements within MantisBT.  When importing changesets from your repository, Source looks at the commit message of each changeset for references to bug numbers in your tracker, and sets up links in the database for any bugs mentioned.  When viewing bugs mentioned in commit messages, a new section is displayed after the bugnotes called "Related Changesets", giving a list of linked changes, including information about the changeset, such as the branch, author, timestamp, and a list of changed files.

<!-- endexcerpt -->

Since a picture is worth a thousand words, and I'm not that great of a writer, few screenshots for your viewing pleasure:

<a href="http://leetcode.net/blog/files/2009/01/si-repos.png"><img src="http://leetcode.net/blog/files/2009/01/si-repos-300x59.png" alt="List of integrated repositories." width="300" height="59" class="size-medium wp-image-103" /></a>
<a href="http://leetcode.net/blog/files/2009/01/si-search.png"><img src="http://leetcode.net/blog/files/2009/01/si-search-300x171.png" alt="Search for imported changesets that match a set of filter criterion." width="300" height="171" class="size-medium wp-image-111" /></a>
<a href="http://leetcode.net/blog/files/2009/01/si-browse.png"><img src="http://leetcode.net/blog/files/2009/01/si-browse-300x80.png" alt="List of changesets for a repository or search result." width="300" height="80" class="size-medium wp-image-110" /></a>
<a href="http://leetcode.net/blog/files/2009/01/si-related.png"><img src="http://leetcode.net/blog/files/2009/01/si-related-300x68.png" alt="List of repository changesets attached to the current issue." width="300" height="68" class="size-medium wp-image-99" /></a>
<a href="http://leetcode.net/blog/files/2009/01/si-details.png"><img src="http://leetcode.net/blog/files/2009/01/si-details-300x93.png" alt="Detailed information about the selected changeset." width="300" height="93" class="size-medium wp-image-100" /></a>

<strong>Installation, Configuration, and Integration</strong>

So how do you get this source control goodness in your own MantisBT installation?  Well, first, you need to make sure you meet a few basic requirements:

<ul>
<li>a development snapshot of MantisBT version 1.2.x - either download a <a href="http://www.mantisbt.org/builds">nightly build</a>, or a snapshot from the <a href="http://git.mantisbt.org">MantisBT Gitweb</a> - the old 1.2.0a2 release tarball will not work.</li>

<li>to integrate Git, you need EITHER</li>
  <ul>
  <li>a public GitHub repository, OR</li>
  <li>a Gitweb installation (repo.or.cz works well)</li>
  </ul>

<li>to integrate Subversion, you need EITHER</li>
  <ul>
  <li>a public SourceForge repository, OR</li>
  <li>a WebSVN installation to view diffs and/or file contents</li>
  </ul>

</ul>

<em>Note that the Source Integration package relies on external viewers for Git integration, as it does yet support local repository access.</em>

Assuming that you meet the above requirements, you can begin the installation and integration process.  The latest version of the plugins can be found at the <a href="http://git.mantisforge.org">MantisForge Gitweb</a> by clicking on the 'snapshot' link next to each repository.

<ol>
<li>Install or upgrade to the latest Mantis 1.2.x (remember, the 1.2.0a2 release will not work)</li>
<li>Install the Meta plugin</li>
<li>Install the Source plugin</li>
<li>Install the appropriate Source extension plugin or plugins:</li>
  <ul>
  <li>SourceGithub for GitHub</li>
  <li>SourceGitweb for Gitweb and repo.or.cz</li>
  <li>SourceSFSVN for SourceForge</li>
  <li>SourceWebSVN for WebSVN</li>
  </ul>
<a href="http://leetcode.net/blog/files/2009/01/si-plugin.png"><img src="http://leetcode.net/blog/files/2009/01/si-plugin-300x143.png" alt="Installed plugins." width="300" height="143" class="size-medium wp-image-102" /></a>

<li>You'll now have a new link in your MantisBT menu, named "Repositories"; click on it now</li>
<a href="http://leetcode.net/blog/files/2009/01/si-repos.png"><img src="http://leetcode.net/blog/files/2009/01/si-repos-300x59.png" alt="List of integrated repositories." width="300" height="59" class="size-medium wp-image-103" /></a>

<li>Optional:  Click on the "Configuration" link to change the regular expressions used to match bug references in commit messages to match the style used in your project.  By default, it will match text like "issue #xxx" or "bugs #xxx, #yyy", etc. Note that the first regex finds groups of references, and the second regex matches the actual issue numbers.</li>
<a href="http://leetcode.net/blog/files/2009/01/si-regexes.png"><img src="http://leetcode.net/blog/files/2009/01/si-regexes-300x46.png" alt="Default regular expressions for extracting commit message bug references." width="300" height="46" class="size-medium wp-image-105" /></a>

<li>Fill in the "Create Repository" form, with an appropriate name, and selecting the appropriate repository type from the list of installed extensions</li>
<a href="http://leetcode.net/blog/files/2009/01/si-create.png"><img src="http://leetcode.net/blog/files/2009/01/si-create-300x80.png" alt="Form used to create a new repository integration." width="300" height="80" class="size-medium wp-image-106" /></a>

<li>You'll be taken to a second form with a new set of options based on the repository type you've chosen.  Fill in the appropriate information, and click "Update Repository" to save the information</li>
<a href="http://leetcode.net/blog/files/2009/01/si-update.png"><img src="http://leetcode.net/blog/files/2009/01/si-update-300x137.png" alt="Form for updating specific repository information." width="300" height="137" class="size-medium wp-image-107" /></a>

<li>You should be ready to begin the data import process.  Click "Import Latest Data" to begin.  <em>Note that for large repositories, you may need to repeat this step, due to limits or timeouts, until it has finished importing the entire repository.</em></li>

</ol>

At this point, you should have your repository imported and integrated with your MantisBT installation, but you still need to do some further effort to make sure MantisBT stays up to date with the latest changes from the repository:

<ul>
<li>For GitHub, enable remote checkins for address "65.74.0.0" to allow GitHub's servers access, and point your repository's post-receive URL to "http://yoururl.xyz/mantisbt/plugin.php?page=Source/checkin"</li>
<a href="http://leetcode.net/blog/files/2009/01/si-remote-checkin.png"><img src="http://leetcode.net/blog/files/2009/01/si-remote-checkin-300x75.png" alt="Configuring remote checkin options." width="300" height="75" class="size-medium wp-image-108" /></a>

<li>For Gitweb, SourceForge, or WebSVN integration, find your repository's ID, and setup a cronjob (or something equivalent) to run "curl http://yoururl.xyz/mantisbt/plugin.php?page=Source/repo_import_latest&amp;id=XX"</li>
<li>For WebSVN, you may optionally use the included post-commit hook found in the plugin directory.</li>
</ul>

So now you should be done setting up integration between your repository and MantisBT.  Congratulations!
