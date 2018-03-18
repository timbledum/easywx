import types

import wx
from .button_window import ButtonWindow
from .settings import Settings


def buttonbox(msg='',
              title='',
              choices=('Button[1]', 'Button[2]', 'Button[3]'),
              images=None):

    return choices[indexbox(**locals())]


def indexbox(**kwargs):
    settings = Settings(**kwargs)
    app = wx.App()
    frame = ButtonWindow(settings)
    app.MainLoop()
    return frame.result


def ynbox(choices=['Yes', 'No'],
          msg='Shall I continue?',
          title=''):

    return indexbox(**locals())


def ccbox(choices=['C[o]ntinue', 'C[a]ncel'],
          msg='Shall I continue?',
          title=''):

    return indexbox(**locals())


button_boxes = [func for func in globals().values() if
                isinstance(func, types.FunctionType)]
