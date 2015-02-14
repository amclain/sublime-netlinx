# Sublime Text AMX NetLinx Plugin

sublime-netlinx

This is a plugin for developers looking for a lighter weight alternative to
NetLinx Studio, while still providing powerful functionality. On top of the
features provided by [Sublime Text](http://www.sublimetext.com/), this plugin
adds syntax highlighting, color schemes, and build support for the AMX NetLinx
programming language. This is also a great option for programmers who are
looking to use one editor for multiple languages.

***Designed for [Sublime Text 3](http://www.sublimetext.com/3)***


## Documentation

[https://sourceforge.net/p/sublime-netlinx/wiki/Home/](https://sourceforge.net/p/sublime-netlinx/wiki/Home/)


## Setting Up A Workspace

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
