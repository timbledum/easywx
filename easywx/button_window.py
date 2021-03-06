import wx


class ButtonWindow(wx.Frame):

    def __init__(
        self,
        msg=None,
        title=None,
        choices=["Yes", "No", "Maybe"],
        images=None,
        settings=None,
    ):
        super().__init__(None)

        self.SetTitle(title)
        self.result = None

        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        text_label = wx.StaticText(panel, -1, label=msg)
        text_label.Wrap(settings.min_width)
        sizer.Add(text_label, **settings.sizer_settings)

        if images:
            images = self.make_images_iterable(images)

            for image in images:
                png = wx.Image(image, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                image = wx.StaticBitmap(
                    panel, -1, png, (10, 5), (png.GetWidth(), png.GetHeight())
                )
                sizer.Add(
                    image, flag=(wx.ALIGN_CENTER | wx.ALL), border=settings.border
                )

        self.buttons = [wx.Button(panel, -1, text) for text in choices]

        for button in self.buttons:
            button.Bind(wx.EVT_BUTTON, self.button_press)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        for button in self.buttons:
            button_sizer.Add(button, **settings.sizer_settings)

        sizer.Add(button_sizer, **settings.sizer_settings)

        sizer.SetSizeHints(self)
        panel.SetSizerAndFit(sizer)

        panel.Layout()
        self.Show(True)

    def button_press(self, event):
        self.result = self.buttons.index(event.EventObject)
        self.Close()

    def make_images_iterable(self, images):
        if isinstance(images, str):
            return [images]

        try:
            _ = iter(images)
        except TypeError:
            return [images]

        else:
            return images
