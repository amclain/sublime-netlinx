NetLinx: Fix Indentation
========================
*This process will convert tabs to spaces, which is fully compatible for viewing
in NetLinx Studio.*

NetLinx Studio uses a mix of tabs and spaces for whitespace by default, which
can make NetLinx source code files look terrible in other text editors. If you
are opening a file created in NetLinx Studio, or otherwise notice that the line
indentation does not look correct, run the `NetLinx: Fix Indentation` command
from the Sublime Text command palette (Ctrl + Shift + P).

If a NetLinx programmer used a nonstandard tab width, this command probably
won't work. In that case, you will have to try selecting various tab widths in
Sublime Text and running the `Indentation: Convert To Spaces` command. If all
tabs are correctly converted to spaces and there are still indentation problems,
try `Indentation: Reindent Lines`.
