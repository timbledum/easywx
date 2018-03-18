from contextlib import contextmanager
from pathlib import Path
import wx

def diropenbox(msg='', title='', default=''):
    app = wx.App()
    frame = wx.Frame()
    dialog = wx.DirDialog(frame, message=title, defaultPath=default)
    dialog.ShowModal()
    path = dialog.GetPath()
    return path


def fileopenbox(msg='',
                title=None,
                default='*',
                filetypes=None,
                multiple=False):
    # with init_frame() as frame:
    #     dialog = wx.FileDialog(frame, message=msg, defaultPath=default)
    # dialog.ShowModal()
    # path = dialog.GetPath()
    # return path
    # wx.FD_MULTIPLE
    pass


def filesavebox(msg='', title=None, default='', filetypes=''):
    default_path = Path(default)
    app = wx.App()
    frame = wx.Frame()
    dialog = wx.FileDialog(frame, message=msg,
                           defaultDir=str(default_path.parent),
                           defaultFile=str(default_path.name),
                           wildcard='',
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
    dialog.ShowModal()
    path = dialog.GetPath()
    return path


if __name__ == '__main__':
    samples = (diropenbox, fileopenbox, filesavebox)
    for func in samples:
        print(func())
