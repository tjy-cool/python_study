# #!/usr/bin/env python
# # Funtion:
# # Filename:
#
# import wx
# import Gauge
#
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent):
#         wx.Frame.__init__(self, parent, -1, "ColourGauge Demo")
#
#         panel = wx.Panel(self)
#
#         gauge1 = Gauge.ColourGauge(panel, -1, size=(100, 25))
#         gauge1.setPercent(0.8)
#         gauge1.setBarColour(wx.RED)
#         gauge1.setBackgroundColour(wx.WHITE)
#
#         gauge2 = Gauge.ColourGauge(panel, -1, size=(200, 50))
#         gauge2.setPercent(0.9)
#         gauge2.setBarColour(wx.RED)
#         gauge2.setBackgroundColour(wx.BLUE)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(gauge1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 20)
#         sizer.Add(gauge2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 20)
#
#         panel.SetSizer(sizer)
#         sizer.Layout()
#
#
# # our normal wxApp-derived class, as usual
#
# app = wx.App(0)
#
# frame = MyFrame(None)
# app.SetTopWindow(frame)
# frame.Show()
#
# app.MainLoop()

import wx
import time
class GuageFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Gauge Example', size=(600, 300))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("white")
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 100, (100, 60), (250, 25), style=wx.GA_SMOOTH) #style=wx.GA_PROGRESSBAR
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

    def OnIdle(self, event):

        if self.count >= 100:
            self.gauge.SetValue(self.count)
            self.count = 0
            time.sleep(1)
        # else:
        time.sleep(0.2)
        self.gauge.SetValue(self.count)
        self.count = self.count + 1


if __name__ == '__main__':
    app = wx.App()
    frame = GuageFrame()
    frame.Show()
    app.MainLoop()