# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TilerLayerDockWidget
                                 A QGIS plugin
 Ceres Tiler Layer Loader
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-12
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Ceres Imaging
        email                : mmiranda@ceresimaging.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "tiler_layer_dockwidget_base.ui")
)


class TilerLayerDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(TilerLayerDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.hideAll()

        self.layer.addItem("")
        self.layer.addItem("Mosaic", "mosaic")
        self.layer.addItem("FieldGeo", "fieldgeo")
        self.layer.addItem("Imagery", "imagery")
        self.layer.addItem("PLI", "pli")

        self.mosaicType.addItem("Jenoptik", "Jenoptik")
        self.mosaicType.addItem("VNIR", "VNIR")

        self.layer.activated.connect(self.layerChanged)

        # only for testing
        # self.flight.setText("16073")
        # self.field.setText("76846")
        # self.overlay.setText("700eeb72-21dc-4834-9be7-22ac173387c0")
        # self.layer.setCurrentIndex(1)
        # self.overlay.show()
        # self.overlayLabel.show()

    def hideAll(self):
        self.flight.hide()
        self.flightLabel.hide()
        self.field.hide()
        self.fieldLabel.hide()
        self.mosaicType.hide()
        self.mosaicTypeLabel.hide()
        self.overlay.hide()
        self.overlayLabel.hide()

    def layerChanged(self, index):
        self.hideAll()
        layer = self.layer.currentData()
        if layer == "mosaic":
            self.flight.show()
            self.flightLabel.show()
            self.field.show()
            self.fieldLabel.show()
            self.mosaicType.show()
            self.mosaicTypeLabel.show()
        elif layer == "fieldgeo":
            self.field.show()
            self.fieldLabel.show()
        elif layer == "imagery":
            self.overlay.show()
            self.overlayLabel.show()
        elif layer == "pli":
            self.overlay.show()
            self.overlayLabel.show()

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
