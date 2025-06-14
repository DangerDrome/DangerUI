# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacexEWVpL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(640, 480))
        icon = QIcon()
        icon.addFile(u":/icons/octotools/octo-tools.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"padding:5px; color:#999999; margin-top:0px; margin-bottom:0px; border:0px solid #111111; border-radius:5px; background-color:#333333; font-size: 22px")
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon1 = QIcon()
        icon1.addFile(u":/icons/octotools/task.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon2 = QIcon()
        icon2.addFile(u":/icons/octotools/folder_02.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon3 = QIcon()
        icon3.addFile(u":/icons/octotools/floppy-disk.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        icon4 = QIcon()
        icon4.addFile(u":/icons/svg/material/outlined/Content/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_As.setIcon(icon4)
        self.actionRecent_File = QAction(MainWindow)
        self.actionRecent_File.setObjectName(u"actionRecent_File")
        icon5 = QIcon()
        icon5.addFile(u":/icons/svg/material/TwoTone/Image/timelapse.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRecent_File.setIcon(icon5)
        self.actionRecent_File_02 = QAction(MainWindow)
        self.actionRecent_File_02.setObjectName(u"actionRecent_File_02")
        self.actionRecent_File_02.setIcon(icon5)
        self.actionRecent_File_03 = QAction(MainWindow)
        self.actionRecent_File_03.setObjectName(u"actionRecent_File_03")
        self.actionRecent_File_03.setIcon(icon5)
        self.actionMode = QAction(MainWindow)
        self.actionMode.setObjectName(u"actionMode")
        self.actionMode.setCheckable(True)
        icon6 = QIcon()
        icon6.addFile(u":/icons/svg/material/outlined/Toggle/toggle_off.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/svg/material/outlined/Toggle/toggle_on.svg", QSize(), QIcon.Normal, QIcon.On)
        self.actionMode.setIcon(icon6)
        self.actionObjects = QAction(MainWindow)
        self.actionObjects.setObjectName(u"actionObjects")
        self.actionObjects.setCheckable(True)
        icon7 = QIcon()
        icon7.addFile(u":/icons/svg/material/TwoTone/Content/font_download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionObjects.setIcon(icon7)
        self.actionParameters = QAction(MainWindow)
        self.actionParameters.setObjectName(u"actionParameters")
        self.actionParameters.setCheckable(True)
        self.actionData_Spreadsheet = QAction(MainWindow)
        self.actionData_Spreadsheet.setObjectName(u"actionData_Spreadsheet")
        self.actionData_Spreadsheet.setCheckable(True)
        self.actionOutput_Log = QAction(MainWindow)
        self.actionOutput_Log.setObjectName(u"actionOutput_Log")
        self.actionOutput_Log.setCheckable(True)
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionlogo = QAction(MainWindow)
        self.actionlogo.setObjectName(u"actionlogo")
        self.actionlogo.setIcon(icon)
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionView = QAction(MainWindow)
        self.actionView.setObjectName(u"actionView")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionWindow = QAction(MainWindow)
        self.actionWindow.setObjectName(u"actionWindow")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionMaximize = QAction(MainWindow)
        self.actionMaximize.setObjectName(u"actionMaximize")
        icon8 = QIcon()
        icon8.addFile(u":/icons/svg/material/outlined/Image/crop_din.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMaximize.setIcon(icon8)
        self.actionMinimize = QAction(MainWindow)
        self.actionMinimize.setObjectName(u"actionMinimize")
        icon9 = QIcon()
        icon9.addFile(u":/icons/svg/material/TwoTone/Content/remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMinimize.setIcon(icon9)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon10 = QIcon()
        icon10.addFile(u":/icons/svg/material/TwoTone/Navigation/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionClose.setIcon(icon10)
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        self.actionOpen_3 = QAction(MainWindow)
        self.actionOpen_3.setObjectName(u"actionOpen_3")
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.setObjectName(u"actionSave_2")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color:#1d1d1d; color:#3d3d3d;padding:10px; border:1px dashed #333;")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_10 = QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(24, 24))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(0)
        self.label_3.setOpenExternalLinks(False)

        self.verticalLayout_10.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.widget_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.Status = QStatusBar(MainWindow)
        self.Status.setObjectName(u"Status")
        self.Status.setStyleSheet(u"padding:10px")
        MainWindow.setStatusBar(self.Status)
        self.ToolBar = QToolBar(MainWindow)
        self.ToolBar.setObjectName(u"ToolBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToolBar.sizePolicy().hasHeightForWidth())
        self.ToolBar.setSizePolicy(sizePolicy1)
        self.ToolBar.setMinimumSize(QSize(0, 0))
        self.ToolBar.setStyleSheet(u"padding:10px;")
        self.ToolBar.setIconSize(QSize(30, 30))
        self.ToolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.ToolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.ToolBar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setCursor(QCursor(Qt.SizeAllCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/svg/material/outlined/Editor/table_chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dockWidget.setWindowIcon(icon11)
        self.dockWidget.setStyleSheet(u"padding:10px; border:1px dashed #333;")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidgetContents.setCursor(QCursor(Qt.ArrowCursor))
        self.dockWidgetContents.setStyleSheet(u"background-color:#1d1d1d; color:#3d3d3d;")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.dockWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setFocusPolicy(Qt.NoFocus)
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.widget)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidget_2.setCursor(QCursor(Qt.SizeAllCursor))
        self.dockWidget_2.setStyleSheet(u"padding:10px; border:1px dashed #333;")
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.dockWidgetContents_3.setCursor(QCursor(Qt.ArrowCursor))
        self.dockWidgetContents_3.setStyleSheet(u"background-color:#1d1d1d; color:#3d3d3d;")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.dockWidgetContents_3)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.dockWidget_2.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_2)
        self.dockWidget_3 = QDockWidget(MainWindow)
        self.dockWidget_3.setObjectName(u"dockWidget_3")
        self.dockWidget_3.setCursor(QCursor(Qt.SizeAllCursor))
        self.dockWidget_3.setAutoFillBackground(False)
        self.dockWidget_3.setStyleSheet(u"padding:10px; border:1px dashed #333;")
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.dockWidgetContents_4.setCursor(QCursor(Qt.ArrowCursor))
        self.dockWidgetContents_4.setStyleSheet(u"background-color:#1d1d1d; color:#3d3d3d;")
        self.verticalLayout_7 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_4 = QWidget(self.dockWidgetContents_4)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_9 = QVBoxLayout(self.widget_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2)


        self.verticalLayout_7.addWidget(self.widget_4)

        self.dockWidget_3.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget_3)
        self.dockWidget_4 = QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName(u"dockWidget_4")
        self.dockWidget_4.setCursor(QCursor(Qt.SizeAllCursor))
        self.dockWidget_4.setStyleSheet(u"padding:10px; border:1px dashed #333;")
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.dockWidgetContents_5.setCursor(QCursor(Qt.ArrowCursor))
        self.dockWidgetContents_5.setStyleSheet(u"background-color:#1d1d1d; color:#3d3d3d;")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_3 = QWidget(self.dockWidgetContents_5)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.dockWidget_4.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget_4)
        self.RightToolBar = QToolBar(MainWindow)
        self.RightToolBar.setObjectName(u"RightToolBar")
        self.RightToolBar.setMaximumSize(QSize(10, 10))
        self.RightToolBar.setStyleSheet(u"padding:0px")
        self.RightToolBar.setMovable(False)
        MainWindow.addToolBar(Qt.RightToolBarArea, self.RightToolBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1088, 46))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuWindow = QMenu(self.menuBar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.ToolBar.addAction(self.actionNew)
        self.ToolBar.addAction(self.actionOpen)
        self.ToolBar.addAction(self.actionSave)
        self.ToolBar.addSeparator()
        self.ToolBar.addSeparator()
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addAction(self.actionOpen_3)
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OctoTools", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(statustip)
        self.actionNew.setStatusTip(QCoreApplication.translate("MainWindow", u"New File", None))
#endif // QT_CONFIG(statustip)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(statustip)
        self.actionOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Open File", None))
#endif // QT_CONFIG(statustip)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(QCoreApplication.translate("MainWindow", u"Save File", None))
#endif // QT_CONFIG(statustip)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
#if QT_CONFIG(statustip)
        self.actionSave_As.setStatusTip(QCoreApplication.translate("MainWindow", u"Save File As...", None))
#endif // QT_CONFIG(statustip)
        self.actionRecent_File.setText(QCoreApplication.translate("MainWindow", u"Recent File 01", None))
        self.actionRecent_File_02.setText(QCoreApplication.translate("MainWindow", u"Recent File 02", None))
        self.actionRecent_File_03.setText(QCoreApplication.translate("MainWindow", u"Recent File 03", None))
        self.actionMode.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
#if QT_CONFIG(tooltip)
        self.actionMode.setToolTip(QCoreApplication.translate("MainWindow", u"Mode", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionMode.setStatusTip(QCoreApplication.translate("MainWindow", u"View Mode Switch", None))
#endif // QT_CONFIG(statustip)
        self.actionObjects.setText(QCoreApplication.translate("MainWindow", u"Objects", None))
        self.actionParameters.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.actionData_Spreadsheet.setText(QCoreApplication.translate("MainWindow", u"Data Spreadsheet", None))
        self.actionOutput_Log.setText(QCoreApplication.translate("MainWindow", u"Output Log", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
#if QT_CONFIG(tooltip)
        self.actionFile.setToolTip(QCoreApplication.translate("MainWindow", u"File", None))
#endif // QT_CONFIG(tooltip)
        self.actionlogo.setText("")
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
#if QT_CONFIG(tooltip)
        self.actionEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Edit", None))
#endif // QT_CONFIG(tooltip)
        self.actionView.setText(QCoreApplication.translate("MainWindow", u"View", None))
#if QT_CONFIG(tooltip)
        self.actionView.setToolTip(QCoreApplication.translate("MainWindow", u"File", None))
#endif // QT_CONFIG(tooltip)
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionWindow.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionMaximize.setText(QCoreApplication.translate("MainWindow", u"Maximize", None))
        self.actionMinimize.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionOpen_2.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen_3.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(statustip)
        self.centralwidget.setStatusTip(QCoreApplication.translate("MainWindow", u"Node Graph", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"[ Node Graph ]", None))
        self.ToolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
#if QT_CONFIG(statustip)
        self.ToolBar.setStatusTip(QCoreApplication.translate("MainWindow", u"Tool Bar", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.dockWidget.setStatusTip(QCoreApplication.translate("MainWindow", u"Object Tree", None))
#endif // QT_CONFIG(statustip)
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"Objects", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"[ Object Tree ]", None))
#if QT_CONFIG(statustip)
        self.dockWidget_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Node Parameters", None))
#endif // QT_CONFIG(statustip)
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"[ Node Parameters ]", None))
#if QT_CONFIG(statustip)
        self.dockWidget_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Output Log", None))
#endif // QT_CONFIG(statustip)
        self.dockWidget_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"[ Logging Output ]", None))
#if QT_CONFIG(statustip)
        self.dockWidget_4.setStatusTip(QCoreApplication.translate("MainWindow", u"Data Spreadsheet", None))
#endif // QT_CONFIG(statustip)
        self.dockWidget_4.setWindowTitle(QCoreApplication.translate("MainWindow", u"Data ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"[ Data Spreadsheet ]", None))
        self.RightToolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

