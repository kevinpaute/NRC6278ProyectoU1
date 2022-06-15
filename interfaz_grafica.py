from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1102, 847)
        icon = QIcon()
        icon.addFile(u"../../../../../../../../Downloads/3310748.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1101, 851))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 0);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(30, 140, 1041, 631))
        self.textBrowser_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 40, 561, 71))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(680, 30, 201, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 470, 1021, 301))
        font3 = QFont()
        font3.setPointSize(13)
        self.textBrowser.setFont(font3)
        self.textBrowser.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.tabla_rest = QTableWidget(self.tab_2)
        if (self.tabla_rest.columnCount() < 2):
            self.tabla_rest.setColumnCount(2)
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font4);
        __qtablewidgetitem.setBackground(QColor(38, 185, 173));
        self.tabla_rest.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        __qtablewidgetitem1.setBackground(QColor(38, 185, 173));
        self.tabla_rest.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tabla_rest.rowCount() < 26):
            self.tabla_rest.setRowCount(26)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(13, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(14, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(15, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(16, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(17, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(18, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(19, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(20, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(21, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(22, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(23, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(24, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_rest.setVerticalHeaderItem(25, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_rest.setItem(0, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_rest.setItem(0, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabla_rest.setItem(1, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabla_rest.setItem(1, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabla_rest.setItem(2, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tabla_rest.setItem(2, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabla_rest.setItem(3, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tabla_rest.setItem(3, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabla_rest.setItem(4, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tabla_rest.setItem(4, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tabla_rest.setItem(5, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tabla_rest.setItem(5, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tabla_rest.setItem(6, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tabla_rest.setItem(6, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tabla_rest.setItem(7, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tabla_rest.setItem(7, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tabla_rest.setItem(8, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tabla_rest.setItem(8, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tabla_rest.setItem(9, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tabla_rest.setItem(9, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tabla_rest.setItem(10, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tabla_rest.setItem(10, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tabla_rest.setItem(11, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tabla_rest.setItem(11, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tabla_rest.setItem(12, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tabla_rest.setItem(12, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tabla_rest.setItem(13, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tabla_rest.setItem(13, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tabla_rest.setItem(14, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tabla_rest.setItem(14, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tabla_rest.setItem(15, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tabla_rest.setItem(15, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tabla_rest.setItem(16, 0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tabla_rest.setItem(16, 1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tabla_rest.setItem(17, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tabla_rest.setItem(17, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tabla_rest.setItem(18, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tabla_rest.setItem(18, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tabla_rest.setItem(19, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tabla_rest.setItem(19, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tabla_rest.setItem(20, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tabla_rest.setItem(20, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tabla_rest.setItem(21, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tabla_rest.setItem(21, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tabla_rest.setItem(22, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tabla_rest.setItem(22, 1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tabla_rest.setItem(23, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tabla_rest.setItem(23, 1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tabla_rest.setItem(24, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tabla_rest.setItem(24, 1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tabla_rest.setItem(25, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tabla_rest.setItem(25, 1, __qtablewidgetitem79)
        self.tabla_rest.setObjectName(u"tabla_rest")
        self.tabla_rest.setGeometry(QRect(460, 60, 611, 341))
        self.tabla_rest.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.tabla_rest.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_rest.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabla_rest.horizontalHeader().setStretchLastSection(True)
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 50, 371, 301))
        self.widget.setStyleSheet(u"background-color: rgb(38, 185, 173);")
        self.btn_limpiar = QPushButton(self.widget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(140, 230, 91, 41))
        self.btn_limpiar.setStyleSheet(u"background-color: rgb(181, 169, 33);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 211, 41))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setWeight(50)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"olor: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(38, 185, 173);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 150, 241, 31))
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: rgb(0,0,0);\n"
"background-color: rgb(38, 185, 173);")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 230, 91, 41))
        self.pushButton.setStyleSheet(u"\n"
"background-color: rgb(0, 152, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.line_nodo2 = QLineEdit(self.widget)
        self.line_nodo2.setObjectName(u"line_nodo2")
        self.line_nodo2.setGeometry(QRect(240, 150, 101, 41))
        self.line_nodo2.setFont(font5)
        self.line_nodo2.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.line_nodo1 = QLineEdit(self.widget)
        self.line_nodo1.setObjectName(u"line_nodo1")
        self.line_nodo1.setGeometry(QRect(240, 90, 101, 41))
        self.line_nodo1.setFont(font5)
        self.line_nodo1.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.btn_salir = QPushButton(self.widget)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setGeometry(QRect(250, 230, 91, 41))
        self.btn_salir.setStyleSheet(u"background-color:rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Comic Sans MS\";")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 20, 251, 41))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"olor: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(38, 185, 173);")
        self.widget_3 = QWidget(self.tab_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(30, 430, 1041, 361))
        self.widget_3.setStyleSheet(u"background-color: rgb(38, 185, 173);")
        self.widget_2 = QWidget(self.tab_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(30, 399, 281, 81))
        self.widget_2.setStyleSheet(u"background-color: rgb(38, 182, 170);")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 261, 31))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(0,0,0);")
        self.tabWidget.addTab(self.tab_2, "")
        self.widget_3.raise_()
        self.widget_2.raise_()
        self.widget.raise_()
        self.label_4.raise_()
        self.textBrowser.raise_()
        self.tabla_rest.raise_()

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"B\u00fasqueda de restaurante preferido", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">El aplicativo tiene una secci\u00f2n llamada &quot;Recorrido Restaurante&quot;. Para usar este programa siga las siguientes instrucciones :</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1. Dar clic en la opci\u00f2n del men\u00f9"
                        " &quot;Recorrido Restaurante&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2. Para que funcione el programa debe ingresar un nodo inicial que representa el ID de la ubicacion en la que se encuentra usted actualmente. Solo se permite ingresar los IDs: 3, 6, 9, 15, 19, 24. Estos nodos representan los lugares de trabajo o estudio.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3. Ingresar el valor del nodo objetivo que"
                        " representa el ID del restaurante que desea dirigirse. Se permiten todos los nodos excepto los nodos: 3, 6, 9, 15, 24.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4. Para mostrar la mejor ruta que debe seguir para llegar a su restaurante deseado, debe dar clic en el bot\u00f2n &quot;Buscar ruta&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">5. La secci\u00f3n del lado derecho contiene una tabla donde muestra los n"
                        "odos, en este caso, identificadores de cada restaurante. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">6. La secci\u00f3n de en medio, muestra el recorrido realizado para ir al restaurante.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">7. La secci\u00f3n de abajo muestra la gr\u00e1fica del recorrido.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-size:12pt;\">5. En caso desea probar otro recorrido, dar clic en el bot\u00f2n &quot;Limpiar&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">6. Para salir del programa de clic en el bot\u00f2n &quot;Salir&quot;.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Bienvenido al Manual de Usuario", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Manual de Usuario", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Localizaciones", None))
        ___qtablewidgetitem = self.tabla_rest.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID (Nodo)", None));
        ___qtablewidgetitem1 = self.tabla_rest.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Restaurantes y Lugar de trabajo/estudio", None));

        __sortingEnabled = self.tabla_rest.isSortingEnabled()
        self.tabla_rest.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tabla_rest.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem3 = self.tabla_rest.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"McDonald's\ud83c\udf54", None));
        ___qtablewidgetitem4 = self.tabla_rest.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem5 = self.tabla_rest.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Pizzeria El Hornero\ud83c\udf55", None));
        ___qtablewidgetitem6 = self.tabla_rest.item(2, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem7 = self.tabla_rest.item(2, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Casa Bamb\u00fa\ud83c\udf71", None));
        ___qtablewidgetitem8 = self.tabla_rest.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem9 = self.tabla_rest.item(3, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"CNT\ud83c\udfe2", None));
        ___qtablewidgetitem10 = self.tabla_rest.item(4, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem11 = self.tabla_rest.item(4, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Donde Coco\ud83c\udf5b", None));
        ___qtablewidgetitem12 = self.tabla_rest.item(5, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"5", None));
        ___qtablewidgetitem13 = self.tabla_rest.item(5, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"La Cocina de Consuelo\ud83c\udf5a", None));
        ___qtablewidgetitem14 = self.tabla_rest.item(6, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"6", None));
        ___qtablewidgetitem15 = self.tabla_rest.item(6, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"Universidad PUCE\ud83c\udfec", None));
        ___qtablewidgetitem16 = self.tabla_rest.item(7, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"7", None));
        ___qtablewidgetitem17 = self.tabla_rest.item(7, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"Mandayan Chill & Fest\ud83c\udf72", None));
        ___qtablewidgetitem18 = self.tabla_rest.item(8, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"8", None));
        ___qtablewidgetitem19 = self.tabla_rest.item(8, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"Santo Moro Grill\ud83e\udd90", None));
        ___qtablewidgetitem20 = self.tabla_rest.item(9, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"9", None));
        ___qtablewidgetitem21 = self.tabla_rest.item(9, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"Universidad UTE\ud83c\udfec", None));
        ___qtablewidgetitem22 = self.tabla_rest.item(10, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"10", None));
        ___qtablewidgetitem23 = self.tabla_rest.item(10, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"Parrilladas Oh que rico\ud83e\udd53", None));
        ___qtablewidgetitem24 = self.tabla_rest.item(11, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"11", None));
        ___qtablewidgetitem25 = self.tabla_rest.item(11, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"Mr. Pincho\ud83e\udd53", None));
        ___qtablewidgetitem26 = self.tabla_rest.item(12, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"12", None));
        ___qtablewidgetitem27 = self.tabla_rest.item(12, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form", u"Margarita\ud83c\udf71", None));
        ___qtablewidgetitem28 = self.tabla_rest.item(13, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form", u"13", None));
        ___qtablewidgetitem29 = self.tabla_rest.item(13, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Form", u"KFC\ud83c\udf57\ud83c\udf5f", None));
        ___qtablewidgetitem30 = self.tabla_rest.item(14, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Form", u"14", None));
        ___qtablewidgetitem31 = self.tabla_rest.item(14, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Form", u"El Rinc\u00f3n del Che\ud83c\udf5a", None));
        ___qtablewidgetitem32 = self.tabla_rest.item(15, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Form", u"15", None));
        ___qtablewidgetitem33 = self.tabla_rest.item(15, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Form", u"Universidad ESPE\ud83c\udfec", None));
        ___qtablewidgetitem34 = self.tabla_rest.item(16, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Form", u"16", None));
        ___qtablewidgetitem35 = self.tabla_rest.item(16, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Form", u"Conchal Chabelita\ud83e\udd90", None));
        ___qtablewidgetitem36 = self.tabla_rest.item(17, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Form", u"17", None));
        ___qtablewidgetitem37 = self.tabla_rest.item(17, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Form", u"El Menestron\ud83c\udf5b", None));
        ___qtablewidgetitem38 = self.tabla_rest.item(18, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Form", u"18", None));
        ___qtablewidgetitem39 = self.tabla_rest.item(18, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Form", u"Pizza Hurt\ud83c\udf55", None));
        ___qtablewidgetitem40 = self.tabla_rest.item(19, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Form", u"19", None));
        ___qtablewidgetitem41 = self.tabla_rest.item(19, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Form", u"Municipio\ud83c\udfe2", None));
        ___qtablewidgetitem42 = self.tabla_rest.item(20, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Form", u"20", None));
        ___qtablewidgetitem43 = self.tabla_rest.item(20, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Form", u"La Cuchara Brava\ud83c\udf72", None));
        ___qtablewidgetitem44 = self.tabla_rest.item(21, 0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Form", u"21", None));
        ___qtablewidgetitem45 = self.tabla_rest.item(21, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Form", u"Legends Food & Drinks \ud83c\udf5f", None));
        ___qtablewidgetitem46 = self.tabla_rest.item(22, 0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Form", u"22", None));
        ___qtablewidgetitem47 = self.tabla_rest.item(22, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Form", u"Super Pollo\ud83c\udf57", None));
        ___qtablewidgetitem48 = self.tabla_rest.item(23, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Form", u"23", None));
        ___qtablewidgetitem49 = self.tabla_rest.item(23, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Form", u"Papa John's Pizza\ud83c\udf5f", None));
        ___qtablewidgetitem50 = self.tabla_rest.item(24, 0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Form", u"24", None));
        ___qtablewidgetitem51 = self.tabla_rest.item(24, 1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Form", u"Supermercado AKI\ud83c\udfec", None));
        ___qtablewidgetitem52 = self.tabla_rest.item(25, 0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Form", u"25", None));
        ___qtablewidgetitem53 = self.tabla_rest.item(25, 1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Form", u"La Pizzeria\ud83c\udf55", None));
        self.tabla_rest.setSortingEnabled(__sortingEnabled)

        self.btn_limpiar.setText(QCoreApplication.translate("Form", u"Limpiar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ingrese su ubicaci\u00f3n:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ingrese el restaurante:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.line_nodo2.setText("")
        self.line_nodo1.setText("")
        self.btn_salir.setText(QCoreApplication.translate("Form", u"Salir", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Datos para el recorrido", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Ruta para ir al restaurante:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Recorrido Restaurante", None))
    # retranslateUi

