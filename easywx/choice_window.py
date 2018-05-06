import wx


class ChoiceWindow(wx.Frame):

    def __init__(
        self,
        msg=None,
        title=None,
        choices=["Yes", "No", "Maybe"],
        preselect=0,
        multiple=False,
        settings=None,
    ):
        super().__init__(None)

        self.SetTitle(title)
        self.result = None
        self.choices = choices

        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        text_label = wx.StaticText(panel, -1, label=msg)
        text_label.Wrap(settings.min_width)
        sizer.Add(text_label, **settings.sizer_settings)

        wx_multi = wx.LB_EXTENDED if multiple else wx.LB_SINGLE
        self.list_box = wx.ListBox(panel, -1, choices=self.choices, style=wx_multi)

        self.list_box.SetSelection(preselect)
        sizer.Add(self.list_box, **settings.sizer_settings)

        self.buttons = [wx.Button(panel, -1, text) for text in ["Cancel", "OK"]]

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

        button_clicked = self.buttons.index(event.EventObject)
        result = self.list_box.GetSelections()
        if button_clicked == 1:
            self.result = [self.choices[ind] for ind in result]
        else:
            self.result = None
        self.Close()
