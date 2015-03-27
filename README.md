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


Setting Up A Workspace
----------------------
*Workspace creation will be a little clumsy until this functionality is added
to [netlinx-workspace](https://github.com/amclain/netlinx-workspace).*

1) Open NetLinx Studio and go through the `Workspace Wizard`. When it comes
to the `Master Source Code File Selection` screen, choose `Add the Master Source
Code File later`.

2) Add the project folder to Sublime Text: `Project` -> `Add Folder to Project...`

3) Select `NetLinx: New From Template: Overview` from the Command Palette
(ctrl + shift + p) or `Tools` -> `Command Palette`.

4) Fill in the header and program name, then save the .axs file. This file will
contain includes to device and touch panel files, but typically shouldn't do
any of the heavy lifting itself.

5) Create a folder named `include`. This is where the device and touch panel
code will reside. Breaking up functionality into different files makes it easier
to maintain a complex system, as well as reuse those components in other systems.

6) Select `NetLinx: New From Template: Include`, fill in the header for one of
the devices (touch panel, for example), change the include guard
(`#if_not_defined`) to a project-unique name, and save the file in the `include`
folder. Code does not need to be written yet.

7) Repeat step 6, adding an include file for each logical component of the
system. Subfolders may be necessary for complex projects.

8) Add the appropriate `#include` declarations to the .axs source code file.

9) In NetLinx Studio, add the .axs file as an existing source file and set it to
`Master File`. Add the .axi include files as existing include files.

10) Press `Build Active System` as a sanity check to make sure the workspace
is set up correctly. Since no source code has been written at this point,
any errors will be problems with files that haven't been included correctly.
Fix the errors, if any.

11) Close NetLinx Studio. At this point the source code can be written in
Sublime Text.

12) With the .axs or include file open in Sublime Text, build the file
(ctrl + b) or `Tools` -> `Build`.

13) The project should compile. If it doesn't, verify the installation of
Ruby and [netlinx-compile](https://github.com/amclain/netlinx-compile).

14) Begin programming.


Command Reference
-----------------
This plugin provides commands that are accessible from the Sublime Text Command
Palette (`Tools` -> `Command Palette`) (Ctrl + Shift + P).

* [Build: Build](docs/build.md) (Ctrl + B) - Same as *Build: Workspace*
* [Build: Source](docs/build.md)
* [Build: Workspace](docs/build.md)
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
