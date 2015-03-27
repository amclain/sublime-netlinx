Build Commands
==============
*NOTE: Build support requires the [NetLinx Compile](https://github.com/amclain/netlinx-compile)
utility to be installed, as well as the NetLinx compiler provided by AMX.*


Build: Build
------------
Same as *Build: Workspace*
Hotkey: Ctrl + B


Build: Source
-------------
Builds the active source code file. Automatically scans for include and module
files.


Build: Workspace
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


Build: Run
----------
Future
