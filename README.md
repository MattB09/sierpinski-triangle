# sierpinski-triangle
A visualization of how the Sierpinski Triangle emerges when following an algorithm of placing a random dot within a triangle, choosing a random corner of the triangle and then placing a dot halfway between those points. Then choose another random corner and place a dot in between the new dot and that corner. Repeat.

Run with Python3.11

`python main.py`

No dependencies. However, the python version must be setup with TKinter support. If not, the program cannot be run as an error will occur.

If you get an error indicating tkinter is not installed, you can follow these steps.

macOS:
```bash
# Install Tkinter using Homebrew
brew install tk

# Set the TK_LIBRARY environment variable
export TK_LIBRARY="/usr/local/opt/tcl-tk/lib/tk8.6"

# Reinstall Python with Tkinter support
pyenv uninstall 3.11.0
pyenv install 3.11.0
```

## Preview
![sierpinsky-triangle](https://github.com/MattB09/sierpinski-triangle/assets/29540686/bc1bf281-6453-4abb-baf0-c4b317f0c8be)
