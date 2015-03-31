Build Commands
==============
*NOTE: Build support requires the [NetLinx Compile](https://github.com/amclain/netlinx-compile)
utility to be installed, as well as the NetLinx compiler provided by AMX.*

The NetLinx build system can be changed between the variants listed below by
using `ctrl + shift + b`, which can be helpful for switching between compiling
all systems in the workspace, or only the active system. As of Sublime Text 3
build 3080 the last build system selected will be remembered when using
`ctrl + b`. See the [build systems post](http://www.sublimetext.com/forum/viewtopic.php?f=2&t=17471)
for more details.


Build: Build
------------
Same as *Build: Workspace*
Hotkey: Ctrl + B


Build: Source
-------------
Builds the active source code file. Automatically scans for include and module
files.


Build: Workspace - All Systems
----------------
Searches for a workspace file containing the source code file that you ran build
on and compiles the workspace. It starts looking for a workspace in the current
working directory and traverses upwards through parent directories until one is
found. If no matching workspace is found, the active source code file will be
compiled as if *Build: Source* was executed.

Note: [NetLinx Compile](https://github.com/amclain/netlinx-compile), which this
command utilizes, is smart enough to check inside of NetLinx Studio workspace
(.apw) files for the active source code file before invoking the compiler. It
will not pick the first .apw file that it sees; however, this is not an excuse
for reckless organization of project files. This also means includes and modules
can be nested in subdirectories of the project as long as their paths in the
workspace file are accurate.


Build: Workspace - Active System
----------------
Like `Build: Workspace - All Systems`, but only builds the active system.


Build: Run
----------
Future
