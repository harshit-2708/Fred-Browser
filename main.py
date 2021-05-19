import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        nav = QToolBar()
        self.addToolBar(nav)
        back_bt = QAction('Back', self)
        back_bt.triggered.connect(self.browser.back)
        nav.addAction(back_bt)
        for_bt = QAction('Forward', self)
        for_bt.triggered.connect(self.browser.forward)
        nav.addAction(for_bt)
        reload_bt = QAction('Reload', self)
        reload_bt.triggered.connect(self.browser.forward)
        nav.addAction(reload_bt)
        home_bt = QAction('Home', self)
        home_bt.triggered.connect(self.nav_home)
        nav.addAction(home_bt)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.nav_to_url)
        nav.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)


    def nav_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    #
    def nav_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Freadd')
window = MainWindow()
app.exec()
