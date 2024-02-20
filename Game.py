#добавить таблицу лидеров
#добавить правильное число в диалоговые окна, win и loss

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIntValidator
from os import path, chdir
from random import randint
import gspread

directory = path.dirname(path.abspath(__file__))
chdir(directory)

gc = gspread.service_account(filename='score-game-414413-106ebc34d3ce.json')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        font_path = "Chalkduster.ttf"
        QtGui.QFontDatabase.addApplicationFont(font_path)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(560, 433)
        MainWindow.setMinimumSize(QtCore.QSize(560, 429))
        MainWindow.setMaximumSize(QtCore.QSize(560, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picturs/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 13, 172, 255), stop:1 rgba(0, 170, 114, 255));\n"
    "font-family: \"Chalkduster\";\n"
    "font-size: 14pt;\n"
    )
        self.centralwidget.setObjectName("centralwidget")
        self.chash_bar = QtWidgets.QFrame(parent=self.centralwidget)
        self.chash_bar.setGeometry(QtCore.QRect(10, 0, 541, 60))
        self.chash_bar.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.chash_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.chash_bar.setObjectName("chash_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.chash_bar)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, -1, 20, -1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon_score = QtWidgets.QPushButton(parent=self.chash_bar)
        self.icon_score.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.icon_score.setMaximumSize(QtCore.QSize(40, 40))
        self.icon_score.setStyleSheet("")
        self.icon_score.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("picturs/score.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.icon_score.setIcon(icon1)
        self.icon_score.setIconSize(QtCore.QSize(50, 50))
        self.icon_score.setObjectName("icon_score")
        self.horizontalLayout.addWidget(self.icon_score)
        self.score = QtWidgets.QLabel(parent=self.chash_bar)
        self.score.setStyleSheet("")
        self.score.setObjectName("score")
        self.horizontalLayout.addWidget(self.score)
        spacerItem = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nickname = QtWidgets.QLineEdit(parent=self.chash_bar)
        self.nickname.setMaximumSize(QtCore.QSize(300, 35))
        self.nickname.setAcceptDrops(True)
        self.nickname.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgb(255, 238, 0);\n"
"border-radius: 10px;")
        self.nickname.setMaxLength(25)
        self.nickname.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.nickname.setCursorPosition(14)
        self.nickname.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nickname.setDragEnabled(False)
        self.nickname.setReadOnly(False)
        self.nickname.setObjectName("nickname")
        self.nickname.setText('Введи имя')
        self.horizontalLayout.addWidget(self.nickname)
        spacerItem = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.icon_money = QtWidgets.QPushButton(parent=self.chash_bar)
        self.icon_money.setMaximumSize(QtCore.QSize(100, 30))
        self.icon_money.setToolTipDuration(-1)
        self.icon_money.setStyleSheet("")
        self.icon_money.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("picturs/money.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.icon_money.setIcon(icon2)
        self.icon_money.setIconSize(QtCore.QSize(35, 35))
        self.icon_money.setObjectName("icon_money")
        self.horizontalLayout.addWidget(self.icon_money)
        self.cash = QtWidgets.QLabel(parent=self.chash_bar)
        self.cash.setStyleSheet("")
        self.cash.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.cash.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.cash.setObjectName("cash")
        self.horizontalLayout.addWidget(self.cash)
        self.frame_pravilo = QtWidgets.QWidget(parent=self.centralwidget)
        self.frame_pravilo.setGeometry(QtCore.QRect(10, 60, 541, 151))
        self.frame_pravilo.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 238, 0);\n"
"border-radius: 10px")
        self.frame_pravilo.setObjectName("frame_pravilo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_pravilo)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pravilo = QtWidgets.QLabel(parent=self.frame_pravilo)
        self.pravilo.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-style: none;")
        self.pravilo.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.pravilo.setScaledContents(False)
        self.pravilo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pravilo.setWordWrap(True)
        self.pravilo.setIndent(-1)
        self.pravilo.setOpenExternalLinks(False)
        self.pravilo.setObjectName("pravilo")
        self.verticalLayout.addWidget(self.pravilo)
        self.frame_stavka = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_stavka.setGeometry(QtCore.QRect(10, 210, 541, 80))
        self.frame_stavka.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_stavka.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_stavka.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_stavka.setObjectName("frame_stavka")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_stavka)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(10, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stavka = QtWidgets.QLabel(parent=self.frame_stavka)
        self.stavka.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stavka.setObjectName("stavka")
        self.horizontalLayout_2.addWidget(self.stavka)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.money_1 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_1.setMaximumSize(QtCore.QSize(30, 30))
        self.money_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_1.setStyleSheet("")
        self.money_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("picturs/moneta_prss.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap("picturs/moneta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        icon4.addPixmap(QtGui.QPixmap("picturs/moneta_1.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.On)
        self.money_1.setIcon(icon4)
        self.money_1.setIconSize(QtCore.QSize(30, 30))
        self.money_1.setCheckable(True)
        self.money_1.setChecked(False)
        self.money_1.setAutoRepeat(False)
        self.money_1.setAutoExclusive(False)
        self.money_1.setAutoRepeatDelay(500)
        self.money_1.setAutoDefault(False)
        self.money_1.setObjectName("money_1")
        self.horizontalLayout_2.addWidget(self.money_1)
        self.money_2 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_2.setMaximumSize(QtCore.QSize(30, 30))
        self.money_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_2.setStyleSheet("")
        self.money_2.setText("")
        self.money_2.setIcon(icon4)
        self.money_2.setIconSize(QtCore.QSize(30, 30))
        self.money_2.setCheckable(True)
        self.money_2.setChecked(False)
        self.money_2.setAutoRepeat(False)
        self.money_2.setAutoExclusive(False)
        self.money_2.setAutoRepeatDelay(500)
        self.money_2.setAutoDefault(False)
        self.money_2.setObjectName("money_2")
        self.horizontalLayout_2.addWidget(self.money_2)
        self.money_3 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_3.setMaximumSize(QtCore.QSize(30, 30))
        self.money_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_3.setStyleSheet("")
        self.money_3.setText("")
        self.money_3.setIcon(icon4)
        self.money_3.setIconSize(QtCore.QSize(30, 30))
        self.money_3.setCheckable(True)
        self.money_3.setChecked(False)
        self.money_3.setAutoRepeat(False)
        self.money_3.setAutoExclusive(False)
        self.money_3.setAutoRepeatDelay(500)
        self.money_3.setAutoDefault(False)
        self.money_3.setObjectName("money_3")
        self.horizontalLayout_2.addWidget(self.money_3)
        self.money_4 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_4.setMaximumSize(QtCore.QSize(30, 30))
        self.money_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_4.setStyleSheet("")
        self.money_4.setText("")
        self.money_4.setIcon(icon4)
        self.money_4.setIconSize(QtCore.QSize(30, 30))
        self.money_4.setCheckable(True)
        self.money_4.setChecked(False)
        self.money_4.setAutoRepeat(False)
        self.money_4.setAutoExclusive(False)
        self.money_4.setAutoRepeatDelay(500)
        self.money_4.setAutoDefault(False)
        self.money_4.setObjectName("money_4")
        self.horizontalLayout_2.addWidget(self.money_4)
        self.money_5 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_5.setMaximumSize(QtCore.QSize(30, 30))
        self.money_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_5.setStyleSheet("")
        self.money_5.setText("")
        self.money_5.setIcon(icon4)
        self.money_5.setIconSize(QtCore.QSize(30, 30))
        self.money_5.setCheckable(True)
        self.money_5.setChecked(False)
        self.money_5.setAutoRepeat(False)
        self.money_5.setAutoExclusive(False)
        self.money_5.setAutoRepeatDelay(500)
        self.money_5.setAutoDefault(False)
        self.money_5.setObjectName("money_5")
        self.horizontalLayout_2.addWidget(self.money_5)
        self.money_6 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_6.setMaximumSize(QtCore.QSize(30, 30))
        self.money_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_6.setStyleSheet("")
        self.money_6.setText("")
        self.money_6.setIcon(icon4)
        self.money_6.setIconSize(QtCore.QSize(30, 30))
        self.money_6.setCheckable(True)
        self.money_6.setChecked(False)
        self.money_6.setAutoRepeat(False)
        self.money_6.setAutoExclusive(False)
        self.money_6.setAutoRepeatDelay(500)
        self.money_6.setAutoDefault(False)
        self.money_6.setObjectName("money_6")
        self.horizontalLayout_2.addWidget(self.money_6)
        self.money_7 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_7.setMaximumSize(QtCore.QSize(30, 30))
        self.money_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_7.setStyleSheet("")
        self.money_7.setText("")
        self.money_7.setIcon(icon4)
        self.money_7.setIconSize(QtCore.QSize(30, 30))
        self.money_7.setCheckable(True)
        self.money_7.setChecked(False)
        self.money_7.setAutoRepeat(False)
        self.money_7.setAutoExclusive(False)
        self.money_7.setAutoRepeatDelay(500)
        self.money_7.setAutoDefault(False)
        self.money_7.setObjectName("money_7")
        self.horizontalLayout_2.addWidget(self.money_7)
        self.money_8 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_8.setMaximumSize(QtCore.QSize(30, 30))
        self.money_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_8.setStyleSheet("")
        self.money_8.setText("")
        self.money_8.setIcon(icon4)
        self.money_8.setIconSize(QtCore.QSize(30, 30))
        self.money_8.setCheckable(True)
        self.money_8.setChecked(False)
        self.money_8.setAutoRepeat(False)
        self.money_8.setAutoExclusive(False)
        self.money_8.setAutoRepeatDelay(500)
        self.money_8.setAutoDefault(False)
        self.money_8.setObjectName("money_8")
        self.horizontalLayout_2.addWidget(self.money_8)
        self.money_9 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_9.setMaximumSize(QtCore.QSize(30, 30))
        self.money_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_9.setStyleSheet("")
        self.money_9.setText("")
        self.money_9.setIcon(icon4)
        self.money_9.setIconSize(QtCore.QSize(30, 30))
        self.money_9.setCheckable(True)
        self.money_9.setChecked(False)
        self.money_9.setAutoRepeat(False)
        self.money_9.setAutoExclusive(False)
        self.money_9.setAutoRepeatDelay(500)
        self.money_9.setAutoDefault(False)
        self.money_9.setObjectName("money_9")
        self.horizontalLayout_2.addWidget(self.money_9)
        self.money_10 = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.money_10.setMaximumSize(QtCore.QSize(30, 30))
        self.money_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.money_10.setStyleSheet("")
        self.money_10.setText("")
        self.money_10.setIcon(icon4)
        self.money_10.setIconSize(QtCore.QSize(30, 30))
        self.money_10.setCheckable(True)
        self.money_10.setChecked(False)
        self.money_10.setAutoRepeat(False)
        self.money_10.setAutoExclusive(False)
        self.money_10.setAutoRepeatDelay(500)
        self.money_10.setAutoDefault(False)
        self.money_10.setObjectName("money_10")
        self.horizontalLayout_2.addWidget(self.money_10)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.check_money = QtWidgets.QPushButton(parent=self.frame_stavka)
        self.check_money.setMaximumSize(QtCore.QSize(100, 40))
        self.check_money.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.check_money.setStyleSheet("")
        self.check_money.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("picturs/OK off.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon5.addPixmap(QtGui.QPixmap("picturs/OK.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.check_money.setIcon(icon5)
        self.check_money.setIconSize(QtCore.QSize(40, 40))
        self.check_money.setCheckable(True)
        self.check_money.setObjectName("check_money")
        self.horizontalLayout_2.addWidget(self.check_money)
        self.horizontalWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(10, 350, 541, 80))
        self.horizontalWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.otvet = QtWidgets.QLabel(parent=self.horizontalWidget)
        self.otvet.setMaximumSize(QtCore.QSize(70, 16777215))
        self.otvet.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.otvet.setObjectName("otvet")
        self.horizontalLayout_6.addWidget(self.otvet)
        self.reply = QtWidgets.QLineEdit(parent=self.horizontalWidget)
        self.reply.setValidator(QIntValidator())
        self.reply.setMaximumSize(QtCore.QSize(60, 30))
        self.reply.setAcceptDrops(True)
        self.reply.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgb(255, 238, 0);\n"
"border-radius: 10px;")
        self.reply.setMaxLength(4)
        self.reply.setFrame(False)
        self.reply.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.reply.setCursorPosition(1)
        self.reply.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.reply.setObjectName("reply")
        self.horizontalLayout_6.addWidget(self.reply)
        self.ok_reply = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.ok_reply.setMaximumSize(QtCore.QSize(40, 40))
        self.ok_reply.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ok_reply.setStyleSheet("QPushButton {\n"
"\n"
"background-image: url(picturs/OK.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-image: url(picturs/OK off.png);\n"
"}")
        self.ok_reply.setText("")
        self.ok_reply.setIconSize(QtCore.QSize(40, 40))
        self.ok_reply.setObjectName("ok_reply")
        self.horizontalLayout_6.addWidget(self.ok_reply)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.return_box = QtWidgets.QLabel(parent=self.horizontalWidget)
        self.return_box.setMinimumSize(QtCore.QSize(300, 62))
        self.return_box.setMaximumSize(QtCore.QSize(300, 62))
        self.return_box.setToolTipDuration(-1)
        self.return_box.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 238, 0);\n"
"border-radius: 10px\n"
"")
        self.return_box.setText("")
        self.return_box.setScaledContents(False)
        self.return_box.setWordWrap(True)
        self.return_box.setObjectName("return_box")
        self.horizontalLayout_6.addWidget(self.return_box)
        self.save_score = QtWidgets.QPushButton(parent=self.horizontalWidget)
        self.save_score.setMaximumSize(QtCore.QSize(40, 40))
        self.save_score.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.save_score.setStyleSheet("QPushButton {\n"
"\n"
"background-image: url(picturs/save_on.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-image: url(picturs/save_off.png);\n"
"}")
        self.save_score.setText("")
        self.save_score.setIconSize(QtCore.QSize(50, 50))
        self.save_score.setObjectName("save_score")
        self.horizontalLayout_6.addWidget(self.save_score)
        self.frame_bet = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_bet.setGeometry(QtCore.QRect(10, 290, 541, 60))
        self.frame_bet.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_bet.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_bet.setObjectName("frame_bet")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_bet)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bet = QtWidgets.QLabel(parent=self.frame_bet)
        self.bet.setStyleSheet("")
        self.bet.setObjectName("bet")
        self.horizontalLayout_3.addWidget(self.bet)
        spacerItem3 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.try_num = QtWidgets.QLabel(parent=self.frame_bet)
        self.try_num.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.try_num.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.try_num.setWordWrap(False)
        self.try_num.setObjectName("try_num")
        self.horizontalLayout_3.addWidget(self.try_num)
        self.big_small = QtWidgets.QLabel(parent=self.centralwidget)
        self.big_small.setGeometry(QtCore.QRect(10, 340, 230, 42))
        self.big_small.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.big_small.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.big_small.setWordWrap(False)
        self.big_small.setObjectName("big_small")
        self.win_dialog = QtWidgets.QMessageBox()
        self.win_dialog.setWindowTitle('Victory')
        self.win_dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 13, 172, 255), stop:1 rgba(0, 170, 114, 255));\n"
    "font-family: \"Chalkduster\";\n"
    "font-size: 14pt;\n"
    )
        
        self.win_lable = QtWidgets.QLabel()
        self.win_lable.setText("<html><head/><body><p>VICTORY</span><img src=\"picturs/smile.png\"/></p></body></html>")
        self.win_lable.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.win_dialog.layout().addWidget(self.win_lable)
        self.win_lable_1 = QtWidgets.QLabel()
        self.win_lable_1.setText(f"<html><head/><body><p>GHBDTN</p></body></html>")
        self.win_lable_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.win_dialog.layout().addWidget(self.win_lable)
        
        self.zadanie()
        MainWindow.setCentralWidget(self.centralwidget)
        self.stavka_user()
        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.check_money.clicked.connect(self.stavka_user)
        self.money_1.clicked.connect(lambda: self.activate_other_buttons(self.money_1))
        self.money_2.clicked.connect(lambda: self.activate_other_buttons(self.money_2))
        self.money_3.clicked.connect(lambda: self.activate_other_buttons(self.money_3))
        self.money_4.clicked.connect(lambda: self.activate_other_buttons(self.money_4))
        self.money_5.clicked.connect(lambda: self.activate_other_buttons(self.money_5))
        self.money_6.clicked.connect(lambda: self.activate_other_buttons(self.money_6))
        self.money_7.clicked.connect(lambda: self.activate_other_buttons(self.money_7))
        self.money_8.clicked.connect(lambda: self.activate_other_buttons(self.money_8))
        self.money_9.clicked.connect(lambda: self.activate_other_buttons(self.money_9))
        self.money_10.clicked.connect(lambda: self.activate_other_buttons(self.money_10))
        self.list_1 = []
        self.score_user = 0
        self.score_PC = 0
        self.cash_user = 10
        
        
        self.ok_reply.clicked.connect(self.game)
        self.icon_score.clicked.connect(self.score_table)
        self.save_score.clicked.connect(self.save_score_table)
        

        

    def zadanie(self):
        

        self.stepen = 1
        num_1 = randint(1,1000)
        num_2 = randint(num_1,1000)
        num_3 = randint(num_1, num_2)
        self.num_1txt = num_1
        self.num_2txt = num_2
        self.num_3txt = num_3
        otrezok = num_2 - num_1
        print(num_3)

        

        while 2 ** self.stepen <= otrezok:
                self.stepen += 1
        
        self.popitki = self.stepen

        self.pravilo.setText(f"<html><head/><body><p><span style=\" font-weight:700;\">Загадано число от {self.num_1txt} до {self.num_2txt}. </span></p><p><span style=\" font-weight:700;\">Это число можно отгадать за {self.stepen} попыток. </span></p><p><span style=\" font-weight:700;\">Отгадаешь, получишь награду x2.</span></p></body></html>")
        self.try_num.setText(f"<html><head/><body><p>Попыток осталось: {self.popitki} </p></body></html>")
      

    def stavka_user(self):
        self.money_bet = int(self.money_1.isChecked() + self.money_2.isChecked() + self.money_3.isChecked() + self.money_4.isChecked() + self.money_5.isChecked() + self.money_6.isChecked() + self.money_7.isChecked() + self.money_8.isChecked() + self.money_9.isChecked() + self.money_10.isChecked())
        self.bet.setText(f"Ваша ставка: {self.money_bet}")


        if self.check_money.isChecked():
            self.money_1.setEnabled(False)
            self.money_2.setEnabled(False)
            self.money_3.setEnabled(False)
            self.money_4.setEnabled(False)
            self.money_5.setEnabled(False)
            self.money_6.setEnabled(False)
            self.money_7.setEnabled(False)
            self.money_8.setEnabled(False)
            self.money_9.setEnabled(False)
            self.money_10.setEnabled(False)
       
        else:
            self.money_1.setEnabled(True)
            self.money_2.setEnabled(True)
            self.money_3.setEnabled(True)
            self.money_4.setEnabled(True)
            self.money_5.setEnabled(True)
            self.money_6.setEnabled(True)
            self.money_7.setEnabled(True)
            self.money_8.setEnabled(True)
            self.money_9.setEnabled(True)
            self.money_10.setEnabled(True)


    def activate_other_buttons(self, button_clicked):
        
        all_buttons = [self.money_1, self.money_2, self.money_3, self.money_4, self.money_5, self.money_6, self.money_7, self.money_8, self.money_9, self.money_10]
        button_index = all_buttons.index(button_clicked)
        for i, button in enumerate(all_buttons):
            if i <= button_index:
                button.setChecked(True)
            else:
                button.setChecked(False) 


    def game(self):
        
        self.check_money.setEnabled(False)

        self.otvet_user = self.reply.text()
        
        list_2 = ', '.join(str(num) for num in self.list_1)


        print(int(self.otvet_user))
        

        if int(self.otvet_user) == int(self.num_3txt):
            self.big_small.setText("<html><head/><body><p><span style=\" color:#f90004;\">Верно</span></p></body></html>")
            self.dialog = QtWidgets.QDialog()
            self.ui = Ui_WIN()
            self.ui.setupUi(self.dialog, self.num_3txt)
            self.dialog.show()
            self.return_box.setText(f"<html><head/><body><p><span style=\" font-weight:700;\">Правильно, загаданное число:{self.num_3txt} </span></p></body></html>")
            self.list_1 = []
            self.score_user += 1
            self.score.setText(f"{self.score_user} : {self.score_PC}")
            self.cash_user = int(self.cash_user) + int(self.money_bet)
            self.cash.setText(f"{self.cash_user}")
            self.check_money.setEnabled(True)
            self.zadanie()
        elif int(self.popitki) == 1:
            self.big_small.setText("<html><head/><body><p><span style=\" color:#f90004;\">Проиграл</span></p></body></html>")
            self.dialog = QtWidgets.QDialog()
            self.ui = Ui_LOSS()
            self.ui.setupUi(self.dialog, self.num_3txt)
            self.dialog.show()
            self.return_box.setText(f"<html><head/><body><p><span style=\" font-weight:700;\">Не правильно, загаданное число:{self.num_3txt} </span></p></body></html>")
            self.list_1 = []
            self.score_PC += 1
            self.score.setText(F"{self.score_user} : {self.score_PC}")
            self.cash_user = int(self.cash_user) - int(self.money_bet)
            self.cash.setText(f"{self.cash_user}")
            self.check_money.setEnabled(True)
            self.zadanie()
        elif int(self.otvet_user) < int(self.num_1txt):
            self.big_small.setText("<html><head/><body><p><span style=\" color:#f90004;\">Ниже порога</span></p></body></html>")
        elif int(self.otvet_user) > int(self.num_2txt):
            self.big_small.setText("<html><head/><body><p><span style=\" color:#f90004;\">Выше порога</span></p></body></html>")
        elif int(self.otvet_user) > int(self.num_3txt):
            self.big_small.setText("<html><head/><body><p><span style=\" color:#f90004;\">Много</span></p></body></html>")
            self.list_1.append(self.otvet_user)
            list_2 = ', '.join(str(num) for num in self.list_1)
            self.return_box.setText(list_2)
            self.reply.clear()
            self.popitki = self.popitki - 1
            self.try_num.setText(f"<html><head/><body><p>Попыток осталось: {self.popitki} </p></body></html>")
            print(self.list_1)
        elif int(self.otvet_user) < int(self.num_3txt):
            self.big_small.setText("<html><head/><body><p><span style=\" color:#f90004;\">Мало</span></p></body></html>")
            self.list_1.append(self.otvet_user)
            list_2 = ', '.join(str(num) for num in self.list_1)
            self.return_box.setText(list_2)
            self.reply.clear()
            self.popitki = self.popitki - 1
            self.try_num.setText(f"<html><head/><body><p>Попыток осталось: {self.popitki} </p></body></html>")
            print(self.list_1)


    def save_score_table(self):
        # Открытие таблицы по URL
        url = 'https://docs.google.com/spreadsheets/d/1b1ZijreGEe4frk1Op6gzTada1zMB7hNFSwo9crery9M/edit?usp=sharing'
        table = gc.open_by_url(url)

        # # Выбор листа, с которым хотите работать
        worksheet = table.sheet1

        self.nickname_text = self.nickname.text()
        # Добавление данных в первую строку
        data = [[self.nickname_text, self.score_user, self.cash_user]]
        print(data)
        worksheet.update(data, 'A16')

    def score_table(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_score_dialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Числовая угадайка"))
        self.icon_score.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Таблица рекордов</span></p></body></html>"))
        self.score.setText(_translate("MainWindow", "0 : 0"))
        self.cash.setText(_translate("MainWindow", "10"))
        self.pravilo.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-weight:700;\">Загадано число от {self.num_1txt} до {self.num_2txt}. </span></p><p><span style=\" font-weight:700;\">Это число можно отгадать за {self.stepen} попыток. </span></p><p><span style=\" font-weight:700;\">Отгадаешь, получишь награду x2.</span></p></body></html>"))
        self.stavka.setText(_translate("MainWindow", "Ставка:"))
        self.otvet.setText(_translate("MainWindow", "Ответ:"))
        self.reply.setText(_translate("MainWindow", ""))
        self.return_box.setText(_translate("MainWindow", ''))
        self.bet.setText(_translate("MainWindow", f"Ваша ставка: 0"))
        self.try_num.setText(_translate("MainWindow", f"<html><head/><body><p>Попыток осталось: {self.popitki} </p></body></html>"))
        self.big_small.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" color:#f90004;\"> </span></p></body></html>"))
        self.icon_money.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Твой кэш заработанный за год)</span></p></body></html>"))
        self.save_score.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Сохранить счет в таблицу рекордов</span></p></body></html>"))


class Ui_WIN(object):
    def setupUi(self, WIN, num_win):
        self.num_win = num_win
        WIN.setObjectName("WIN")
        WIN.resize(294, 350)
        WIN.setMinimumSize(QtCore.QSize(294, 350))
        WIN.setMaximumSize(QtCore.QSize(500, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picturs/win.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        WIN.setWindowIcon(icon)
        WIN.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 13, 172, 255), stop:1 rgba(0, 170, 114, 255));\n"
"font: 14pt \"Chalkduster\";\n"
"\n"
"")
        self.verticalFrame = QtWidgets.QFrame(parent=WIN)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 10, 291, 331))
        self.verticalFrame.setMinimumSize(QtCore.QSize(291, 331))
        self.verticalFrame.setMaximumSize(QtCore.QSize(291, 331))
        self.verticalFrame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(parent=self.verticalFrame)
        self.label_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_1.setWordWrap(False)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.label_victory = QtWidgets.QLabel(parent=self.verticalFrame)
        self.label_victory.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_victory.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_victory.setWordWrap(False)
        self.label_victory.setObjectName("label_victory")
        self.verticalLayout.addWidget(self.label_victory)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalFrame)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_2.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.num_win}</span></p></body></html>")
        self.verticalLayout.addWidget(self.label_2)
        self.ok_next = QtWidgets.QPushButton(parent=self.verticalFrame)
        self.ok_next.setMinimumSize(QtCore.QSize(280, 0))
        self.ok_next.setMaximumSize(QtCore.QSize(40, 40))
        self.ok_next.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ok_next.setStyleSheet("QPushButton {\n"
"\n"
"background-image: url(picturs/OK.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-image: url(picturs/OK off.png);\n"
"}")
        self.ok_next.setText("")
        self.ok_next.setIconSize(QtCore.QSize(40, 40))
        self.ok_next.setObjectName("ok_next")
        self.ok_next.clicked.connect(WIN.close)
        self.verticalLayout.addWidget(self.ok_next)

        self.retranslateUi(WIN)
        QtCore.QMetaObject.connectSlotsByName(WIN)

    def retranslateUi(self, WIN):
        _translate = QtCore.QCoreApplication.translate
        WIN.setWindowTitle(_translate("WIN", "Form"))
        self.label_1.setText(_translate("WIN", "<html><head/><body><p><span style=\" color:#f9cf35;\">VICTORY!!!</span></p></body></html>"))
        self.label_victory.setText(_translate("WIN", "<html><head/><body><p><img src=\"picturs/win.png\"/></p></body></html>"))
        self.label_2.setText(_translate("WIN", f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.num_win}</span></p></body></html>"))


class Ui_LOSS(object):
    def setupUi(self, LOSS, num_loss):
        self.num_loss = num_loss
        LOSS.setObjectName("LOSS")
        LOSS.resize(294, 350)
        LOSS.setMinimumSize(QtCore.QSize(294, 350))
        LOSS.setMaximumSize(QtCore.QSize(294, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picturs/loss.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        LOSS.setWindowIcon(icon)
        LOSS.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 13, 172, 255), stop:1 rgba(0, 170, 114, 255));\n"
"font: 14pt \"Chalkduster\";\n"
"\n"
"")
        self.verticalFrame = QtWidgets.QFrame(parent=LOSS)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 10, 291, 331))
        self.verticalFrame.setMinimumSize(QtCore.QSize(291, 331))
        self.verticalFrame.setMaximumSize(QtCore.QSize(291, 331))
        self.verticalFrame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(parent=self.verticalFrame)
        self.label_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_1.setWordWrap(False)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.label_loss = QtWidgets.QLabel(parent=self.verticalFrame)
        self.label_loss.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_loss.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loss.setWordWrap(False)
        self.label_loss.setObjectName("label_loss")
        self.verticalLayout.addWidget(self.label_loss)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalFrame)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.ok_next = QtWidgets.QPushButton(parent=self.verticalFrame)
        self.ok_next.setMinimumSize(QtCore.QSize(280, 0))
        self.ok_next.setMaximumSize(QtCore.QSize(40, 40))
        self.ok_next.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ok_next.setStyleSheet("QPushButton {\n"
"\n"
"background-image: url(picturs/OK.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-image: url(picturs/OK off.png);\n"
"}")
        self.ok_next.setText("")
        self.ok_next.setIconSize(QtCore.QSize(40, 40))
        self.ok_next.setObjectName("ok_next")
        self.ok_next.clicked.connect(LOSS.close)
        self.verticalLayout.addWidget(self.ok_next)

        self.retranslateUi(LOSS)
        QtCore.QMetaObject.connectSlotsByName(LOSS)

    def retranslateUi(self, LOSS):
        _translate = QtCore.QCoreApplication.translate
        LOSS.setWindowTitle(_translate("LOSS", "Form"))
        self.label_1.setText(_translate("LOSS", "<html><head/><body><p><span style=\" color:#f9cf35;\">LOSS!!!</span></p></body></html>"))
        self.label_loss.setText(_translate("LOSS", "<html><head/><body><p><img src=\"picturs/loss.png\"/></p></body></html>"))
        self.label_2.setText(_translate("LOSS", f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.num_loss}</span></p></body></html>"))


class Ui_score_dialog(object):
    def setupUi(self, score_dialog):
        score_dialog.setObjectName("score_dialog")
        score_dialog.resize(291, 331)
        score_dialog.setMinimumSize(QtCore.QSize(291, 331))
        score_dialog.setMaximumSize(QtCore.QSize(291, 331))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("picturs/score.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        score_dialog.setWindowIcon(icon)
        score_dialog.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 13, 172, 255), stop:1 rgba(0, 170, 114, 255));\n"
"font: 14pt \"Chalkduster\";\n"
"\n"
"")
        self.scrollArea = QtWidgets.QScrollArea(parent=score_dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 300, 261))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(300, 300))
        self.scrollArea.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: solid;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -201, 283, 462))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.name_10 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_10.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_10.setWordWrap(False)
        self.name_10.setObjectName("name_10")
        self.gridLayout_2.addWidget(self.name_10, 10, 1, 1, 1)
        self.score_11 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_11.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_11.setWordWrap(False)
        self.score_11.setObjectName("score_11")
        self.gridLayout_2.addWidget(self.score_11, 11, 2, 1, 1)
        self.score_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_2.setWordWrap(False)
        self.score_2.setObjectName("score_2")
        self.gridLayout_2.addWidget(self.score_2, 1, 2, 1, 1)
        self.money_1 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_1.setWordWrap(False)
        self.money_1.setObjectName("money_1")
        self.gridLayout_2.addWidget(self.money_1, 0, 3, 1, 1)
        self.money_7 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_7.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_7.setWordWrap(False)
        self.money_7.setObjectName("money_7")
        self.gridLayout_2.addWidget(self.money_7, 6, 3, 1, 1)
        self.name_1 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_1.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_1.setWordWrap(False)
        self.name_1.setObjectName("name_1")
        self.gridLayout_2.addWidget(self.name_1, 0, 1, 1, 1)
        self.score_13 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_13.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_13.setWordWrap(False)
        self.score_13.setObjectName("score_13")
        self.gridLayout_2.addWidget(self.score_13, 13, 2, 1, 1)
        self.money_10 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_10.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_10.setWordWrap(False)
        self.money_10.setObjectName("money_10")
        self.gridLayout_2.addWidget(self.money_10, 10, 3, 1, 1)
        self.money_14 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_14.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_14.setWordWrap(False)
        self.money_14.setObjectName("money_14")
        self.gridLayout_2.addWidget(self.money_14, 14, 3, 1, 1)
        self.name_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_6.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_6.setWordWrap(False)
        self.name_6.setObjectName("name_6")
        self.gridLayout_2.addWidget(self.name_6, 5, 1, 1, 1)
        self.score_1 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.score_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_1.setWordWrap(False)
        self.score_1.setObjectName("score_1")
        self.gridLayout_2.addWidget(self.score_1, 0, 2, 1, 1)
        self.name_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_3.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_3.setWordWrap(False)
        self.name_3.setObjectName("name_3")
        self.gridLayout_2.addWidget(self.name_3, 2, 1, 1, 1)
        self.name_15 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_15.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_15.setWordWrap(False)
        self.name_15.setObjectName("name_15")
        self.gridLayout_2.addWidget(self.name_15, 15, 1, 1, 1)
        self.name_12 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_12.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_12.setWordWrap(False)
        self.name_12.setObjectName("name_12")
        self.gridLayout_2.addWidget(self.name_12, 12, 1, 1, 1)
        self.score_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_5.setWordWrap(False)
        self.score_5.setObjectName("score_5")
        self.gridLayout_2.addWidget(self.score_5, 4, 2, 1, 1)
        self.score_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_6.setWordWrap(False)
        self.score_6.setObjectName("score_6")
        self.gridLayout_2.addWidget(self.score_6, 5, 2, 1, 1)
        self.name_14 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_14.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_14.setWordWrap(False)
        self.name_14.setObjectName("name_14")
        self.gridLayout_2.addWidget(self.name_14, 14, 1, 1, 1)
        self.name_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_4.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_4.setWordWrap(False)
        self.name_4.setObjectName("name_4")
        self.gridLayout_2.addWidget(self.name_4, 3, 1, 1, 1)
        self.money_15 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_15.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_15.setWordWrap(False)
        self.money_15.setObjectName("money_15")
        self.gridLayout_2.addWidget(self.money_15, 15, 3, 1, 1)
        self.score_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_3.setWordWrap(False)
        self.score_3.setObjectName("score_3")
        self.gridLayout_2.addWidget(self.score_3, 2, 2, 1, 1)
        self.money_13 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_13.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_13.setWordWrap(False)
        self.money_13.setObjectName("money_13")
        self.gridLayout_2.addWidget(self.money_13, 13, 3, 1, 1)
        self.score_12 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_12.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_12.setWordWrap(False)
        self.score_12.setObjectName("score_12")
        self.gridLayout_2.addWidget(self.score_12, 12, 2, 1, 1)
        self.score_8 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_8.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_8.setWordWrap(False)
        self.score_8.setObjectName("score_8")
        self.gridLayout_2.addWidget(self.score_8, 8, 2, 1, 1)
        self.money_12 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_12.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_12.setWordWrap(False)
        self.money_12.setObjectName("money_12")
        self.gridLayout_2.addWidget(self.money_12, 12, 3, 1, 1)
        self.money_9 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_9.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_9.setWordWrap(False)
        self.money_9.setObjectName("money_9")
        self.gridLayout_2.addWidget(self.money_9, 9, 3, 1, 1)
        self.money_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_2.setWordWrap(False)
        self.money_2.setObjectName("money_2")
        self.gridLayout_2.addWidget(self.money_2, 1, 3, 1, 1)
        self.score_9 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_9.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_9.setWordWrap(False)
        self.score_9.setObjectName("score_9")
        self.gridLayout_2.addWidget(self.score_9, 9, 2, 1, 1)
        self.name_8 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_8.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_8.setWordWrap(False)
        self.name_8.setObjectName("name_8")
        self.gridLayout_2.addWidget(self.name_8, 8, 1, 1, 1)
        self.money_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_6.setWordWrap(False)
        self.money_6.setObjectName("money_6")
        self.gridLayout_2.addWidget(self.money_6, 5, 3, 1, 1)
        self.name_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_2.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_2.setWordWrap(False)
        self.name_2.setObjectName("name_2")
        self.gridLayout_2.addWidget(self.name_2, 1, 1, 1, 1)
        self.name_11 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_11.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_11.setWordWrap(False)
        self.name_11.setObjectName("name_11")
        self.gridLayout_2.addWidget(self.name_11, 11, 1, 1, 1)
        self.score_7 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_7.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_7.setWordWrap(False)
        self.score_7.setObjectName("score_7")
        self.gridLayout_2.addWidget(self.score_7, 6, 2, 1, 1)
        self.money_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_3.setWordWrap(False)
        self.money_3.setObjectName("money_3")
        self.gridLayout_2.addWidget(self.money_3, 2, 3, 1, 1)
        self.name_7 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_7.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_7.setWordWrap(False)
        self.name_7.setObjectName("name_7")
        self.gridLayout_2.addWidget(self.name_7, 6, 1, 1, 1)
        self.money_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_5.setWordWrap(False)
        self.money_5.setObjectName("money_5")
        self.gridLayout_2.addWidget(self.money_5, 4, 3, 1, 1)
        self.money_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_4.setWordWrap(False)
        self.money_4.setObjectName("money_4")
        self.gridLayout_2.addWidget(self.money_4, 3, 3, 1, 1)
        self.money_11 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_11.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_11.setWordWrap(False)
        self.money_11.setObjectName("money_11")
        self.gridLayout_2.addWidget(self.money_11, 11, 3, 1, 1)
        self.score_15 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_15.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_15.setWordWrap(False)
        self.score_15.setObjectName("score_15")
        self.gridLayout_2.addWidget(self.score_15, 15, 2, 1, 1)
        self.name_9 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_9.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"\n"
"")
        self.name_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_9.setWordWrap(False)
        self.name_9.setObjectName("name_9")
        self.gridLayout_2.addWidget(self.name_9, 9, 1, 1, 1)
        self.name_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_5.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_5.setWordWrap(False)
        self.name_5.setObjectName("name_5")
        self.gridLayout_2.addWidget(self.name_5, 4, 1, 1, 1)
        self.money_8 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.money_8.setMaximumSize(QtCore.QSize(40, 16777215))
        self.money_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.money_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.money_8.setWordWrap(False)
        self.money_8.setObjectName("money_8")
        self.gridLayout_2.addWidget(self.money_8, 8, 3, 1, 1)
        self.score_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_4.setWordWrap(False)
        self.score_4.setObjectName("score_4")
        self.gridLayout_2.addWidget(self.score_4, 3, 2, 1, 1)
        self.name_13 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_13.setMaximumSize(QtCore.QSize(130, 16777215))
        self.name_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_13.setWordWrap(False)
        self.name_13.setObjectName("name_13")
        self.gridLayout_2.addWidget(self.name_13, 13, 1, 1, 1)
        self.score_10 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_10.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_10.setWordWrap(False)
        self.score_10.setObjectName("score_10")
        self.gridLayout_2.addWidget(self.score_10, 10, 2, 1, 1)
        self.score_14 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.score_14.setMaximumSize(QtCore.QSize(40, 16777215))
        self.score_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.score_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.score_14.setWordWrap(False)
        self.score_14.setObjectName("score_14")
        self.gridLayout_2.addWidget(self.score_14, 14, 2, 1, 1)
        self.n_1 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_1.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_1.setWordWrap(False)
        self.n_1.setObjectName("n_1")
        self.n_1.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">1</span></p></body></html>")
        self.gridLayout_2.addWidget(self.n_1, 0, 0, 1, 1)
        self.n_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_2.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_2.setWordWrap(False)
        self.n_2.setObjectName("n_2")
        self.gridLayout_2.addWidget(self.n_2, 1, 0, 1, 1)
        self.n_2.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">2</span></p></body></html>")
        self.n_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_3.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_3.setWordWrap(False)
        self.n_3.setObjectName("n_3")
        self.gridLayout_2.addWidget(self.n_3, 2, 0, 1, 1)
        self.n_3.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">3</span></p></body></html>")
        self.n_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_4.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_4.setWordWrap(False)
        self.n_4.setObjectName("n_4")
        self.gridLayout_2.addWidget(self.n_4, 3, 0, 1, 1)
        self.n_4.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">4</span></p></body></html>")
        self.n_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_5.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_5.setWordWrap(False)
        self.n_5.setObjectName("n_5")
        self.gridLayout_2.addWidget(self.n_5, 4, 0, 1, 1)
        self.n_5.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">5</span></p></body></html>")
        self.n_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_6.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_6.setWordWrap(False)
        self.n_6.setObjectName("n_6")
        self.gridLayout_2.addWidget(self.n_6, 5, 0, 1, 1)
        self.n_6.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">6</span></p></body></html>")
        self.n_7 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_7.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_7.setWordWrap(False)
        self.n_7.setObjectName("n_7")
        self.gridLayout_2.addWidget(self.n_7, 6, 0, 1, 1)
        self.n_7.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">7</span></p></body></html>")
        self.n_8 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_8.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_8.setWordWrap(False)
        self.n_8.setObjectName("n_8")
        self.gridLayout_2.addWidget(self.n_8, 8, 0, 1, 1)
        self.n_8.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">8</span></p></body></html>")
        self.n_9 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_9.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_9.setWordWrap(False)
        self.n_9.setObjectName("n_9")
        self.gridLayout_2.addWidget(self.n_9, 9, 0, 1, 1)
        self.n_9.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">9</span></p></body></html>")
        self.n_10 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_10.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_10.setWordWrap(False)
        self.n_10.setObjectName("n_10")
        self.gridLayout_2.addWidget(self.n_10, 10, 0, 1, 1)
        self.n_10.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">10</span></p></body></html>")
        self.n_11 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_11.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_11.setWordWrap(False)
        self.n_11.setObjectName("n_11")
        self.gridLayout_2.addWidget(self.n_11, 11, 0, 1, 1)
        self.n_11.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">11</span></p></body></html>")
        self.n_12 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_12.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_12.setWordWrap(False)
        self.n_12.setObjectName("n_12")
        self.gridLayout_2.addWidget(self.n_12, 12, 0, 1, 1)
        self.n_12.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">12</span></p></body></html>")
        self.n_13 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_13.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_13.setWordWrap(False)
        self.n_13.setObjectName("n_13")
        self.gridLayout_2.addWidget(self.n_13, 13, 0, 1, 1)
        self.n_13.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">13</span></p></body></html>")
        self.n_14 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_14.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_14.setWordWrap(False)
        self.n_14.setObjectName("n_14")
        self.gridLayout_2.addWidget(self.n_14, 14, 0, 1, 1)
        self.n_14.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">14</span></p></body></html>")
        self.n_15 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.n_15.setMaximumSize(QtCore.QSize(25, 16777215))
        self.n_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.n_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.n_15.setWordWrap(False)
        self.n_15.setObjectName("n_14")
        self.gridLayout_2.addWidget(self.n_15, 15, 0, 1, 1)
        self.n_15.setText("<html><head/><body><p><span style=\" color:#f9cf35;\">15</span></p></body></html>")
        self.name_30 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_30.setMaximumSize(QtCore.QSize(25, 16777215))
        self.name_30.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.name_30.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_30.setWordWrap(False)
        self.name_30.setObjectName("name_30")
        self.gridLayout_2.addWidget(self.name_30, 15, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalFrame = QtWidgets.QFrame(parent=score_dialog)
        self.horizontalFrame.setGeometry(QtCore.QRect(0, 270, 291, 61))
        self.horizontalFrame.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.refresh = QtWidgets.QPushButton(parent=self.horizontalFrame)
        self.refresh.setMinimumSize(QtCore.QSize(40, 40))
        self.refresh.setMaximumSize(QtCore.QSize(40, 40))
        self.refresh.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.refresh.setStyleSheet("QPushButton {\n"
"\n"
"background-image: url(picturs/refresh_on.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"\n"
"\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-image: url(picturs/refresh_off.png);\n"
"}")
        self.refresh.setText("")
        self.refresh.setIconSize(QtCore.QSize(40, 40))
        self.refresh.setObjectName("refresh")
        self.horizontalLayout.addWidget(self.refresh)
        self.ok_next = QtWidgets.QPushButton(parent=self.horizontalFrame)
        self.ok_next.setMinimumSize(QtCore.QSize(40, 40))
        self.ok_next.setMaximumSize(QtCore.QSize(40, 40))
        self.ok_next.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ok_next.setStyleSheet("QPushButton {\n"
"\n"
"background-image: url(picturs/OK.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"\n"
"\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-image: url(picturs/OK off.png);\n"
"}")
        self.ok_next.setText("")
        self.ok_next.setIconSize(QtCore.QSize(40, 40))
        self.ok_next.setObjectName("ok_next")
        self.ok_next.clicked.connect(score_dialog.close)
        self.horizontalLayout.addWidget(self.ok_next)
        self.verticalFrame = QtWidgets.QFrame(parent=score_dialog)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 270, 291, 3))
        self.verticalFrame.setMaximumSize(QtCore.QSize(16777215, 3))
        self.verticalFrame.setStyleSheet("border: 3px solid black;")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.refresh.clicked.connect(self.read_score)
        QtCore.QMetaObject.connectSlotsByName(score_dialog)

    def read_score(self):
        # Открытие таблицы по URL
        url = 'https://docs.google.com/spreadsheets/d/1b1ZijreGEe4frk1Op6gzTada1zMB7hNFSwo9crery9M/edit?usp=sharing'
        table = gc.open_by_url(url)

        # Выбор листа, с которым хотите работать
        worksheet = table.sheet1

        # Добавление данных в первую строку
        # data = ["Хуй", "Пизда", "Джигурда"]
        # worksheet.append_row(data)

        # Считывание данных
        cell_value_1 = worksheet.row_values(1)
        self.name_table_1 = cell_value_1 [0]
        self.score_table_1 = cell_value_1 [1]
        self.money_table_1 = cell_value_1 [2]
        self.name_1.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.name_table_1}</span></p></body></html>")
        self.score_1.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.score_table_1}</span></p></body></html>")
        self.money_1.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.money_table_1}</span></p></body></html>")


        cell_value_2 = worksheet.row_values(2)
        self.name_table_2 = cell_value_2 [0]
        self.score_table_2 = cell_value_2 [1]
        self.money_table_2 = cell_value_2 [2]
        self.name_2.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.name_table_2}</span></p></body></html>")
        self.score_2.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.score_table_2}</span></p></body></html>")
        self.money_2.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.money_table_2}</span></p></body></html>")

        cell_value_3 = worksheet.row_values(3)
        self.name_table_3 = cell_value_3 [0]
        self.score_table_3 = cell_value_3 [1]
        self.money_table_3 = cell_value_3 [2]
        self.name_3.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.name_table_3}</span></p></body></html>")
        self.score_3.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.score_table_3}</span></p></body></html>")
        self.money_3.setText(f"<html><head/><body><p><span style=\" color:#f9cf35;\">{self.money_table_3}</span></p></body></html>")

        cell_value_4 = worksheet.row_values(4)
        self.name_table_4 = cell_value_4 [0]
        self.score_table_4 = cell_value_4 [1]
        self.money_table_4 = cell_value_4 [2]
        self.name_4.setText(f"<html><head/><body><p><span style=\" color:#f9cf45;\">{self.name_table_4}</span></p></body></html>")
        self.score_4.setText(f"<html><head/><body><p><span style=\" color:#f9cf45;\">{self.score_table_4}</span></p></body></html>")
        self.money_4.setText(f"<html><head/><body><p><span style=\" color:#f9cf45;\">{self.money_table_4}</span></p></body></html>")

        cell_value_5 = worksheet.row_values(5)
        self.name_table_5 = cell_value_5 [0]
        self.score_table_5 = cell_value_5 [1]
        self.money_table_5 = cell_value_5 [2]
        self.name_5.setText(f"<html><head/><body><p><span style=\" color:#f9cf55;\">{self.name_table_5}</span></p></body></html>")
        self.score_5.setText(f"<html><head/><body><p><span style=\" color:#f9cf55;\">{self.score_table_5}</span></p></body></html>")
        self.money_5.setText(f"<html><head/><body><p><span style=\" color:#f9cf55;\">{self.money_table_5}</span></p></body></html>")

        cell_value_6 = worksheet.row_values(6)
        self.name_table_6 = cell_value_6 [0]
        self.score_table_6 = cell_value_6 [1]
        self.money_table_6 = cell_value_6 [2]
        self.name_6.setText(f"<html><head/><body><p><span style=\" color:#f9cf66;\">{self.name_table_6}</span></p></body></html>")
        self.score_6.setText(f"<html><head/><body><p><span style=\" color:#f9cf66;\">{self.score_table_6}</span></p></body></html>")
        self.money_6.setText(f"<html><head/><body><p><span style=\" color:#f9cf66;\">{self.money_table_6}</span></p></body></html>")

        cell_value_7 = worksheet.row_values(7)
        self.name_table_7 = cell_value_7 [0]
        self.score_table_7 = cell_value_7 [1]
        self.money_table_7 = cell_value_7 [2]
        self.name_7.setText(f"<html><head/><body><p><span style=\" color:#f9cf77;\">{self.name_table_7}</span></p></body></html>")
        self.score_7.setText(f"<html><head/><body><p><span style=\" color:#f9cf77;\">{self.score_table_7}</span></p></body></html>")
        self.money_7.setText(f"<html><head/><body><p><span style=\" color:#f9cf77;\">{self.money_table_7}</span></p></body></html>")

        cell_value_8 = worksheet.row_values(8)
        self.name_table_8 = cell_value_8 [0]
        self.score_table_8 = cell_value_8 [1]
        self.money_table_8 = cell_value_8 [2]
        self.name_8.setText(f"<html><head/><body><p><span style=\" color:#f9cf88;\">{self.name_table_8}</span></p></body></html>")
        self.score_8.setText(f"<html><head/><body><p><span style=\" color:#f9cf88;\">{self.score_table_8}</span></p></body></html>")
        self.money_8.setText(f"<html><head/><body><p><span style=\" color:#f9cf88;\">{self.money_table_8}</span></p></body></html>") 

        cell_value_9 = worksheet.row_values(9)
        self.name_table_9 = cell_value_9 [0]
        self.score_table_9 = cell_value_9 [1]
        self.money_table_9 = cell_value_9 [2]
        self.name_9.setText(f"<html><head/><body><p><span style=\" color:#f9cf99;\">{self.name_table_9}</span></p></body></html>")
        self.score_9.setText(f"<html><head/><body><p><span style=\" color:#f9cf99;\">{self.score_table_9}</span></p></body></html>")
        self.money_9.setText(f"<html><head/><body><p><span style=\" color:#f9cf99;\">{self.money_table_9}</span></p></body></html>")

        cell_value_10 = worksheet.row_values(10)
        self.name_table_10 = cell_value_10 [0]
        self.score_table_10 = cell_value_10 [1]
        self.money_table_10 = cell_value_10 [2]
        self.name_10.setText(f"<html><head/><body><p><span style=\" color:#f10cf1010;\">{self.name_table_10}</span></p></body></html>")
        self.score_10.setText(f"<html><head/><body><p><span style=\" color:#f10cf1010;\">{self.score_table_10}</span></p></body></html>")
        self.money_10.setText(f"<html><head/><body><p><span style=\" color:#f10cf1010;\">{self.money_table_10}</span></p></body></html>")

        cell_value_11 = worksheet.row_values(11)
        self.name_table_11 = cell_value_11 [0]
        self.score_table_11 = cell_value_11 [1]
        self.money_table_11 = cell_value_11 [2]
        self.name_11.setText(f"<html><head/><body><p><span style=\" color:#f11cf1111;\">{self.name_table_11}</span></p></body></html>")
        self.score_11.setText(f"<html><head/><body><p><span style=\" color:#f11cf1111;\">{self.score_table_11}</span></p></body></html>")
        self.money_11.setText(f"<html><head/><body><p><span style=\" color:#f11cf1111;\">{self.money_table_11}</span></p></body></html>")

        cell_value_12 = worksheet.row_values(12)
        self.name_table_12 = cell_value_12 [0]
        self.score_table_12 = cell_value_12 [1]
        self.money_table_12 = cell_value_12 [2]
        self.name_12.setText(f"<html><head/><body><p><span style=\" color:#f12cf1212;\">{self.name_table_12}</span></p></body></html>")
        self.score_12.setText(f"<html><head/><body><p><span style=\" color:#f12cf1212;\">{self.score_table_12}</span></p></body></html>")
        self.money_12.setText(f"<html><head/><body><p><span style=\" color:#f12cf1212;\">{self.money_table_12}</span></p></body></html>")

        cell_value_13 = worksheet.row_values(13)
        self.name_table_13 = cell_value_13 [0]
        self.score_table_13 = cell_value_13 [1]
        self.money_table_13 = cell_value_13 [2]
        self.name_13.setText(f"<html><head/><body><p><span style=\" color:#f13cf1313;\">{self.name_table_13}</span></p></body></html>")
        self.score_13.setText(f"<html><head/><body><p><span style=\" color:#f13cf1313;\">{self.score_table_13}</span></p></body></html>")
        self.money_13.setText(f"<html><head/><body><p><span style=\" color:#f13cf1313;\">{self.money_table_13}</span></p></body></html>")
        
        cell_value_14 = worksheet.row_values(14)
        self.name_table_14 = cell_value_14 [0]
        self.score_table_14 = cell_value_14 [1]
        self.money_table_14 = cell_value_14 [2]
        self.name_14.setText(f"<html><head/><body><p><span style=\" color:#f14cf1414;\">{self.name_table_14}</span></p></body></html>")
        self.score_14.setText(f"<html><head/><body><p><span style=\" color:#f14cf1414;\">{self.score_table_14}</span></p></body></html>")
        self.money_14.setText(f"<html><head/><body><p><span style=\" color:#f14cf1414;\">{self.money_table_14}</span></p></body></html>")

        cell_value_15 = worksheet.row_values(15)
        self.name_table_15 = cell_value_15 [0]
        self.score_table_15 = cell_value_15 [1]
        self.money_table_15 = cell_value_15 [2]
        self.name_15.setText(f"<html><head/><body><p><span style=\" color:#f15cf1515;\">{self.name_table_15}</span></p></body></html>")
        self.score_15.setText(f"<html><head/><body><p><span style=\" color:#f15cf1515;\">{self.score_table_15}</span></p></body></html>")
        self.money_15.setText(f"<html><head/><body><p><span style=\" color:#f15cf1515;\">{self.money_table_15}</span></p></body></html>")



        print(self.name_table_1)
        print(self.score_table_1)
        print(self.money_table_1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())



