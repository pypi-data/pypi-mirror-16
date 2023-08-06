default semantics for install.extra_path cause all installed modules to go
into a directory whose name is equal to the contents of the .pth file.

All that was necessary was to remove that one behavior to get what you'd
generally want.


