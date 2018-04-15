import wx
from .choice_window import ChoiceWindow
from .settings import Settings


def textbox(
    msg="", title=" ", text="", codebox=False, callback=None, run=True
):
    pass


def integerbox(
    msg="",
    title=" ",
    default=None,
    lowerbound=0,
    upperbound=99,
    images=None,
    root=None,
):
    pass


def multenterbox(
    msg="Fill in values for the fields.",
    title=" ",
    fields=[],
    values=[],
    callback=None,
    run=True,
):
    pass


def enterbox(
    msg="Enter something.",
    title=" ",
    default="",
    strip=True,
    image=None,
    root=None,
):
    pass


def exceptionbox(msg=None, title=None):
    pass


def choicebox(
    msg="Pick an item",
    title="",
    choices=['Option1', 'Option2', 'Option3'],
    preselect=0,
    callback=None,
    run=True,
):
        settings = Settings()

        app = wx.App()
        frame = ChoiceWindow(msg=msg, title=title, choices=choices,
                             settings=settings, multiple=False)
        app.MainLoop()

        return frame.result[0] if frame.result else None


def codebox(msg="", title=" ", text=""):
    pass


def passwordbox(
    msg="Enter your password.", title=" ", default="", image=None, root=None
):
    pass


def multpasswordbox(
    msg="Fill in values for the fields.",
    title=" ",
    fields=(),
    values=(),
    callback=None,
    run=True,
):
    pass


def multchoicebox(
    msg="Pick an item",
    title="",
    choices=[],
    preselect=0,
    callback=None,
    run=True,
):
        settings = Settings()

        app = wx.App()
        frame = ChoiceWindow(msg=msg, title=title, choices=choices,
                             settings=settings, multiple=True)
        app.MainLoop()
        return frame.result
