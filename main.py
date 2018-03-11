import wx
import button_window
from settings import Settings


def buttons(**kwargs):
    settings = Settings(**kwargs)
    app = wx.App()
    frame = button_window.ButtonWindow(settings)
    app.MainLoop()
    return frame.result


def yes_no(button_input=['Yes', 'No'],
           message='Would you like to continue?',
           title='Proceed?',
           **kwargs):

    kwargs.update(button_input)
    buttons(**kwargs)