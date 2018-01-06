import Config
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication,
    QGraphicsDropShadowEffect,QFrame)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal,QRect,QDateTime,QDate
from PyQt5.QtGui import QIcon, QPixmap,QColor,QTransform
from time import strftime
import sys, random


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Slova')
        self.setGeometry(0,0,width,height)
        #background
       
        xscale = float(width) / 1024.0
        yscale = float(height) / 600.0
        frames = []
        framep = 0

        frame1 = QFrame(self)
        frame1.setObjectName("frame1")
        frame1.setGeometry(0, 0, width, height)
        frame1.setStyleSheet("#frame1 { background-color: black; border-image: url(" +
                            Config.background + ") 0 0 0 0 stretch stretch;}")
        frames.append(frame1)

        frame2 = QFrame(self)
        frame2.setObjectName("frame2")
        frame2.setGeometry(0, 0, width, height)
        frame2.setStyleSheet("#frame2 { background-color: transparent; border-image: url(" +
                            Config.background + ") 0 0 0 0 stretch stretch;}")
        frame2.setVisible(False)
        frames.append(frame2)

        ypos=0
        self.temper = QLabel(frame1)
        self.temper.setObjectName("temper")
        self.temper.setStyleSheet("#temper { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(40 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        self.temper.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.temper.setGeometry(0, height *0.26 , 300 * xscale, 100)

        self.power = QLabel(frame1)
        self.power.setObjectName("power")
        self.power.setStyleSheet("#power { background-color: transparent; color: " +
                            Config.textcolor +"; font-size: " +str(int(40 * xscale)) +
                            "px; " +Config.fontattr +"}")
        self.power.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.power.setGeometry(0, height *0.53 , 300 * xscale, 100)

        self.energyDay = QLabel(frame1)
        self.energyDay.setObjectName("power")
        self.energyDay.setStyleSheet("#power { background-color: transparent; color: " +
                            Config.textcolor +"; font-size: " +str(int(40 * xscale)) +
                            "px; " +Config.fontattr +"}")
        self.energyDay.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.energyDay.setGeometry(0, height *0.68 , 300 * xscale, 100)

        self.energyAcc = QLabel(frame1)
        self.energyAcc.setObjectName("power")
        self.energyAcc.setStyleSheet("#power { background-color: transparent; color: " +
                            Config.textcolor +"; font-size: " +str(int(40 * xscale)) +
                            "px; " +Config.fontattr +"}")
        self.energyAcc.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.energyAcc.setGeometry(0, height *0.84 , 300 * xscale, 100)


        self.temper2 = QLabel(frame2)
        self.temper2.setObjectName("temper2")
        self.temper2.setStyleSheet("#temper2 { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(100 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        self.temper2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.temper2.setGeometry(125 * xscale, 780 * yscale, 300 * xscale, 100)

        ypos += 115
        
        self.humidity = QLabel(frame1)
        self.humidity.setObjectName("humidity")
        self.humidity.setStyleSheet("#humidity { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(30 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        self.humidity.setAlignment(Qt.AlignHCenter | Qt.AlignTop) 
        self.humidity.setGeometry(width * 0.04,height*0.33, 300 * xscale, 100)

        ypos += 30
        self.indoorTemp = QLabel(frame1)
        self.indoorTemp.setObjectName("indoorTemp")
        self.indoorTemp.setStyleSheet("#indoorTemp { background-color: transparent; color: " +
                            Config.indoorTextColor +
                            "; font-size: " +
                            str(int(70 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        self.indoorTemp.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.indoorTemp.setGeometry(3 * xscale, ypos * yscale, 300 * xscale, 100)

        ypos += 75
        self.indoorHumi = QLabel(frame1)
        self.indoorHumi.setObjectName("wind")
        self.indoorHumi.setStyleSheet("#wind { background-color: transparent; color: " +
                        Config.textcolor +
                        "; font-size: " +
                        str(int(30 * xscale)) +
                        "px; " +
                        Config.fontattr +
                        "}")
        self.indoorHumi.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.indoorHumi.setGeometry(3 * xscale, ypos * yscale, 300 * xscale, 100)

        ypos += 20
        wind2 = QLabel(frame1)
        wind2.setObjectName("wind2")
        wind2.setStyleSheet("#wind2 { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(20 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        wind2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        wind2.setGeometry(3 * xscale , ypos * yscale , 300 * xscale, 100)

        ypos += 20
        self.wdate = QLabel(frame1)
        self.wdate.setObjectName("wdate")
        self.wdate.setStyleSheet("#wdate { background-color: transparent; color: " +
                            Config.textcolor +
                            "; font-size: " +
                            str(int(15 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        self.wdate.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.wdate.setGeometry(3 * xscale, ypos * yscale, 300 * xscale, 100)


        self.bottom = QLabel(frame1)
        self.bottom.setObjectName("bottom")
        self.bottom.setStyleSheet("#bottom { font-family:sans-serif; color: " +
                            Config.textcolor +
                            "; background-color: transparent; font-size: " +
                            str(int(30 * xscale)) +
                            "px; " +
                            Config.fontattr +
                            "}")
        self.bottom.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.bottom.setGeometry(0, height - 50, width, 50)

        self.temp = QLabel(frame1)
        self.temp.setObjectName("temp")
        self.temp.setStyleSheet("#temp { font-family:sans-serif; color: " +
                        Config.textcolor +
                        "; background-color: transparent; font-size: " +
                        str(int(30 * xscale)) +
                        "px; " +
                        Config.fontattr +
                        "}")
        self.temp.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.temp.setGeometry(0, height - 100, width, 50)
        
        self.showTemp()
        #self.tick()
        #ctimer = QTimer(self)
        #ctimer.timeout.connect(self.tick)
        #ctimer.start(1000)
        self.show()
        #self.showFullScreen()
    
       
    def showTemp(self):
        do_am, nhiet_do,_power,energyDay,energyAccumulation = 90,40,50,1,25

        self.energyAcc.setText(str(energyAccumulation))
        self.energyDay.setText(str(energyDay))
        self.power.setText(str(_power))
        self.temper.setText(str(nhiet_do))
        #self.temper2.setText(str(100) + u'°C')
        self.humidity.setText(str(do_am))
    
"""
    def tick(self):
        #print('tick')
        global hourpixmap, minpixmap, secpixmap
        global hourpixmap2, minpixmap2, secpixmap2
        global lastmin, lastday, lasttimestr
        global clockrect
        global datex, datex2, datey2, pdy
        now_second = int(strftime("%S"))
        angle = now_second * 6
        ts = secpixmap.size()
        secpixmap2 = secpixmap.transformed(
            QTransform().scale(
                float(clockrect.width()) / ts.height(),
                float(clockrect.height()) / ts.height()
            ).rotate(angle),
            Qt.SmoothTransformation
        )
        self.sechand.setPixmap(secpixmap2)
        ts = secpixmap2.size()
        self.sechand.setGeometry(
            clockrect.center().x() - ts.width() / 2,
            clockrect.center().y() - ts.height() / 2,
            ts.width(),
            ts.height()
        )
        now_minute = int(strftime('%M'))
        now_hour = int(strftime('%H'))
        if now_minute != lastmin:
            lastmin = now_minute
            angle = now_minute * 6
            ts = minpixmap.size()
            minpixmap2 = minpixmap.transformed(
                QTransform().scale(
                    float(clockrect.width()) / ts.height(),
                    float(clockrect.height()) / ts.height()
                ).rotate(angle),
                Qt.SmoothTransformation
            )
            self.minhand.setPixmap(minpixmap2)
            ts = minpixmap2.size()
            self.minhand.setGeometry(
                clockrect.center().x() - ts.width() / 2,
                clockrect.center().y() - ts.height() / 2,
                ts.width(),
                ts.height()
            )

            angle = ((now_hour % 12) + now_minute / 60.0) * 30.0
            ts = hourpixmap.size()
            hourpixmap2 = hourpixmap.transformed(
                QTransform().scale(
                    float(clockrect.width()) / ts.height(),
                    float(clockrect.height()) / ts.height()
                ).rotate(angle),
                Qt.SmoothTransformation
            )
            self.hourhand.setPixmap(hourpixmap2)
            ts = hourpixmap2.size()
            self.hourhand.setGeometry(
                clockrect.center().x() - ts.width() / 2,
                clockrect.center().y() - ts.height() / 2,
                ts.width(),
                ts.height()
            )

        dy = strftime("0:%I:%M %p")
        if dy != pdy:
            pdy = dy
            datey2.setText(dy)
        now_day = int(strftime("%d"))
        if now_day != lastday:
            lastday = now_day
            # date
            sup = 'th'
            if (now_day == 1 or now_day == 21 or now_day == 31):
                sup = 'st'
            if (now_day == 2 or now_day == 22):
                sup = 'nd'
            if (now_day == 3 or now_day == 23):
                sup = 'rd'
            if Config.DateLocale != "":
                sup = ""
            ds = strftime("%A %B %d %Y")
            datex.setText(ds)
            datex2.setText(ds)
"""

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    desktop = app.desktop()
    rec = desktop.screenGeometry()
    height = rec.height()
    width = rec.width()
    myApp = App()    
    sys.exit(app.exec_())    