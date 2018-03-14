import wx


class ButtonWindow(wx.Frame):
    def __init__(self, settings):
        super().__init__(None)

        self.SetTitle(settings.title)
        self.result = None

        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        text_label = wx.StaticText(panel, -1, label=settings.msg)
        text_label.Wrap(settings.min_width)
        sizer.Add(text_label, **settings.sizer_settings)

        choices = settings.choices
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
