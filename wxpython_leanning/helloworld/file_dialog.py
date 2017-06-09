# #!/usr/bin/env python
# # coding:utf-8
# """
#   Author:  u"王浩" --<823921498@qq.com>
#   Purpose: u"文件选择，保存"
#   Created: 2014/8/26
# """
#
# import wx
# import os
#
# wildcard = u"Python 文件 (*.py)|*.py|" \
#            u"编译的 Python 文件 (*.pyc)|*.pyc|" \
#            u" 垃圾邮件文件 (*.spam)|*.spam|" \
#            "Egg file (*.egg)|*.egg|" \
#            "All files (*.*)|*.*"
#
#
# ###############################################################################
# class FileDialog(wx.Frame):
#     """文件选择，保存"""
#
#     # ----------------------------------------------------------------------
#     def __init__(self):
#         """Constructor"""
#         wx.Frame.__init__(self, None, -1)
#         b1 = wx.Button(self, -1, u"选择文件", (50, 50))
#         self.Bind(wx.EVT_BUTTON, self.OnButton1, b1)
#
#         b2 = wx.Button(self, -1, u"保存文件", (50, 90))
#         self.Bind(wx.EVT_BUTTON, self.OnButton2, b2)
#
#         # ----------------------------------------------------------------------
#
#     def OnButton1(self, event):
#         """"""
#         dlg = wx.FileDialog(self, message=u"选择文件",
#                             defaultDir=os.getcwd(),
#                             defaultFile="",
#                             wildcard=wildcard
#                            )    # style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
#
#         if dlg.ShowModal() == wx.ID_OK:
#             paths = dlg.GetPaths()  # 返回一个list，如[u'E:\\test_python\\Demo\\ColourDialog.py', u'E:\\test_python\\Demo\\DirDialog.py']
#             print
#             paths
#             for path in paths:
#                 print
#                 path  # E:\test_python\Demo\ColourDialog.py E:\test_python\Demo\DirDialog.py
#
#         dlg.Destroy()
#
#         # ----------------------------------------------------------------------
#
#     def OnButton2(self, event):
#         """"""
#         dlg = wx.FileDialog(self, message=u"保存文件",
#                             defaultDir=os.getcwd(),
#                             defaultFile="",
#                             wildcard=wildcard,
#                             style=wx.SAVE)
#         dlg.SetFilterIndex(0)  # 设置默认保存文件格式，这里的0是py，1是pyc
#         dlg.ShowModal()
#         dlg.Destroy()
#
#
#         ###############################################################################
#
#
# if __name__ == '__main__':
#     frame = wx.PySimpleApp()
#     app = FileDialog()
#     app.Show()
#     frame.MainLoop()



'''
import wx
import os


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title)

        self.InitUI()

    def InitUI(self):
        self.count = 0
        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        self.text = wx.TextCtrl(pnl, size=(-1, 200), style=wx.TE_MULTILINE)
        self.btn1 = wx.Button(pnl, label="Open a File")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn1)

        hbox1.Add(self.text, proportion=1, flag=wx.ALIGN_CENTRE)
        hbox2.Add(self.btn1, proportion=1, flag=wx.RIGHT, border=10)

        vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)

        vbox.Add(hbox1, proportion=1, flag=wx.EXPAND | wx.ALIGN_CENTRE)

        pnl.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def OnClick(self, e):
        wildcard = ""   # "Text Files (*.txt)|*.txt"
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, wx.FD_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            f = open(dlg.GetPath(), 'r', encoding='utf-8')

            with f:
                data = f.read()
                self.text.SetValue(data)
        dlg.Destroy()


ex = wx.App()
Mywin(None, 'FileDialog Demo - www.yiibai.com')
ex.MainLoop()

'''

import wx

app = wx.App()
win = wx.Frame(
    None,
    title="simple editor",
    size=(410, 335))

bkg = wx.Panel(win)


def openFile(evt):
    dlg = wx.FileDialog(
        win,
        "Open",
        "",
        "",
        "All files (*.*)|*.*",
        wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    filepath = ''
    if dlg.ShowModal() == wx.ID_OK:
        filepath = dlg.GetPath()
    else:
        return
    filename.SetValue(filepath)
    fopen = open(filepath,'r', encoding='utf-8')
    fcontent = fopen.read()
    contents.SetValue(fcontent)
    fopen.close()


def saveFile(evt):
    fcontent = contents.GetValue()
    fopen = open(filename.GetValue(), 'w')
    fopen.write(fcontent)
    fopen.close()


openBtn = wx.Button(bkg, label='open')
openBtn.Bind(wx.EVT_BUTTON, openFile)

saveBtn = wx.Button(bkg, label='save')
saveBtn.Bind(wx.EVT_BUTTON, saveFile)

filename = wx.TextCtrl(bkg, style=wx.TE_READONLY)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE)

hbox = wx.BoxSizer()
hbox.Add(openBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)
hbox.Add(filename, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)
hbox.Add(saveBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)

bbox = wx.BoxSizer(wx.VERTICAL)
bbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL)
bbox.Add(
    contents,
    proportion=1,
    flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,
    border=5)

bkg.SetSizer(bbox)
win.Show()
app.MainLoop()