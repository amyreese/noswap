title: PHP Bugs Me, or Where Type Coercion Causes Bugs
description: News flash: type coercion in PHP can cause unexpected and buggy behavior.  Gasp!
date: 2010-03-02
tags: facepalm, mantisbt, php
nocrumbs:
---
I really like PHP as a technology, both for its extensibility and its deployment
style. I think it is the quickest and most straightforward platform to create
web applications with, and frameworks like [CodeIgniter](http://codeigniter.com/)
make it even better.

I've long been on the fence regarding PHP's type coercion and comparison issues,
but a [recent bug][php-type-1] in [Mantis Bug Tracker][php-type-2] has made me
/facepalm for the first time in my long history of working with PHP:

> When I click on "Edit" next to 1.2, mantis shows me the 1.20 properties.
> When I click 1.1 it shows me 1.10!

The offending snippet of code:

	foreach( $g_cache_versions as $t_version ) {
	   if ( ( $t_version['version'] == $p_version )
		  && ( $t_version['project_id'] == $c_project_id ) ) {
		  return $t_version['id'];
	   }
	}

At first glance, it seems perfectly normal... and then you read the commit log,
emphasis mine:

> This is due to an incorrect version name comparison in version_get_id whereby
the following check between strings was occurring:
>
> <code>if( "1.1" == "1.10" ) { ... }</code>
>
> PHP evaluates this expression to true *because 1.1 and 1.10 are treated as
floats*. We however need to preserve the string type during this comparison,
thus we need to use the === comparison operator instead.

I thought I'd seen it all...

[php-type-1]: http://www.mantisbt.org/bugs/view.php?id=11571
[php-type-2]: http://www.mantisbt.org
