#!/usr/bin/env python
# Funtion:      
# Filename:

import wx

class bucky(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent,id, "Frame tjy window", size = (300, 200))
        panel= wx.Panel(self)

        status = self.CreateStatusBar()
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        first.Append(wx.NewId(), "New Window", "This is a new window")
        first.Append(wx.NewId(), "Open...", "This will open a new window")
        second.Append(wx.NewId(), "Cut", "Cut to clipboard")
        second.Append(wx.NewId(), "Copy", "Copy to clipboard")
        menubar.Append(first,"File")
        menubar.Append(second, "Edit")
        self.SetMenuBar(menubar)

if __name__ == "__main__":
    app = wx.App()
    frame = bucky(parent=None, id=-1)
    frame.Show()    # 显示框架
    app.MainLoop()  # 运行