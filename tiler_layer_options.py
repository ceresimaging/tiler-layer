from qgis.PyQt.QtWidgets import QFormLayout, QLineEdit, QLabel
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

        tilerLabel = QLabel("Tiler Base URL")
        self.tiler = QLineEdit(
            self.settings.value("tiler_layer/tiler", "https://tile.ceresimaging.net")
        )
        apiLabel = QLabel("API Base URL")
        self.api = QLineEdit(
            self.settings.value("tiler_layer/api", "https://works.ceresimaging.net")
        )
        tokenLabel = QLabel("API Token")
        self.token = QLineEdit(self.settings.value("tiler_layer/token"))

        layout = QFormLayout()

        layout.addRow(tilerLabel, self.tiler)
        layout.addRow(apiLabel, self.api)
        layout.addRow(tokenLabel, self.token)

        self.setLayout(layout)

    def apply(self):
        self.settings.setValue("tiler_layer/tiler", self.tiler.text())
        self.settings.setValue("tiler_layer/api", self.api.text())
        self.settings.setValue("tiler_layer/token", self.token.text())
