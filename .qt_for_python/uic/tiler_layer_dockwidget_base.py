# Form implementation generated from reading ui file '/Users/mmiranda/Projects/ceres/tiler-layer/zip_build/tiler_layer/tiler_layer_dockwidget_base.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TilerLayerDockWidgetBase(object):
    def setupUi(self, TilerLayerDockWidgetBase):
        TilerLayerDockWidgetBase.setObjectName("TilerLayerDockWidgetBase")
        TilerLayerDockWidgetBase.resize(305, 539)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setObjectName("formLayout")
        self.flightLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.flightLabel.setObjectName("flightLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.flightLabel)
        self.flight = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.flight.setObjectName("flight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.flight)
        self.mosaicTypeLabel = QtWidgets.QLabel(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mosaicTypeLabel.sizePolicy().hasHeightForWidth())
        self.mosaicTypeLabel.setSizePolicy(sizePolicy)
        self.mosaicTypeLabel.setObjectName("mosaicTypeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.mosaicTypeLabel)
        self.mosaicType = QtWidgets.QComboBox(self.dockWidgetContents)
        self.mosaicType.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mosaicType.sizePolicy().hasHeightForWidth())
        self.mosaicType.setSizePolicy(sizePolicy)
        self.mosaicType.setObjectName("mosaicType")
        self.mosaicType.addItem("")
        self.mosaicType.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.mosaicType)
        self.fieldLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.fieldLabel.setObjectName("fieldLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.fieldLabel)
        self.field = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.field.setText("")
        self.field.setObjectName("field")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.field)
        self.overlayLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.overlayLabel.setObjectName("overlayLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.overlayLabel)
        self.overlay = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.overlay.setText("")
        self.overlay.setObjectName("overlay")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.overlay)
        self.customerLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.customerLabel.setObjectName("customerLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.customerLabel)
        self.customer = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.customer.setObjectName("customer")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.customer)
        self.assetLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.assetLabel.setObjectName("assetLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.assetLabel)
        self.asset = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.asset.setObjectName("asset")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.asset)
        self.gridLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.gridLabel.setObjectName("gridLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.gridLabel)
        self.grid = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.grid.setText("")
        self.grid.setObjectName("grid")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.grid)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.extent = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.extent.setChecked(True)
        self.extent.setObjectName("extent")
        self.gridLayout.addWidget(self.extent, 3, 0, 1, 1)
        self.layerLayout = QtWidgets.QFormLayout()
        self.layerLayout.setObjectName("layerLayout")
        self.layer = QtWidgets.QComboBox(self.dockWidgetContents)
        self.layer.setObjectName("layer")
        self.layerLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.layer)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.layerLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.gridLayout.addLayout(self.layerLayout, 0, 0, 1, 1)
        self.load = QtWidgets.QPushButton(self.dockWidgetContents)
        self.load.setObjectName("load")
        self.gridLayout.addWidget(self.load, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        TilerLayerDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(TilerLayerDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(TilerLayerDockWidgetBase)

    def retranslateUi(self, TilerLayerDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        TilerLayerDockWidgetBase.setWindowTitle(_translate("TilerLayerDockWidgetBase", "Tiler Layer"))
        self.flightLabel.setText(_translate("TilerLayerDockWidgetBase", "Flight"))
        self.mosaicTypeLabel.setText(_translate("TilerLayerDockWidgetBase", "Type"))
        self.mosaicType.setItemText(0, _translate("TilerLayerDockWidgetBase", "Jenoptik"))
        self.mosaicType.setItemText(1, _translate("TilerLayerDockWidgetBase", "VNIR"))
        self.fieldLabel.setText(_translate("TilerLayerDockWidgetBase", "Field"))
        self.overlayLabel.setText(_translate("TilerLayerDockWidgetBase", "Overlay"))
        self.customerLabel.setText(_translate("TilerLayerDockWidgetBase", "Customer"))
        self.assetLabel.setText(_translate("TilerLayerDockWidgetBase", "Asset"))
        self.gridLabel.setText(_translate("TilerLayerDockWidgetBase", "Grid"))
        self.extent.setText(_translate("TilerLayerDockWidgetBase", "Set Exent to Layer"))
        self.label.setText(_translate("TilerLayerDockWidgetBase", "Layer"))
        self.load.setText(_translate("TilerLayerDockWidgetBase", "Load"))