# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore, QtWidgets
from PIL import Image
from PIL.ImageQt import ImageQt

from fgmk import tMat, getdata, current_project, alpha_composite, tile_set


class QTile(QtWidgets.QLabel):
    def __init(self, parent):
        #super().__init__(parent)
        QtWidgets.QLabel.__init__(self, parent)

    tileType = []
    tileX = 0
    tileY = 0
    boxSize = 32

    clicked = QtCore.pyqtSignal()
    rightClicked = QtCore.pyqtSignal()
    doubleClicked = QtCore.pyqtSignal()

    def Rescale(self, tileset,  scale=1):
        self.scale = scale
        self.updateTileImageInMap(self.tileType[0], 0, tileset, self.scale)

    def initTile(self, tileset, x, y, boxSize, tileType, scale=1):
        self.tileType = tileType
        self.tileX = x
        self.tileY = y
        self.boxSize = boxSize
        self.scale = scale
        self.updateTileImageInMap(self.tileType[0], 0, tileset, self.scale)

    def updateTileImageInMap(self, ChangeTileType, layer, tileset,  scale=1):
        self.tileType[layer] = ChangeTileType
        self.scale = scale

        if(scale == 2):
            tempscale = 1
        elif(scale == 0.5):
            tempscale = 2
        else:
            tempscale = 0

        Composite = tile_set.clearTile.tileset[0][tempscale]
        try:
            for i in range(len(self.tileType) - 2):
                if(self.tileType[i]):
                    Composite = Image.alpha_composite(
                        Composite, tileset[self.tileType[i]][tempscale])
            if(self.tileType[i + 1]):
                Composite = Image.alpha_composite(Composite, tile_set.colisionSet.tileset[
                                                  self.tileType[i + 1]][tempscale])
            if(self.tileType[i + 2]):
                Composite = Image.alpha_composite(Composite, tile_set.eventSet.tileset[
                                                  self.tileType[i + 2]][tempscale])
        except:
            for i in range(len(self.tileType) - 2):
                if(self.tileType[i]):
                    Composite = alpha_composite.alpha_composite(
                        Composite, tileset[self.tileType[i]][tempscale])
            if(self.tileType[i + 1]):
                Composite = alpha_composite.alpha_composite(Composite, tile_set.colisionSet.tileset[
                                                 self.tileType[i + 1]][tempscale])
            if(self.tileType[i + 2]):
                Composite = alpha_composite.alpha_composite(Composite, tile_set.eventSet.tileset[
                                                 self.tileType[i + 2]][tempscale])

        if(scale != 1 and scale != 0.5 and scale != 2):
            Composite = Composite.resize(
                (int(self.boxSize * scale), int(self.boxSize * scale)), Image.NEAREST)

        Composite = Composite.resize(
            (int(self.boxSize * scale), int(self.boxSize * scale)), Image.NEAREST)

        pixmap = QtGui.QPixmap.fromImage(ImageQt(Composite))
        self.setPixmap(pixmap)

    def mousePressEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.rightClicked.emit()
        else:
            self.clicked.emit()

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()

    ##def wheelEvent(self, ev):
    #    self.emit(SIGNAL('scroll(int)'), ev.delta())
