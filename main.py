from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtWebEngineWidgets import *



class MyWebBrowser(QMainWindow):


    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Test Browser")


        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()


        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)


        self.go_button = QPushButton("Go")
        self.go_button.setMinimumHeight(30)
        
        self.back_botton = QPushButton("<")
        self.back_botton.setMinimumHeight(30)

        self.forward_button = QPushButton(">")
        self.forward_button.setMinimumHeight(30)


        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_button)
        self.horizontal.addWidget(self.back_botton)
        self.horizontal.addWidget(self.forward_button)


        self.browser = QWebEngineView()

        self.go_button.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_botton.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://www.google.com/"))


        self.window.setLayout(self.layout)
        self.window.show()


    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://www." + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = MyWebBrowser()
app.exec_()

        

