title: Integrating Source Control Tools with Mantis Bug Tracker
tags: bzr, cvs, hg, mantisbt, plugins, source integration
date: 2009-03-22
---
*Update: The information in this post is unfortunately out of date.  While much of the code samples are similar, the new method of creating new plugins has changed in subtle, but very significant ways.  Until a new guide can be written, please refer to the existing plugins for code examples.*

Considering that my last post on <a href="http://leetcode.net/blog/2009/01/integrating-git-svn-with-mantisbt/">Integrating Git and SVN</a> has garnered a fair amount of attention, I thought that it would be useful to discuss my Source Integration framework in more detail.  Specifically, I'll be covering topics such as the design and implementation of the framework and, more importantly, how developers can go about implementing support for other version control tools.

The point of this is to show that it's quite possible to integrate just about any type of version control tool with the Source Integration system; indeed I planned from the beginning to create a generalized framework that would support many different types and paradigms for version control.  This should at least be evident in that I have already created extension plugins for Git and Subversion - it should be quite possible to extend the concepts further to Mercurial, Bazaar, CVS, or any other tool.

For the point of brevity, I'll make the assumption that the developer at least has a fair understanding of PHP, their version control tool, and how events and plugins work in <a href="http://www.mantisbt.org">MantisBT</a>.  If you are not yet familiar with the plugin system, there is currently a basic introduction in the <a href="http://docs.mantisbt.org/master/en/developers/">MantisBT Developer's Guide</a>, which I'll hopefully be adding more information to in the near future.

<!-- endexcerpt -->

<em>Note: the following few sections dive into the concepts of how the framework was designed; for those just interested in creating extension plugins, skip to the <a href="#implementation">implementation</a> section.</em>

<strong>Design Decisions</strong>

I tried to approach the design of this system from the standpoint of both generality and simplicity; there are many source control topics that I have either brushed out of the way, or left up to the implementations of other existing projects.  The end goal was to have a flexible system that could support almost any type of tool currently available, while also abstracting (or delegating) away as much as possible to simplify the implementation.

The biggest part of the design that I chose to delegate away was the topic of viewing file contents and commit differences.  There are so many existing tools out there to handle those tasks within source control repositories, that I figured it was a waste of time to worry about.  This means that my system relies on external viewing applications for any repositories in use; for Git, there's <a href="http://github.com">GitHub</a> and <a href="http://git.or.cz/gitwiki/Gitweb">Gitweb</a> support, and <a href="http://websvn.tigris.org/">WebSVN</a> or <a href="http://www.sourceforge.net">SourceForge</a> for Subversion.

Another design abstraction that I decided upon was the handling of tool-specific details, such as how changesets are labelled, or how branches and other such topics are implemented.  I chose to store as neutral a data model as possible, and delegate any display (or interpretation) of the data to the appropriate extension plugins.  For instance, this allows SVN plugins to prepend the standard 'r' in front of revision numbers (such as "r123"), while Git plugins can crop the changeset hash at eight characters for easier user consumption.

The resulting design utilizes the <a href="http://en.wikipedia.org/wiki/Inversion_of_control">Inversion of Control</a> concept to create a "framework" that requires as little tool-specific implementations as possible.  The framework does much of the heavy lifting with integrating the data into MantisBT, and delegates only the tasks to extension plugins that require detailed information about the source control tool being integrated.

Much of this design is a direct extension of the plugin system in MantisBT, which I also created using Inversion of Control, and uses its own set of events to handle the delegation of tasks wherever necessary.  This allows anyone to create an extension plugin that hooks into this framework and implement the integration for any source control tool, without needing to know much about how the framework integrates within MantisBT.

<strong>Data Modelling</strong>

For the actual data modelling, I decided upon three major data structures, and one ancillary structure.  Each structure is given a simple object-oriented API to work with.

The root of the data model is the <em>Repository</em> object, which contains information on the source control repository itself, such as its name, access URL, and "type".  The type is basically a mapping to a specific extension plugin that knows how to retrieve, store, and interpret the data appropriately; examples of the type include "github" provided by the SourceGitHub plugin, and "websvn" provided by the SourceWebSVN plugin.  Each repository also contains a dictionary of arbitrary information that can be used as storage for any tool-specific data; for the GitHub integration, this extra information includes the GitHub user containing the project repository.

Each repository contains a set of <em>Changeset</em> objects, which naturally contains data for each changeset in the repository history.  Each changeset can have a revision string, a branch name, author information, timestamp, commit message, and a parent revision string.  Most of this is completely optional, meant only for use with tools that support that type of data.  For instance, the changeset revision has no meaning when used with a tool like CVS or SCCS, which only tracks revisions at the file level.  

Note that I also decided, for the sake of simplicity, to only track a single parent revision for each changeset, even though some tools may have multiple parents for some changesets (such as merge commits in Git).  This does throw away a small bit of data, but was done for the sake of maintaining a more simplistic data structure.  Give me a good enough argument, and maybe I'll change my mind.  ;)

For each changeset, there may be a set of <em>File</em> objects; these represent any files that have been added, modified, or removed from the repository in that changeset (or potentially any other action you can imagine).  These objects track the filename and/or path, the action, and also track a separate revision string from the changeset object.  This specifically enables usage with source control tools such as CVS that track file revisions.  Note that this object does *not* contain any other information about the file, such as the content or diff, as per my initial decision to keep things simple; the repository itself keeps this information, and for the most part, it's unnecessary information for a bugtracker to handle.

Lastly, we come to the one ancillary data model, but arguably the one that is most important to the whole point of this framework.  For each changeset, there is a set of <em>Bug</em> relationships, that only exist to tie source control changesets to issues in the bugtracker.  It also the simplest data in the system, consisting of just a bug ID.

Roughly following the data models described above, are a set of classes defined in Source.API.php (<em>SourceRepo</em>, <em>SourceChangeset</em>, and <em>SourceFile</em>) which contain a set of public variables for the primary data, and static or public methods for simplifying the process of loading, saving, and manipulating groups of objects.  It should be rather straightforward to pick it up based on the information above and the comments in the code (IMHO).

<strong>Framework Events</strong>

Utilizing the event-based plugin system, the source control integration defines a set of events that delegate tool-specific tasks to appropriate extension plugins, such as viewing changeset information and gathering changeset data from the source control tool itself.

The first event is <em>GET_TYPES</em>, which allows extension plugins to "register" themselves with the integration framework, so that it knows what repository types are supported.  

The next set delegates the display of certain information: <em>SHOW_TYPE</em> covers the output of an extension plugin's repository type, <em>SHOW_CHANGESET</em> allows manipulation of the changeset string, including how the branch and revision information is displayed, and <em>SHOW_FILE</em> allows the plugin to modify how files associated with a changeset are displayed, including action and revision information.

Another set delegates the URL links for data when displayed: <em>URL_REPO</em> for the URL to the main page of the repository browser, <em>URL_CHANGESET</em> for a link to a page in the browser for changeset, <em>URL_FILE</em> for a link to the entire contents of files in a given changeset, and <em>URL_FILE_DIFF</em> for a link to the diff output of files from a given changeset.

To handle repository type-specific data, two events allow extension plugins to hook their own form elements: <em>UPDATE_REPO_FORM</em> for displaying the form elements, and <em>UPDATE_REPO</em> for retrieving the form data and storing it in the repository object.

The last set of events allow extension plugins to gather data from the repository itself and create data objects and return them to the system: <em>PRECOMMIT</em> to analyze the incoming data from a repository's post-commit hook to determine what repository type the data is for, <em>COMMIT</em> to interpret the data and generate objects for an incoming group of changesets, <em>IMPORT_LATEST</em> to pull the latest data from the repository without requiring a post-commit hook, and <em>IMPORT_FULL</em> to wipe and completely re-import changeset data from the repository.

<a name="implementation"></a><strong>Implementing an Extension Plugin</strong>

So how does this design come together when creating an extension plugin to integrate a new source control tool?  Well, it's actually not that complicated; most of the design I discussed in the above sections helps make this portion of the process much simpler and easier to implement.  It even goes so far as to give you an initial head start when creating a new extension plugin, with an abstract class to inherit from with most of the plumbing already taken care of for you.

I'm going to cover a lot of this topic using a fake version control tool ("Open Sauce") as an example; for almost everything, you'll need to substitute code specific to the tool you're integrating with Mantis.  You may also be interested in reading through the <a href="http://git.mantisforge.org/w/source-integration.git?a=blob;f=SourceGithub/SourceGithub.php;h=c10d4f56fe96ffbef8965697dd8236a2420443a5;hb=HEAD">SourceGithub</a> and <a href="http://git.mantisforge.org/w/source-integration.git?a=blob;f=SourceWebSVN/SourceWebSVN.php;h=3f1818d0621d4271048aad98ab59be1c74cee0f2;hb=HEAD">SourceWebSVN</a> plugins as "real world" examples.  Onwards.

Naturally, your extension plugin will still need to be a valid Mantis plugin, so let's start there.  You'll need to create a new plugin (see the <a href="http://docs.mantisbt.org/master/en/developers/">MantisBT documentation</a> for this), and the plugin will need to extend the <a href="http://git.mantisforge.org/w/source-integration.git?a=blob;f=Source/MantisSourcePlugin.class.php;h=950ffb086b2f8fb08d4c15e0a0b622c152fe9e6b;hb=HEAD">MantisSourcePlugin</a> class, which is what provides you with the plumbing I mentioned above, such as hooking the framework events, and defining an abstract API for you to implement.  For a rough example of the base plugin declaration:

    &lt;?php
    class SourceOpenSauce extends MantisSourcePlugin {
      function register() {
        $this-&gt;name = 'Open Sauce Integration';
        $this-&gt;version = 'One Point Oh';

        $this-&gt;requires = array(
          'MantisCore' =&gt; '1.2.0',
          'Source' =&gt; '0.13',
        );
      }
    }

So that's a decent start, but now we'll need to start filling in all the pieces of the MantisSourcePlugin interface.  The interface methods each map to an event defined by the main Source Integration framework, and allow your plugin to take control whenever tool-specific details are needed.

<strong>Note: for most of these methods, you will need to check that the repository "type" is the one your plugin has registered, so that it does not try to handle the wrong repositories.</strong>

Let's register our repository type and tell the framework how to display it; this could benefit from using internationalized language strings, but that's beyond the topic scope:

    function get_types( $p_event ) {
      return array( 'opensauce' =&gt; 'Open Sauce' );
    }

    function show_type( $p_event, $p_type ) {
      if ( $p_type == 'opensauce' ) {
        return 'Open Sauce';
      }
    }

So now we can tell the framework how we want changesets and file entries to be displayed; for the purpose of example, we'll assume that both changesets and files have revision numbers:

    function show_changeset( $p_event, $p_repo, $p_changeset ) {
      if ( $p_repo-&gt;type != 'opensauce' ) {
        return;
      }

      return "$p_changeset-&gt;branch #$p_changeset-&gt;revision";
    }

    function show_file( $p_event, $p_repo, $p_changeset, $p_file ) {
      if ( $p_repo-&gt;type != 'opensauce' ) {
        return;
      }

      return "$p_file-&gt;action - $p_file-&gt;filename #$p_changeset-&gt;revision";
    }

Next up is defining how source control data links to the made-up "Open Sauce Webview" application.  Note that we are getting the viewer's base URL from the repo object, which we'll cover later:

    function url_repo( $p_event, $p_repo, $p_changeset=null ) {
      if ( $p_repo-&gt;type != 'opensauce' ) {
        return;
      }

      $t_url = $p_repo-&gt;info['viewer_url'];

      if ( !is_null( $p_changeset ) ) {
        $t_rev = $p_changeset-&gt;revision;
      } else {
        $t_rev = false;
      }

      return ( $t_rev ? "$t_url/view/$t_rev" : "$t_url/view" );
    }

    function url_changeset( $p_event, $p_repo, $p_changeset ) {
      ...
    }
    function url_file( $p_event, $p_repo, $p_changeset, $p_file ) {
      ...
    }
    function url_diff( $p_event, $p_repo, $p_changeset, $p_file ) {
      ...
    }

Next up is hooking some form elements onto the repository management page, so that the MantisBT administrator can set the base URL for the "Open Sauce Webviewer":

    function update_repo_form( $p_event, $p_repo ) {
      if ( $p_repo-&gt;type != 'opensauce' ) {
        return;
      }

      $t_url = $p_repo-&gt;['viewer_url'];

      echo '&lt;tr ', helper_alternate_class(), '&gt;&lt;td class="category"&gt;',
        'Open Sauce Viewer URL&lt;/td&gt;&lt;td&gt;',
        '&lt;input name="viewer_url" value="',
        string_attribute( $t_url ), '"/&gt;&lt;/td&gt;&lt;/tr&gt;';
    }

    function update_repo( $p_event, $p_repo ) {
      if ( $p_repo-&gt;type != 'opensauce' ) {
        return;
      }

      $p_repo-&gt;info['viewer_url'] = gpc_get_string( 'viewer_url', '' );

      return $p_repo;
    }

The last piece of the puzzle is the biggest: gathering commit data from the repository and converting it into the generalized data structures provided by the framework.  Here, we'll only cover a skeleton of importing the latest commits; you'll need to extrapolate on your own to cover the other methods of bringing in data:

    function import_latest( $p_event, $p_repo ) {
      if ( $p_repo-&gt;type != 'opensauce' ) {
        return;
      }

      # randomly make a query to get the latest commit data; our fake
      # viewer "returns" a JSON-encoded payload with commit info...
      $t_data = json_url( $p_repo-&gt;info['viewer_url'] . '/latest' );

      # prepare to aggregate the data
      $t_changesets = array();

      # go through all the changesets
      foreach( $t_data-&gt;commits as $t_commit ) {
        $t_changeset = new SourceChangeset(
          $p_repo-&gt;id,
          $t_commit-&gt;revision,
          $t_commit-&gt;branch,
          $t_commit-&gt;timestamp,
          $t_commit-&gt;author,
          $t_commit-&gt;message
        );

        # go through all the changeset's files
        foreach( $t_commit-&gt;files as $t_file ) {
          $t_file = new SourceFile(
            0, #no changeset id yet
            $t_file-&gt;revision,
            $t_file-&gt;filename,
            $t_file-&gt;action
          );

          #attach the file to the changeset
          $t_changeset-&gt;files[] = $t_file;
        }

        # parse any referenced bugs from the commit message
        $t_changeset-&gt;bugs = Source_Parse_Buglinks( $t_changeset-&gt;message );
        $t_changeset-&gt;save();

        # keep track of all the changesets imported
        $t_changesets[] = $t_changeset;
      }

      # return the set of changesets imported
      return $t_changesets;
    }

<strong>Wrap It Up</strong>

At this point, we now have a basic extension plugin that can pull data from the source control tool and interact with the framework to display the data appropriately.  You should now be able to take this to the next level, and create an integration plugin for any source control tool you can imagine.  I'd personally love to see support for Mercurial and Bazaar in the near future.

And here's the kicker: if you are willing to release your integration plugin under an open source license (such as BSD or GPL), I'll gladly include it in my main <a href="http://git.mantisforge.org/w/source-integration.git">source-integration.git</a> repository along with the framework, as I do for the existing Git and SVN plugins.  You'll benefit from any community bug fixes and feature updates, and the community will benefit from having all the plugins in a single location, easy to find and install.  I'll even give you developer access to the repository on MantisForge.org in case you need to update it in the future.

Cheers, and happy integrating!
