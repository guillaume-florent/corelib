# coding: utf-8

r"""Log panel that displays log messages"""

import wx
import logging


class WxTextCtrlHandler(logging.Handler):
    r"""Wx text control log handler

    Parameters
    ----------
    ctrl : wx.TextCtrl
        The control that will display the message
    threadsafe : bool, optional (default is False)

    """

    colors = {logging.DEBUG: wx.Colour(224, 224, 224),
              logging.INFO: wx.Colour(0, 204, 0),
              logging.WARNING: wx.Colour(255, 128, 0),
              logging.ERROR: wx.Colour(255, 51, 51),
              logging.CRITICAL: wx.Colour(102, 0, 102)}

    def __init__(self, ctrl, threadsafe=False):
        logging.Handler.__init__(self)
        self.ctrl = ctrl
        self.threadsafe = threadsafe

    def emit(self, record):
        r"""Overriding the emit() method of Handler

        Parameters
        ----------
        record : ?
            The record to display

        """
        s = self.format(record) + '\n'

        if self.threadsafe is True:
            wx.CallAfter(self.ctrl.SetForegroundColour,
                         WxTextCtrlHandler.colors[record.levelno])
            wx.CallAfter(self.ctrl.WriteText, s)
        else:
            self.ctrl.SetForegroundColour(
                WxTextCtrlHandler.colors[record.levelno])
            self.ctrl.WriteText(s)


class LogPanel(wx.Panel):
    r"""A panel that displays messages generated by logging statements

    Parameters
    ----------
    parent : the wx parent widget
    threadsafe : bool, optional (default is False)

    """

    mapping = {"DEBUG": logging.DEBUG,
               "INFO": logging.INFO,
               "WARNING": logging.WARNING,
               "ERROR": logging.ERROR,
               "CRITICAL": logging.CRITICAL}

    def __init__(self,
                 parent,
                 threadsafe=False,
                 format_='%(asctime)s :: %(levelname)8s :: '
                         '%(name)35s :: %(message)s'):
        super(LogPanel, self).__init__(parent, wx.ID_ANY)

        # Add a panel so it looks the correct on all platforms
        style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.TE_RICH2
        self.log = wx.TextCtrl(self, wx.ID_ANY, size=(400, 100),
                               style=style)

        # Use a font where spaces and characters have the same width
        font = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.log.SetFont(font)
        btn_clear = wx.Button(self, wx.ID_ANY, 'Clear')
        self.Bind(wx.EVT_BUTTON, self.on_button_clear, btn_clear)

        levels = list(LogPanel.mapping.keys())
        selection_index = 1

        level_choice = wx.ComboBox(self,
                                   wx.ID_ANY,
                                   style=wx.CB_DROPDOWN | wx.CB_READONLY,
                                   value=levels[selection_index],
                                   choices=levels)
        self.Bind(wx.EVT_COMBOBOX, self.on_level_selected, level_choice)

        # Add widgets to a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        controls_sizer = wx.BoxSizer(wx.HORIZONTAL)
        controls_sizer.Add(level_choice, 0, wx.LEFT, 5)
        controls_sizer.Add(btn_clear, 0, wx.RIGHT, 5)

        sizer.Add(self.log, 1, wx.ALL | wx.EXPAND, 5)
        sizer.Add(controls_sizer, 0, wx.CENTER)
        self.SetSizer(sizer)

        # Get the root logger
        self.logger = logging.getLogger()

        handler = WxTextCtrlHandler(self.log, threadsafe=threadsafe)
        self.logger.addHandler(handler)
        handler.setFormatter(logging.Formatter(format_))
        self.logger.setLevel(LogPanel.mapping[levels[selection_index]])

    def on_button_clear(self, event):
        r"""Callback for a click on the clear button"""
        self.log.Clear()

    def on_level_selected(self, event):
        r"""Callback for a value change in the level combo box"""
        selected_level = event.GetEventObject().GetValue()
        self.logger.setLevel(LogPanel.mapping[selected_level])