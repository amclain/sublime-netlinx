Sublime Text AMX NetLinx Plugin
===============================
sublime-netlinx

[![MIT License](https://img.shields.io/badge/license-MIT-yellowgreen.svg)](https://github.com/amclain/sublime-netlinx/blob/master/license.txt)

This is a plugin for developers looking for a lighter weight alternative to
NetLinx Studio, while still providing powerful functionality. On top of the
features provided by [Sublime Text](http://www.sublimetext.com/), this plugin
adds syntax highlighting, color schemes, and build support for the AMX NetLinx
programming language. This is also a great option for programmers who are
looking to use one editor for multiple languages.

***Designed for [Sublime Text 3](http://www.sublimetext.com/3)***


Installation
------------
1. Install [Sublime Package Control](https://packagecontrol.io/installation)
1. Open the `Command Palette` (Ctrl + Shift + P)
1. Select `Package Control: Install Package`
1. Select `NetLinx`

**NetLinx Classic Color Scheme**

Sublime will use the editor's global color scheme by default. If you would like
the files to look the way they do in NetLinx Studio, the sublime-netlinx package
comes with a classic NetLinx color scheme.

* [Enable NetLinx Classic Color Scheme](docs/enable_netlinx_classic_color_scheme.md)

**Build Support**

Build support requires the [NetLinx Compile](https://github.com/amclain/netlinx-compile)
utility to be installed, as well as the NetLinx compiler provided by AMX. The
AMX NetLinx compiler is bundled with [NetLinx Studio](http://www.amx.com/techcenter/applications.asp?Category=Development%20Tools#NetLinx%20Studio).

**File Transfer**

File transfer is handled by [FileTransfer 2](http://www.amx.com/techcenter/applications.asp?Category=Development%20Tools#FileTransfer%202),
provided by AMX via the Web Update utility or as a download from the prior link.


Issues, Bugs, Feature Requests
------------------------------
Any bugs and feature requests should be reported on the GitHub issue tracker:

https://github.com/amclain/sublime-netlinx/issues


**Pull requests are preferred via GitHub.**

Mercurial users can use [Hg-Git](http://hg-git.github.io/) to interact with
GitHub repositories.


Transitioning From NetLinx Studio
---------------------------------

It is important to understand that sublime-netlinx is an alternative way to
work with NetLinx files, not a feature-for-feature clone of NetLinx Studio.
Therefore, sublime-netlinx requires a different way of thinking than what
you may be used to. If you typically work with multiple programming lanugages,
transitioning to sublime-netlinx will probably be easy and increase your
productivity. If NetLinx is your only programming language, the transition may
be more difficult. If you've spent a reasonable amount of time with
sublime-netlinx and find yourself frustrated, sublime-netlinx may not be right
for you. That's ok.


Setting Up A Workspace
----------------------
The easiest way to maintain a NetLinx workspace with Sublime Text is by
[using a netlinx-workspace workspace.config.yaml file](https://github.com/amclain/netlinx-workspace#yaml-workspace-configuration).
This file can be created by hand, by running `netlinx-workspace --create`, or by
using a framework like [netlinx-erb](https://github.com/amclain/netlinx-erb#netlinx-erb)
that handles all aspects of developing and maintaining a NetLinx project.

> Ideally a project using a workspace.config.yaml file will be able to be
compiled with a standard Sublime build task (ctrl + b). However, the
[extension discovery system issue](https://github.com/amclain/netlinx-compile/issues/9)
needs to be resolved before this works. In the mean time, a NetLinx Studio .apw
file can be generated from the command palette with
`NetLinx: Generate .apw From workspace.config.yaml`. The netlinx-erb framework
isn't affected by this problem, as it uses its own set of automated tasks.

* [Alternate Method Using NetLinx Studio](docs/setting_up_a_workspace_with_netlinx_studio.md)


Command Reference
-----------------
This plugin provides commands that are accessible from the Sublime Text Command
Palette (`Tools` -> `Command Palette`) (Ctrl + Shift + P).

* [Build: Build](docs/build.md) (Ctrl + B) - Same as *Build: Workspace*
* [Build: Source](docs/build.md)
* [Build: Workspace - All Systems](docs/build.md)
* [Build: Workspace - Active System](docs/build.md)
* [Build: Run](docs/build.md) (Future)
* [NetLinx: Fix Indentation](docs/fix_indentation.md)
* [NetLinx: New From Template: Standard](docs/new_from_template.md)
* [NetLinx: New From Template: Include](docs/new_from_template.md)
* [NetLinx: New From Template: Test Suite](docs/new_from_template.md)
* [NetLinx: New From Template: Overview](docs/new_from_template.md)
* NetLinx: Launch File Transfer
* NetLinx: Launch NetLinx Diagnostics


Snippets
--------
All of the code snippets available for auto-completion can be found under the menu:

`Tools` -> `Snippets...`


Helpful Sublime Plugins
-----------------------
* [Abacus](https://github.com/khiltd/Abacus) - Text alignment.
* [All Autocomplete](https://github.com/alienhard/SublimeAllAutocomplete) -
Extends the default autocomplete to find matches in all open files.
* [HexViewer](https://github.com/facelessuser/HexViewer) - Hex viewer/editor.
* [Text Pastry](https://github.com/duydao/Text-Pastry) - Insert number/text sequences.
* [Vintage](http://www.sublimetext.com/docs/3/vintage.html) - Enable Vim hotkeys.
