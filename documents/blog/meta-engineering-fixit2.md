title: "Fixit 2: Meta’s next-generation auto-fixing linter"
link: https://engineering.fb.com/2023/08/07/developer-tools/fixit-2-linter-meta/
date: 2023-08-07
tags: python, me
---

Let's talk about my newest open source project, built as part of my effort
to improve the linting ecosystem at Meta:

> This year, we have been building a new linter, Fixit 2, designed from the
ground up to make developers more efficient and capable, both in open source
projects and the diverse landscape of our internal monorepo. At Meta, we are
using Fixit 2 with a few early adopters, and plan to roll it out to the rest
of our monorepo soon. But any developer can use it to perform auto-fixing more
efficiently and make faster improvements to their own codebases.

Something I don't get to talk about enough is just how much I truly appreciate
the ability to spend my time at Meta solving problems with open source, and
that I can share my work with the rest of the world. Fixit is the third
open source project that I've had the privilege of releasing at Meta, and I
believe Fixit makes it easier than ever before to build new lint rules for
Python, a powerful tool for any Python team.

> Writing a new lint rule can be done with less than a dozen lines of code,
and test cases are defined inline. You can even place it right next to the
code that it will be linting:

>   ```
    # teambread/rules/hollywood.py
    import fixit
    import libcst
    class HollywoodName(fixit.LintRule):
        VALID = [...] # no lint errors here
        INVALID = [...] # bad code samples here
        def visit_SimpleString(self, node: libcst.SimpleString):
            if node.value in ('"Paul"', "'Paul'"):
                self.report(node, "It's underbaked!")
    ```

Unlike other new linters on the market, Fixit is uniquely focused on reducing
the barriers to writing high quality, auto-fixing lint rules in pure Python,
without needing to learn Rust or any other language. Having auto-fixes is also
key:

> When running Fixit 2 with auto-fixing lint rules, any code that triggers the
lint rule is an opportunity to get an automatic replacement, improving th
codebase with less effort from the developer. Applied more broadly, Fixit 2
can even be used as a tool to enact sweeping codemods against a large codebase
while leaving a lint rule in place to handle any matching code in the future.

Fixit 2 is already available [on PyPI](https://pypi.org/project/fixit/).
You can `pip install fixit` and start using it with zero configuration.

> We have a [roadmap][] with plans for future improvements and features, and a
rich set of [documentation and user guides][docs] to help you get started with
Fixit 2 in your own projects or repositories.

[roadmap]: https://github.com/Instagram/Fixit/milestones
[docs]: https://fixit.rtfd.io/en/latest/
