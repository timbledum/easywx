import pathlib
import attr
import wx


@attr.s
class Settings(object):

    msg = 'Place the flour and salt into a large bowl. Add the butter and using your finger rub together until it resembles fine breadcrumbs. Add the milk and cut it through with a knife to combine and so the soft dough starts to form. Tip onto a floured bench then knead together.'
    img_path = pathlib.Path('easywx', 'generic_logo.png')

    # Appearance defaults
    border = attr.ib(default=20)
    min_width = attr.ib(default=500)
    flag = attr.ib(default=wx.ALL)
    sizer_settings = attr.ib(default={'border': 20,
                                      'flag': wx.ALL})

    # input defaults
    choices = attr.ib(default=['Yes', 'No', 'Maybe'])
    msg = attr.ib(default=msg)
    title = attr.ib(default='Party!')
    images = attr.ib(default=str(img_path))