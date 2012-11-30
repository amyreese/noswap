title: Source Integration API Keys
description: The Source Integration framework now supports use of API keys to authorize incoming changeset data.
tags: mantisbt, source integration, github
date: 2011-06-06
---
Today marks an incremental release to the Source Integration plugin framework for MantisBT, now at version
0.16.3.  This marks the introduction of support for using an API key to authorize inbound changeset data
from repository data sources.  It is initially supported for integration with Github, where large array of
servers made it all but impossible to whitelist allowed IPs for remote commit data.

Future plans for the feature include support for configuring multiple API keys simultaneously, as well as
adding support for using the API keys from other data sources, such as SVN or Gitweb repositories.
Additionally, the old options for listing allowed IP addresses is now considered deprecated, and will likely
be removed entirely at the next major release.

To set up an API key in your MantisBT instance, visit the Repository Configuration page, where you will find
a new option labelled, strangely enough, "API Key".  You will need to generate your own key; the best way to
do this is on a machine with OpenSSL by running the following command to create a secure, random string of
hexadecimal digits, and then copying the resulting string to MantisBT:

    $ openssl rand -hex 12

Once this is done, you can enable this on your Github projects by visiting the Service Hooks admin page for
your repositories, activating the MantisBT hook, and copying the same key string into the "Api Key" field
there.  Any future pushes to your Github repo should send data to your MantisBT install using the API key to
authorize the data submission.
