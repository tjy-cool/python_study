#!/usr/bin/env python
# Funtion:      
# Filename:

import wx
import time
time.strftime()
class bucky(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent,id, "Frame tjy window", size = (300, 200))
        panel= wx.Panel(self)
        # button = wx.Button(panel, label="exit", pos=(130,10), size=(120,60))
        # self.Bind(wx.EVT_BUTTON, self.closebutton, button)      # 绑定事件
        self.Bind(wx.EVT_CLOSE, self.closewindow)           # 绑定事件

    def closebutton(self, event):       # 事件
        self.Close(True)

    def closewindow(self, event):       # 事件
        self.Destroy()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = bucky(parent=None, id=-1)
    frame.Show()    # 显示框架
    app.MainLoop()  # 循环监听事件