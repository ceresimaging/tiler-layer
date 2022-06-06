from qgis.PyQt.QtWidgets import QFormLayout, QLineEdit, QLabel, QComboBox
from qgis.gui import QgsOptionsWidgetFactory, QgsOptionsPageWidget
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsSettings
from os import path


class TilerLayerOptionsFactory(QgsOptionsWidgetFactory):
    def __init__(self, plugin_dir):
        super().__init__()
        self.plugin_dir = plugin_dir

    def icon(self):
        return QIcon(path.join(self.plugin_dir, "icon.png"))

    def createWidget(self, parent):
        return ConfigOptionsPage(parent)


class ConfigOptionsPage(QgsOptionsPageWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.settings = QgsSettings()

        tilerLabel = QLabel("Tiler Environment")
        self.tiler = QComboBox()
        self.tiler.addItem("Development", "http://localhost:8888")
        self.tiler.addItem("Testing", "https://tiles-testing.ceresimaging.net")
        self.tiler.addItem("Production", "https://tiles.ceresimaging.net")
        self.tiler.setCurrentIndex(
            self.tiler.findData(self.settings.value("tiler_layer/tiler"))
        )

        apiLabel = QLabel("API Environment")
        self.api = QComboBox()
        self.api.addItem("Development", "http://localhost:8000")
        self.api.addItem("Staging", "https://works-staging.ceresimaging.net")
        self.api.addItem("Production", "https://works.ceresimaging.net")
        self.api.setCurrentIndex(
            self.api.findData(self.settings.value("tiler_layer/api"))
        )

        tokenLabel = QLabel("API Token")
        self.token = QLineEdit(self.settings.value("tiler_layer/token"))

        layout = QFormLayout()

        layout.addRow(tilerLabel, self.tiler)
        layout.addRow(apiLabel, self.api)
        layout.addRow(tokenLabel, self.token)

        self.setLayout(layout)

    def apply(self):
        self.settings.setValue("tiler_layer/tiler", self.tiler.currentData())
        self.settings.setValue("tiler_layer/api", self.api.currentData())
        self.settings.setValue("tiler_layer/token", self.token.text())
