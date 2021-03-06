 # -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.core import *
from qgis.gui import *

import sys
import traceback

from veriso.modules.complexcheck_base import ComplexCheckBase


def _translate(context, text, disambig):
    return QApplication.translate(context, text, disambig)


class ComplexCheck(ComplexCheckBase):

    def __init__(self, iface):
        super(ComplexCheck, self).__init__(iface)
        self.iface = iface

        self.root = QgsProject.instance().layerTreeRoot()

    def run(self):
        self.settings = QSettings("CatAIS", "VeriSO")
        project_id = self.settings.value("project/id")
        epsg = self.settings.value("project/epsg")
        # Für Multilingual-Legenden.
        locale = QSettings().value('locale/userLocale')[0:2]

        if not project_id:
            self.iface.messageBar().pushMessage(
                "Error",
                _translate("VeriSO_EE_wmsBBEO", "project_id not set",
                           None), level=Qgis.Critical, duration=5)
            return

        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            group = _translate("VeriSO_EE_wmsBBEO", "BBEOWMS", None)
            group += " (" + str(project_id) + ")"

            layer = {}
            layer["type"] = "wms"
            layer["group"] = group
            layer["title"] = _translate(
                "VeriSO_EE_wmsBBEO", "gesch. geol. Objekte", None)
            layer["url"] = "http://www.geoservice.apps.be.ch/geoservice/services/a4p/a4p_geologiewms_d_fk_s/MapServer/WMSServer?"
            layer["layers"] = "GEODB.GGO_GGOP"
            layer["format"] = "image/png"
            # layer["crs"] ="EPSG:21781"
            layer["sql"] = ""
            layer["style"] = ""
            vlayer = self.layer_loader.load(layer)
            layer = {}
            layer["type"] = "wms"
            layer["group"] = group
            layer["title"] = _translate("VeriSO_EE_wmsBBEO", "Lawinienverb.",
                                        None)
            layer["url"] = "http://www.geoservice.apps.be.ch/geoservice/services/a4p/a4p_umweltwms_d_fk_s/MapServer/WMSServer?"
            layer["layers"] = "GEODB.SCHBLAW_SBLAWP,GEODB.SCHBLAW_SBLAW"
            layer["format"] = "image/png"
            # layer["crs"] ="EPSG:21781"
            layer["sql"] = ""
            layer["style"] = ""
            vlayer = self.layer_loader.load(layer)
            layer = {}
            layer["type"] = "wms"
            layer["group"] = group
            layer["title"] = _translate("VeriSO_EE_wmsBBEO",
                                        "GBO (geschuetzte botanische...)",
                                        None)
            layer["url"] = "http://www.geoservice.apps.be.ch/geoservice/services/a4p/a4p_umweltwms_d_fk_s/MapServer/WMSServer?"
            layer["layers"] ="GEODB.GBO_GBOP,GEODB.GBO_GBOF"
            layer["format"] ="image/png"
            # layer["crs"] ="EPSG:21781"
            layer["sql"] = ""
            layer["style"] = ""
            vlayer = self.layer_loader.load(layer)
            layer = {}
            layer["type"] = "wms"
            layer["group"] = group
            layer["title"] = _translate("VeriSO_EE_wmsBBEO", "GN5", None)
            layer["url"] = "http://www.geoservice.apps.be.ch/geoservice/services/a4p/a4p_gewaesserwms_d_fk_s/MapServer/WMSServer?"
            layer["layers"] = "GEODB.GN5_GN5ROUTE_B,GEODB.GN5_DOLUNG,GEODB.GN5_GN5ROUTE"
            layer["format"] = "image/png"
            # layer["crs"] ="EPSG:21781"
            layer["sql"] = ""
            layer["style"] = ""
            vlayer = self.layer_loader.load(layer)
            layer = {}
            layer["type"] = "wms"
            layer["group"] = group
            layer["title"] = _translate("VeriSO_EE_wmsBBEO", "Wanderwege",
                                        None)
            layer["url"] = "http://www.geoservice.apps.be.ch/geoservice/services/a4p/a4p_transportwms_d_fk_s/MapServer/WMSServer?"
            layer["layers"] = "GEODB.WANDERNS_WEGE"
            layer["format"] = "image/png"
            # layer["crs"] ="EPSG:21781"
            layer["sql"] = ""
            layer["style"] = ""
            vlayer = self.layer_loader.load(layer)

        except Exception:
            QApplication.restoreOverrideCursor()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.iface.messageBar().pushMessage(
                "Error", str(traceback.format_exc(exc_traceback)),
                level=Qgis.Critical, duration=5)
        QApplication.restoreOverrideCursor()
