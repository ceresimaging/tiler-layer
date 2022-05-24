# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TilerLayer
                                 A QGIS plugin
 Ceres Tiler Layer Loader
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-05-12
        copyright            : (C) 2022 by Ceres Imaging
        email                : mmiranda@ceresimaging.net
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TilerLayer class from file TilerLayer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tiler_layer import TilerLayer

    return TilerLayer(iface)