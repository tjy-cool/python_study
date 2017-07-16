#!/usr/bin/env python
# Funtion:      
# Filename:

import wx

class bucky(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent,id, "Frame tjy window", size = (300, 200))
        panel= wx.Panel(self)

        box = wx.MessageDialog(None, "Do I have the best tuts?", 'Title', wx.OK)    # wx.OK
        answer = box.ShowModal()

        box.Destroy()

if __name__ == "__main__":
    app = wx.App()
    frame = bucky(parent=None, id=-1)
    frame.Show()    # 显示框架
    app.MainLoop()  # 运行