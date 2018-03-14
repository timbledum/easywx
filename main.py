import wx
import button_window
from settings import Settings


def indexbox(**kwargs):
    settings = Settings(**kwargs)
    app = wx.App()
    frame = button_window.ButtonWindow(settings)
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


if __name__ == '__main__':
    print(indexbox())
    print(ynbox())
    print(ccbox())
