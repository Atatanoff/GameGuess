import wx
import wx.xrc
from GameGuess import GameGuess


gg = GameGuess()

class Frame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Числовая угадайка", pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        LayoutV1 = wx.BoxSizer( wx.VERTICAL )

        self.text = wx.StaticText( self, wx.ID_ANY, gg.textLabel, wx.DefaultPosition, wx.Size( -1,50 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ST_NO_AUTORESIZE)
        self.text.Wrap( -1 )

        LayoutV1.Add( self.text, 0, wx.ALL|wx.EXPAND, 5 )

        self.textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CENTER|wx.TE_PROCESS_ENTER)
		

        LayoutV1.Add( self.textCtrl, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        LayoutV1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( LayoutV1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.textCtrl.Bind( wx.EVT_TEXT_ENTER, self.Gues )
        self.m_button1.Bind( wx.EVT_BUTTON, self.btnClick )

    def __del__( self ):
        pass

    # Virtual event handlers, override them in your derived class
    def Gues( self, event ):
        self.btnClick(event)

    def btnClick(self, e):        
        gg.play(self.textCtrl.GetValue())
        
        if gg.valid and gg.game_over:
            self.textCtrl.Hide()
            self.textCtrl.SetValue('y')
        else:
            self.textCtrl.Show()
            self.textCtrl.Clear()
        
        self.text.SetLabel(gg.textLabel)

if __name__=='__main__': 
    app = wx.App()
    frame = Frame(None)
    frame.Show() 
    app.MainLoop()