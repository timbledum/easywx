import attr
import wx


@attr.s
class Settings(object):

    # Appearance defaults
    border = attr.ib(default=20)
    min_width = attr.ib(default=500)
    flag = attr.ib(default=wx.ALL)
    sizer_settings = attr.ib(default={"border": 20, "flag": wx.ALL})
