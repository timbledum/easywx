# easywx #

## *A library for easy function-based pop-up gui prompts based on the
easygui API* ##

This library aims to replicate the API of easygui. Easygui is a great library,
but looks dated and uses tkinter.

Wxpython has emerged as one of the leading python gui frameworks with the
phoenix project bring it up to python 3. Wxpython also uses native widgets
which provides a smooth polished feel.

Classic gui frameworks are fairly intimidating for new users, as they require
a fairly good understanding of class structures. Easywx lowers the barriers to
entry by:

1. Providing solid defaults for window formatting and labels
2. Allowing gui prompts to be called via functions rather than constructing a
   class then calling the loop
