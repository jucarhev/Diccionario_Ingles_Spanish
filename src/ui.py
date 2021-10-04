#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from src.database_manager import *

class UI(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__ (self,parent,0,style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
		favicon = wx.Icon('src/icon/notebook.png',wx.BITMAP_TYPE_PNG, 16,16)
		self.SetIcon(favicon)
		self.SetSize((300,500))
		self.SetTitle("Diccionario")
		self.Centre()
		self.Show()

		self.menu()
		self.gui()

	def menu(self):
		self.menubar = wx.MenuBar(0)
		self.file_menu = wx.Menu()
		self.file_menu_close = wx.MenuItem( self.file_menu,wx.ID_EXIT,u"Close",wx.EmptyString,wx.ITEM_NORMAL)
		self.file_menu.Append(self.file_menu_close)
		self.menubar.Append(self.file_menu, u"&File")
		self.help_menu = wx.Menu()
		self.help_menu_about = wx.MenuItem( self.help_menu,0,u"About",wx.EmptyString,wx.ITEM_NORMAL)
		self.help_menu.Append(self.help_menu_about)
		self.menubar.Append(self.help_menu, u"&Help")
		self.SetMenuBar(self.menubar)

		self.Bind(wx.EVT_MENU, self.salir, self.file_menu_close)
		self.Bind(wx.EVT_MENU, self.about, self.help_menu_about)

	def gui(self):
		bSizer1 = wx.BoxSizer(wx.VERTICAL)
		bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"En", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleBtn1.SetValue( True ) 
		bSizer2.Add( self.m_toggleBtn1, 0, wx.ALL|wx.EXPAND, 5 )
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"src/icon/clear.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.m_bpButton1, 0, wx.ALL|wx.EXPAND, 5 )
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
		self.m_textCtrl2.SetBackgroundColour( wx.Colour( 229, 229, 229 ) )
		bSizer3.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		self.SetSizer( bSizer1 )
		self.Layout()
		self.statusbar = self.CreateStatusBar()

		self.Bind(wx.EVT_TEXT,self.click,self.m_textCtrl1)
		self.Bind(wx.EVT_BUTTON,self.clear,self.m_bpButton1)
		self.Bind(wx.EVT_TOGGLEBUTTON,self.change,self.m_toggleBtn1)

	def click(self,evt):
		lst = Database_Manager()
		valor = self.m_toggleBtn1.GetValue()
		if self.m_textCtrl1.GetValue() != '':
			if valor == True:
				# True  = English
				self.m_toggleBtn1.SetLabel('En')
				sql = "select eword,sword from dict where eword like '"+self.m_textCtrl1.GetValue()+"%';"
				array = lst.query(sql)
				self.textarea(array)
				self.statusbar.SetStatusText(str(lst.num_rows(sql)))
			else:
				# False = Spanish
				self.m_toggleBtn1.SetLabel('Es')
				sql = "select sword,eword from dict where sword like '"+self.m_textCtrl1.GetValue()+"%';"
				array = lst.query(sql)
				self.textarea(array)
				self.statusbar.SetStatusText(str(lst.num_rows(sql)))

	def clear(self,evt):
		self.m_textCtrl1.SetValue('')
		self.m_textCtrl2.SetValue('')

	def change(self,evt):
		valor = self.m_toggleBtn1.GetValue()
		if valor == True:
			# True  = English
			self.m_toggleBtn1.SetLabel('En')
		else:
			# False = Spanish
			self.m_toggleBtn1.SetLabel('Es')

	def textarea(self,array):
		self.m_textCtrl2.SetValue('')
		for row in array:
			ar = row.split(':')
			self.m_textCtrl2.SetDefaultStyle(wx.TextAttr(wx.RED))
			self.m_textCtrl2.AppendText(str(ar[0]) + ': ')
			self.m_textCtrl2.SetDefaultStyle(wx.TextAttr(wx.BLUE))
			self.m_textCtrl2.AppendText(ar[1]+'\n')

	def salir(self,evt):
		self.Destroy()

	def about(self,evt):
		conecta = abuot(None)
		conecta.ShowModal()
		conecta.Destroy()

class abuot ( wx.Dialog ):
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 446,256 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"src/icon/notebook128x128.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Diccionario English-Spanish", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"https://github.com/jucarhev/Diccionario_Ingles_Spanish", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )