#!/usr/bin/env python
# Funtion:      
# Filename:

import wx

app = wx.App()
window = wx.Frame(None, title="wxPython - www.yiibai.com", size=(400, 300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(0, 0))
window.Show(True)
# window.Show(False)
app.MainLoop()