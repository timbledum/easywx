# easywx #

## A library for easy function-based pop-up gui prompts based on the easygui API ##

Classic gui frameworks are fairly intimidating for new users, as they require
a fairly good understanding of class structures. Easywx lowers the barriers to
entry by:

1. Using native gui elements that are portable and look professional
2. Providing solid defaults for window formatting and labels, including
   generous spacing
3. Allowing gui prompts to be called via easy to use functions.
   Typically gui frameworks require you to construct a class system then call
   a loop – this cuts through all of that tedious set-up work


### Example usage
```python
>>> import easywx

>>> easywx.buttonbox('Which music is the best?', 'Best music', ('Reggae', 'Funk', 'Dubstep'))
'Reggae'
```


### History ###

This library aims to replicate the API of easygui. [Easygui][1] is a great library,
but looks dated and uses tkinter.

Wxpython has emerged as one of the leading python gui frameworks with the
phoenix project bring it up to python 3. Wxpython also uses native widgets
which provides a smooth polished feel.

[1]: http://easygui.readthedocs.io
