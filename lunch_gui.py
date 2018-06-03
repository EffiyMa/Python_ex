# -*- coding: utf-8 -*-

import wx


class MyFrame1(wx.Frame):
    def __init__(self,superion):
        wx.Frame.__init__(self, parent=superion,id=wx.ID_ANY,title="Lunch Booking System", pos=wx.DefaultPosition,style=wx.DEFAULT_FRAME_STYLE)
        self.Center()
        self.m_panel1=wx.Panel(self)
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, "**************   WELCOME TO EFFIY'S SHOP  :-)  ***********", (20, 20))
        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, "Menu Info", (130, 60), wx.DefaultSize,
                                   style=wx.BORDER_MASK)
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, "My Choice", (130, 120), wx.DefaultSize,
                                   style=wx.BORDER_MASK)

        self.m_button1.Bind(wx.EVT_BUTTON, MyDialog1(None).OnClick)
        self.m_button2.Bind(wx.EVT_BUTTON, MyDialog2(None).OnClick)

        # Backgroud Color
        self.m_button1.SetBackgroundColour('#0a74f7')
        self.m_button1.SetForegroundColour('white')
        self.m_button2.SetBackgroundColour('#0a74f7')
        self.m_button2.SetForegroundColour('white')

        # panel background
        self.m_panel1.SetBackgroundColour('white')

# wx.Dialog1
class MyDialog1(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title="Menu Info", pos=wx.DefaultPosition, size=wx.Size(302, 362),
                           style=wx.DEFAULT_DIALOG_STYLE)
        self.Center()
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        wx.StaticText(self.panel, -1, "Food", (50, 20))
        wx.StaticText(self.panel, -1, "Price", (150, 20))

    def OnClick(self, event):

        fdList=['Crepe','Pudding','Cake','Juice','Tart']
        pcList=['10','5','15','20','3']
        h=30
        for i in range(5):
            h = h + 20
            wx.StaticText(self.panel, label=fdList[i], pos=(50, h))
            wx.StaticText(self.panel, label=pcList[i], pos=(150, h))

        self.ShowModal()

# wx.Dialog2
class MyDialog2(wx.Dialog):
        def __init__(self, parent):
            wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title="My Choice", pos=wx.DefaultPosition,
                                   size=wx.Size(400, 400),
                                   style=wx.DEFAULT_DIALOG_STYLE)
            self.Center()
            self.panel = wx.Panel(self)
            self.panel.SetBackgroundColour('white')

            self.pay = 0

            wx.StaticText(self.panel, -1, "Your Tele :", (20, 20))
            self.t1 = wx.TextCtrl(self.panel, pos=(150, 20), size=(120, 25))

            wx.StaticText(self.panel, -1, "Your Name :", (20, 50))
            self.t2 = wx.TextCtrl(self.panel, pos=(150, 50), size=(120, 25))


            self.ch1 = wx.CheckBox(self.panel, label="Crepe ---- $10 ",pos=(50,100) )
            self.ch2 = wx.CheckBox(self.panel, label="Pudding ---- $5 ", pos=(50, 120))
            self.ch3 = wx.CheckBox(self.panel, label="Cake ---- $10 ", pos=(50, 140))
            self.ch4 = wx.CheckBox(self.panel, label="Juice ---- $20 ", pos=(50, 160))
            self.ch5 = wx.CheckBox(self.panel, label="Tart ---- $3 ", pos=(50, 180))

            self.Bind(wx.EVT_CHECKBOX, self.onChecked1, self.ch1)
            self.Bind(wx.EVT_CHECKBOX, self.onChecked2, self.ch2)
            self.Bind(wx.EVT_CHECKBOX, self.onChecked3, self.ch3)
            self.Bind(wx.EVT_CHECKBOX, self.onChecked4, self.ch4)
            self.Bind(wx.EVT_CHECKBOX, self.onChecked5, self.ch5)

#number of the food
            self.txt1 = wx.TextCtrl(self.panel,  pos=(300, 100), size=(50,20))
            self.txt2 = wx.TextCtrl(self.panel,  pos=(300, 120), size=(50,20))
            self.txt3 = wx.TextCtrl(self.panel,  pos=(300, 140), size=(50,20))
            self.txt4 = wx.TextCtrl(self.panel,  pos=(300, 160), size=(50,20))
            self.txt5 = wx.TextCtrl(self.panel,  pos=(300, 180), size=(50,20))



            self.txts = {"Crepe ---- $10 ": self.txt1, "Pudding ---- $5 ": self.txt2, "Cake ---- $10 ": self.txt3,
                     "Juice ---- $20 ": self.txt4, "Tart ---- $3 ": self.txt5}

            self.result1 = wx.StaticText(self.panel, label='', pos=(20, 220))
            self.result2 = wx.StaticText(self.panel, label='', pos=(20, 230))
            self.result3 = wx.StaticText(self.panel, label='', pos=(20, 240))
            self.result4 = wx.StaticText(self.panel, label='', pos=(20, 250))
            self.result5 = wx.StaticText(self.panel, label='', pos=(20, 260))



        def OnClick(self,e):

            self.btn = wx.Button(self.panel, label="OK!", pos=(20, 200), size=(85, 25))
            self.btn.Bind(wx.EVT_BUTTON, self.Display)

            self.ShowModal()




        def onChecked1(self,e):
            if self.ch1.GetValue() == True:
                self.result1.SetLabel("Crepe has been chosen")

        def onChecked2(self,e):
            if self.ch2.GetValue() == True:
                self.result2.SetLabel("Pudding has been chosen")

        def onChecked3(self, e):
            if self.ch3.GetValue() == True:
                self.result3.SetLabel("Cake has been chosen")


        def onChecked4(self, e):
            if self.ch4.GetValue() == True:
                self.result4.SetLabel("Juice has been chosen")

        def onChecked5(self, e):
            if self.ch5.GetValue() == True:
                self.result5.SetLabel("Tart has been chosen")

        def Display(self,e):
            x=self.txt1.GetValue().encode("utf-8")
            if (x) != '':
                price = int(x)
                self.pay += price*10

            x = self.txt2.GetValue().encode("utf-8")
            if (x) != '':
                price = int(x)
                self.pay += price * 5

            x = self.txt3.GetValue().encode("utf-8")
            if (x) !='':
                price = int(x)
                self.pay += price * 15

            x = self.txt4.GetValue().encode("utf-8")
            if (x) != '':
                price = int(x)
                self.pay += price * 20

            x = self.txt5.GetValue().encode("utf-8")
            if (x ) != '':
                price = int(x)
                self.pay += price * 3

            self.name=self.t2.GetValue().encode("utf-8")
            wx.StaticText(self.panel,label=self.name+'\'s Total Bill',pos=(150,300))
            bill = wx.StaticText(self.panel, label='', pos=(250, 300))
            bill.SetLabel(str(self.pay))









if __name__=='__main__':
    app=wx.App()
    frm=MyFrame1(None)
    frm.Show()
    app.MainLoop()

