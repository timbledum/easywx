import types

import wx
from .button_window import ButtonWindow
from .settings import Settings




def indexbox(msg="Shall I continue?", title="", choices=("Yes", "No"), images=None):

    settings = Settings()

    app = wx.App()
    frame = ButtonWindow(
        msg=msg, title=title, choices=choices, images=images, settings=settings
    )
    app.MainLoop()
    return frame.result


def buttonbox(
    msg="", title="", choices=("Button[1]", "Button[2]", "Button[3]"), images=None
):

    return choices[indexbox(**locals())]


def ynbox(msg="Shall I continue?", title="", choices=["Yes", "No"]):

    return indexbox(**locals())


def ccbox(msg="Shall I continue?", title="", choices=["C[o]ntinue", "C[a]ncel"]):

    return indexbox(**locals())


def boolbox(msg="Shall I continue?", title="", choices=("[Y]es", "[N]o"), images=None):

    return indexbox(**locals()) == 0  # should also return True if cancelled


def msgbox(
    msg="(Your message goes here)", title=" ", ok_button="OK", image=None, root=None
):

    indexbox(msg=msg, title=title, choices=(ok_button,), images=image)
    return ok_button


FUNCS = [indexbox, buttonbox, ynbox, ccbox, boolbox, msgbox]

if __name__ == "__main__":

    button_boxes = [
        func for func in globals().values() if isinstance(func, types.FunctionType)
    ]
    for func in button_boxes:
        func()
