#sudo pip3 install PyQt5
#sudo pip3 install PyQtWebEngine

import sys # builtin for app in flask / system
from PyQt5.QtWidgets import *  # they import application widgets
from PyQt5.QtWebEngineWidgets import * # they import all the widgets required for the web engine to work
from PyQt5.QtCore import * # for using QUrl in engine

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__() #connection with main window
		self.browser= QWebEngineView() # for viewing the qt web engine
		self.browser.setUrl(QUrl("http://google.com")) #this will as to set url in form of QUrl with default as google
		#for searching particular queries we can add get method in the link like /(our store variable and execute)
		self.setCentralWidget(self.browser) # this will be out Browser
		self.showMaximized() #browser screen will be of full size
		#navigation Bar
		navbar=QToolBar()
		self.addToolBar(navbar) #adds navigation bar to the browser back and forward button spacing
		# back button
		back_btn=QAction('Back',self)
		# when someone trigger u , u have to connect to the browser and reverse
		back_btn.triggered.connect(self.browser.back)
		navbar.addAction(back_btn) #added to navbar 
		#forward button
		forward_btn=QAction('Forward',self)
		forward_btn.triggered.connect(self.browser.forward) # dont call the function forward just type
		navbar.addAction(forward_btn)
		#reload button
		reload_btn=QAction('Reload',self) # name of the button to appread on screen
		reload_btn.triggered.connect(self.browser.reload)
		navbar.addAction(reload_btn)
		#home button
		home_btn=QAction('Home',self)
		home_btn.triggered.connect(self.navigate_home) # navigate to the searching site
		navbar.addAction(home_btn)
		# core funtionality for website
		self.url_bar=QLineEdit() # line text bar from Qlinebar
		self.url_bar.returnPressed.connect(self.navigate_to_url)
		navbar.addWidget(self.url_bar) # to add add some that type we need widget form to make it work we need action form
		
		#if url is changed then update in the url in text box
		self.browser.urlChanged.connect(self.update_url)

	def update_url(self,q): #q is the url ,it can be named anything q,arl,url its a parameter
			self.url_bar.setText(q.toString())
	def navigate_home(self):
			self.browser.setUrl(QUrl('http://www.google.com'))
	def navigate_to_url(self):
			url= self.url_bar.text() # to pick the url written in the url bar
			self.browser.setUrl(QUrl(url))
		 
app=QApplication(sys.argv) # to create an application
QApplication.setApplicationName("KANAK") #Main app name change this name to your personalise browser name you want
window = MainWindow() # open and create window for app
app.exec_() # to make this code into app execute
