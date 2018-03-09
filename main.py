from sogou import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QUrl
import urllib3
import requests
import pandas as pd
import re
from pyquery import PyQuery as pq
import json
import threading


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.timer=QTimer(self)
        self.bt1.clicked.connect(self.c_bt1)
        self.bt2.clicked.connect(self.c_bt2)
        self.bt3.clicked.connect(self.c_bt3)
        self.timer.timeout.connect(self.t_autodo)
        self.headers={
		'Accept': 'text/html, application/xhtml+xml, */*',
		'Accept-Language': 'zh-CN',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; MHA-AL00 Build/HUAWEIMHA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 SogouSearch Android1.0 version3.0 AppVersion/5915',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept-Encoding': 'gzip, deflate',
		'Connection': 'keep-alive',
		'Host': '140.143.49.31',
		'X-Requested-With': 'com.sogou.activity.src',
		'Referer': 'http://nb.sa.sogou.com/',
		}
        self.s=requests.session()
        self.s.headers=self.headers
        self.url="http://140.143.49.31/api/ans2?key=%s"
        self.url1="http://140.143.231.132/weball/api/felab/websocket/getChannelData"
        self.no=0
        self.qq_list=[]
        self.so1=""
        self.so2=""
        self.load_data()

    def t_autodo(self):
        self.no+=1
        self.get_data()
        print(self.no)

    def load_data(self):
        html=self.s.get(self.url1 ,verify=False)
        html.encoding='utf-8'
        text=html.text
        dict1=json.loads(text)
        res=eval(dict1['channelTypeList'])
        self.cmbox.clear()
        for i in res:
            item=i['name']+'->'+i['channel']
            self.cmbox.addItem(item)
            print(item)
            
    def c_bt3(self):
        #self.go_baidu(self.so1)
        #self.go_baidu(self.so2,web=2)
        qq1="10. 刺杀了春秋国君吴王僚的著名刺客是谁？"
        an=['荆轲', '专诸', '聂政']
        #self.go_baidu(qq1,an)
        self.go_baidu(self.so1,self.so2)
        #self.go_baidu1(an)
        #t1 = threading.Thread(target=self.go_baidu, args=(qq1, an,))
        #t2 = threading.Thread(target=self.go_baidu1, args=(an))
        #t1.start()
        #t2.start()

    def go_baidu(self,key,ans):
        url="http://www.baidu.com/s?wd=%s" %key
        html=requests.get(url)
        html.encoding="utf-8"
        code = html.text
        if len(ans)>0:
            str1=ans[0]
            print(ans[0])
            #str1=str1.replace("'","")
            code=code.replace(str1,"<em style='color:red;background-color:yellow'>%s</em>" %str1)
            str1=ans[1]
            #str1=str1.replace("'","")
            code=code.replace(str1,"<em style='color:green;background-color:yellow'>%s</em>" %str1)
            str1=ans[2]
            #str1=str1.replace("'","")
            code=code.replace(str1,"<em style='color:blue;background-color:yellow'>%s</em>" %str1)

        self.web1.setHtml(code)

    def go_baidu1(self,ans):
        if len(ans)==0:
            return
        key=ans[0]+" "+ans[1]+" "+ans[2]
        url="http://www.baidu.com/s?wd=%s" %key
        html=requests.get(url)
        html.encoding="utf-8"
        code=html.text
        self.web2.setHtml(code)

    def c_bt1(self):
        self.no=0
        self.qq_list = []
        self.timer.start(200)
        self.bt2.setEnabled(True)
        self.bt1.setEnabled(False)

    def c_bt2(self):
        self.timer.stop()
        self.bt1.setEnabled(True)
        self.bt2.setEnabled(False)

    def get_data(self):
        try:
            txt=self.cmbox.currentText()
            find=txt.find("->")
            code=txt[find+2:]
            url=self.url % code
            html=self.s.get(url ,verify=False)
            html.encoding='utf-8'
            text=html.text
            fi=text.find("{")
            la=text.find("}",-4)
            txt=text[fi:la+1]
            dict1=json.loads(txt)
            #print(dict1)
            res=dict1['result']
            aDict = json.loads(res[-1])
            qq=aDict['title']
            if qq not in self.qq_list:
                self.qq_list.append(qq)
                res=aDict['result']
                ans=aDict['answers']
                memo=aDict['search_infos'][0]['summary']
                htmlCode="%s<br><font color='red' size==12>答案:[%s]</font><br>%s" %(qq,res,str(ans))
                self.txt.setHtml(htmlCode)
                self.so1=qq
                self.so2=ans
                self.go_baidu(qq,ans)
                print(qq,res)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sty='''
	*
	{
	background-color: qlineargradient(x1: 0, y1: 0, x2: 2, y2: 2,
                                      stop: 0 #DFD8CB, stop: 1 #EDDBAE);
	}
    QPushButton
    { 
	color: red；
	}  
    QPushButton:hover 
    {Color:blue}
    '''
    w.setStyleSheet(sty)
    sys.exit(app.exec_())
