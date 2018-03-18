from contextlib import contextmanager
import wx


@contextmanager
def init_frame():
    app = wx.App()
    frame = wx.Frame()
    yield frame


def diropenbox(msg='', title=None, default=''):
    with init_frame() as frame:
        dialog = wx.DirDialog(frame, message=msg, defaultPath=default)
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

def filesavebox(msg=None, title=None, default='', filetypes=None):
    # with init_frame() as frame:
    #     dialog = wx.FileDialog(frame, message=msg, defaultPath=default)
    # with wx.FileDialog(self, "Save XYZ file", wildcard="XYZ files (*.xyz)|*.xyz",
    #                    style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
    #
    pass


if __name__ == '__main__':
    samples = (diropenbox, fileopenbox, filesavebox)
    for func in samples:
        print(func())
