#!/usr/bin/env python3
# display a tiled image from tileset with PyQt
import os
import tarfile
from PyQt5 import QtGui, QtCore, QtWidgets
from fgmk import Tile, actionDialog, Editor_MainWindow_Menus, game_server, fifl, TileCharaset, Charas, gameInit, current_project
from fgmk import  paletteWdgt, ToolsWdgt, EventsWdgt, LayerWdgt, actionsWdgt, MapExplorerWdgt, getdata, mapfile, TileSet, gameInit, configure_project
from fgmk.flowlayout import FlowLayout as FlowLayout


COLISIONLAYER = 3
EVENTSLAYER = 4

firstClickX = None
firstClickY = None


class MapWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.Grid = QtWidgets.QGridLayout(self)

        self.Grid.setHorizontalSpacing(0)
        self.Grid.setVerticalSpacing(0)
        self.Grid.setSpacing(0)
        self.Grid.setContentsMargins(0, 0, 0, 0)

        self.parent = parent

        self.TileWidth = 0
        self.TileHeight = 0
        self.myScale = 2
        self.currentTile = 5
        self.currentLayer = 0

        self.currentEvent = 1
        self.currentColision = 1

        self.TileList = []

        self.DrawMap(parent)

    def Rescale(self, scale=None):
        if(scale != None):
            self.myScale = scale

        for iy in range(self.TileHeight):
            for jx in range(self.TileWidth):
                self.TileList[iy][jx].Rescale(
                    self.parent.myTileSet.tileset, self.myScale)

        self.resize(self.TileWidth * self.parent.myTileSet.boxsize * self.myScale,
                    self.TileHeight * self.parent.myTileSet.boxsize * self.myScale)

        self.parent.myCharasPalWidget.reinit()

    def DrawMap(self, parent):
        # self.setUpdatesEnabled(False)
        self.setVisible(False)
        LayersMapTiles = parent.myMap.LayersMapTiles

        self.TileHeight = len(LayersMapTiles[0])
        self.TileWidth = len(LayersMapTiles[0][0])

        if len(self.TileList) > 1:
            for collum in self.TileList:
                for wdgt in collum:
                    wdgt.deleteLater()
                    wdgt = None
            self.TileList = []

        # get the background numbers and use to get the tiles
        for iy in range(self.TileHeight):
            self.TileList.append([])
            for jx in range(self.TileWidth):

                self.TileList[iy].append(Tile.QTile(self))
                self.Grid.addWidget(self.TileList[iy][jx], iy, jx)
                self.TileList[iy][jx].initTile(
                    parent.myTileSet.tileset, jx, iy, parent.myTileSet.boxsize, LayersMapTiles[:, iy, jx], self.myScale)
                self.TileList[iy][jx].clicked.connect(self.TileInMapClicked)
                self.TileList[iy][jx].rightClicked.connect(
                    self.TileInMapRightClicked)

        self.resize(self.TileWidth * parent.myTileSet.boxsize * self.myScale,
                    self.TileHeight * parent.myTileSet.boxsize * self.myScale)
        # self.setUpdatesEnabled(True)
        self.setVisible(True)
        # self.show()

    def TileInMapRightClicked(self):
        self.ClickedATileinMap(ToolsWdgt.rightClickTool)

    def TileInMapClicked(self):
        self.ClickedATileinMap(ToolsWdgt.leftClickTool)

    def ClickedATileinMap(self, theClickedTool):
        global firstClickX
        global firstClickY

        if theClickedTool == 0:
            # pen
            if(self.currentLayer == COLISIONLAYER):
                self.changeTileType(self.currentColision)
            elif(self.currentLayer == EVENTSLAYER):
                self.changeTileType(self.currentEvent)
                self.parent.myEventsWidget.updateEventsList()
            else:
                self.changeTileType(self.currentTile)

        elif theClickedTool == 1:
            # dropper
            if(self.currentLayer == COLISIONLAYER):
                self.parent.changeColisionCurrent(
                    self.sender().tileType[COLISIONLAYER])
            elif(self.currentLayer == EVENTSLAYER):
                self.parent.changeEventCurrent(
                    self.sender().tileType[EVENTSLAYER])
                self.parent.myEventsWidget.updateEventsList()
            else:
                self.parent.changeTileCurrent(
                    self.sender().tileType[self.currentLayer])

        elif theClickedTool == 2:
            # bucket
            if(self.currentLayer == COLISIONLAYER):
                self.toolBucketFill(self.currentColision)
            elif(self.currentLayer == EVENTSLAYER):
                self.toolBucketFill(self.currentEvent)
                self.parent.myEventsWidget.updateEventsList()
            else:
                self.toolBucketFill(self.currentTile)

        if theClickedTool == 3:
            # line
            if firstClickX is None:
                firstClickX = self.sender().tileX
                firstClickY = self.sender().tileY
            else:
                if(self.currentLayer == COLISIONLAYER):
                    self.toolLine(self.currentColision,
                                  firstClickX, firstClickY)
                elif(self.currentLayer == EVENTSLAYER):
                    self.toolLine(self.currentEvent, firstClickX, firstClickY)
                    self.parent.myEventsWidget.updateEventsList()
                else:
                    self.toolLine(self.currentTile, firstClickX, firstClickY)
                firstClickX = None
                firstClickY = None
        elif theClickedTool == 4:
            # rectangle
            if firstClickX is None:
                firstClickX = self.sender().tileX
                firstClickY = self.sender().tileY
            else:
                if(self.currentLayer == COLISIONLAYER):
                    self.toolRect(self.currentColision,
                                  firstClickX, firstClickY)
                elif(self.currentLayer == EVENTSLAYER):
                    self.toolRect(self.currentEvent, firstClickX, firstClickY)
                    self.parent.myEventsWidget.updateEventsList()
                else:
                    self.toolRect(self.currentTile, firstClickX, firstClickY)
                firstClickX = None
                firstClickY = None

        elif theClickedTool == 5:
            # charaplacer
            charaX = self.sender().tileX
            charaY = self.sender().tileY
            self.parent.myCharasPalWidget.addCharaAction((charaX, charaY))

        else:
            firstClickX = None
            firstClickY = None

    def changeTileType(self, changeTypeTo):
        command = Editor_MainWindow_Menus.CommandCTTileType(self.parent, self.sender(
        ), self.parent.myMap, self.parent.myTileSet.tileset, self.currentLayer, changeTypeTo, "change tile")
        self.parent.undoStack.push(command)

    def toolBucketFill(self, changeTypeTo):
        listToChange = mapfile.tileFill(self.sender().tileX, self.sender(
        ).tileY, self.parent.myMap.LayersMapTiles[self.currentLayer], changeTypeTo)
        command = Editor_MainWindow_Menus.CommandCGroupTType(self.parent, self.sender(
        ), self.parent.myMap, self.parent.myTileSet.tileset, self.currentLayer, changeTypeTo, listToChange, "bucket fill")
        self.parent.undoStack.push(command)

    def toolLine(self, changeTypeTo, firstX, firstY):
        listToChange = mapfile.tileLine(firstX, firstY, self.sender().tileX, self.sender(
        ).tileY, self.parent.myMap.LayersMapTiles[self.currentLayer], changeTypeTo)
        command = Editor_MainWindow_Menus.CommandCGroupTType(self.parent, self.sender(
        ), self.parent.myMap, self.parent.myTileSet.tileset, self.currentLayer, changeTypeTo, listToChange, "line")
        self.parent.undoStack.push(command)

    def toolRect(self, changeTypeTo, firstX, firstY):
        listToChange = mapfile.tileRect(firstX, firstY, self.sender().tileX, self.sender(
        ).tileY, self.parent.myMap.LayersMapTiles[self.currentLayer], changeTypeTo)
        command = Editor_MainWindow_Menus.CommandCGroupTType(self.parent, self.sender(
        ), self.parent.myMap, self.parent.myTileSet.tileset, self.currentLayer, changeTypeTo, listToChange, "rectangle")
        self.parent.undoStack.push(command)


class CharasPalWidget(QtWidgets.QWidget):
    def __init__(self, mapWdgt, pMap, parent=None, charaInstance=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.mapWdgt = mapWdgt
        self.pMap = pMap
        self.parent = parent

        self.vbox = QtWidgets.QVBoxLayout(self)

        self.charaslist = []
        self.myCharaSelector = Charas.CharaSelector(self, current_project.settings)
        self.vbox.addWidget(self.myCharaSelector)
        self.show()

    def reinit(self):
        for charaplaced in self.charaslist:
            charaplaced[2].stop()
            self.mapWdgt.Grid.removeWidget(charaplaced[2])
            charaplaced[2].deleteLater()

        self.myCharaSelector.update()
        self.charaslist = []

        charalist = self.pMap.getCharaList()
        if(charalist == [''] or not charalist):
            return

        for char in charalist:
            self.addCharaAction((char[1], char[2]), char[0], False)

    def addCharaAction(self, position=(0, 0), chara=None, onmap=True):
        if (chara == None):
            chara = self.myCharaSelector.getSelected()

        if (chara != None):
            scale = self.mapWdgt.myScale / 2.0
            if(self.positionEmpty(position)):
                item = Charas.MiniCharaTile(
                    None, current_project.settings, chara, (0, 0), scale)
                item.rightClicked.connect(self.autodelete)
                self.mapWdgt.Grid.addWidget(item, position[1], position[0])
                if(onmap):
                    self.pMap.insertChara(position[0], position[1], chara)
                self.charaslist.append((chara, position, item))

    def autodelete(self):
        item = self.sender()
        for charaplaced in self.charaslist:
            if(charaplaced[2] == item):
                charaplaced[2].stop()
                self.pMap.removeChara(charaplaced[1][0], charaplaced[1][1])
                self.mapWdgt.Grid.removeWidget(charaplaced[2])
                charaplaced[2].deleteLater()
                break

        self.charaslist.remove(charaplaced)

    def getCharasList(self):
        charaslist = []
        for charaplaced in self.charaslist:
            charaslist.append(charaplaced[0], charaplaced[
                              1][0], charaplaced[1][1])

        return charaslist

    def deletePosition(self, position=(0, 0)):
        for charaplaced in self.charaslist:
            if(charaplaced[1] == position):
                charaplaced[2].stop()
                self.mapWdgt.Grid.removeWidget(charaplaced[2])
                charaplaced[2].deleteLater()
                break

        self.charaslist.remove(charaplaced)

    def positionEmpty(self, position):
        for charaplaced in self.charaslist:
            if(charaplaced[1] == position):
                return False

        else:
            return True

    def getSelected(self):
        return self.myCharaSelector.getSelected()


class ExitFSWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.parent = parent
        self.VBox = QtWidgets.QVBoxLayout(self)
        self.ButtonExitFS = QtWidgets.QPushButton("exit\nfullscreen")
        self.ButtonExitFS.clicked.connect(self.ExitFS)
        self.VBox.addWidget(self.ButtonExitFS)
        self.setMaximumHeight(60)
        # self.setMinimumHeight(60)
        self.setMaximumWidth(90)
        # self.setMinimumWidth(84)

    def ExitFS(self):
        self.parent.fullscreenViewAction.toggle()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, filelist, **kwargs):
        super().__init__(None, **kwargs)

        #self.resize(1024, 768)

        self.undoStack = QtWidgets.QUndoStack(self)

        self.levelName = "newFile"
        current_project.settings["workingFile"] = self.levelName + ".map.json"

        self.myMap = mapfile.MapFormat()

        self.myMap.new(self.levelName, 10, 10)

        self.scrollArea = QtWidgets.QScrollArea(self)

        # get tileset file and split it in images that can be pointed through
        # array

        self.myTileSet = TileSet.TileSet(
            self.myMap.tileImage, self.myMap.palette)
        self.myMapWidget = MapWidget(self)

        self.scrollArea.setWidget(self.myMapWidget)
        self.setCentralWidget(self.scrollArea)

        self.FancyWindow(self)

        self.opemFileIfDropped(filelist)
        self.setAcceptDrops(True)

        self.settings = QtCore.QSettings("FGMK", "fgmkEditor")
        self.loadSettings()


    def changeLayerCurrent(self, changeTo):
        self.myMapWidget.currentLayer = changeTo
        self.myLayerWidget.changeLayerView(changeTo)

    def changeEventCurrent(self, changeTo):
        self.myMapWidget.currentEvent = changeTo
        self.myEventsWidget.eventSelectSpinbox.setValue(changeTo)
        self.changeLayerCurrent(EVENTSLAYER)

    def changeColisionCurrent(self, changeTo):
        self.myMapWidget.currentColision = changeTo
        self.myEventsWidget.setColisionValueView(changeTo)

    def changeTileCurrent(self, changeTo):
        self.myMapWidget.currentTile = changeTo
        self.myPaletteWidget.setImageCurrent(changeTo)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
            self.opemFileIfDropped(event.mimeData().urls()[0].toLocalFile())

        else:
            event.ignore()

    def opemFileIfDropped(self, filelist):
        if (isinstance(filelist, str)):
            if (".map.json" in filelist):
                self.openFileByName(filelist)

        else:
            matching = [s for s in filelist if ".map.json" in s]
            if len(matching) > 0:
                self.openFileByName(matching[0])

    def selectStartPosition(self):
        result = configure_project.selectStartingPosition(self)

        if result is None:
            return


        doSave = False
        if(result[1] != "this"):
            doSave = True
        else:
            if result[0]["World"]["initLevel"] not in result[0]["LevelsList"]:
                msg_msgbox = "The current level is not listed in LevelsList.\nMaybe you didn't save it or added to the list yet.\nProceed anyway?"
                reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                       msg_msgbox, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    doSave = True
            else:
                doSave = True

        if(doSave):
            gameInit.saveInitFile(current_project.settings["gamefolder"], result[0])

    def FancyWindow(self, parent=None):
        self.menubar = QtWidgets.QMenuBar(self)
        fileMenu = self.menubar.addMenu('&File')
        editMenu = self.menubar.addMenu('&Edit')
        current_projectectMenu = self.menubar.addMenu('&Project')
        fileMenu.addAction('&New', self.newFile, "Ctrl+N")
        fileMenu.addAction('&Open...', self.openFile, "Ctrl+O")
        fileMenu.addAction('&Save', self.saveFile, "Ctrl+S")
        fileMenu.addAction('&Save As...', self.saveFileAs, "Shift+Ctrl+S")
        fileMenu.addAction('&Export to JS...',
                           self.exportToJsAs, "Shift+Ctrl+E")
        fileMenu.addAction('&Exit', self.close, "Ctrl+Q")

        undoAction = self.undoStack.createUndoAction(self, self.tr("&Undo"))
        undoAction.setShortcuts(QtGui.QKeySequence.Undo)
        editMenu.addAction(undoAction)
        redoAction = self.undoStack.createRedoAction(self, self.tr("&Redo"))
        redoAction.setShortcuts(QtGui.QKeySequence.Redo)
        editMenu.addAction(redoAction)

        current_projectectMenu.addAction('New &Project', self.newProject, '')
        current_projectectMenu.addAction('Set starting &position...',
                              self.selectStartPosition, '')
        current_projectectMenu.addAction('Edit &charasets...', self.editCharasets, '')
        current_projectectMenu.addAction('Edit &charas...', self.editCharas, '')
        current_projectectMenu.addAction('Run Project', self.runServer, 'f5')

        self.viewMenu = self.menubar.addMenu('&View')

        self.myPaletteWidget = paletteWdgt.PaletteWidget(self, self.myTileSet)
        self.paletteDockWdgt = QtWidgets.QDockWidget("Palette", self)
        self.paletteDockWdgt.setObjectName("Palette")
        self.paletteDockWdgt.setWidget(self.myPaletteWidget)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.paletteDockWdgt)

        self.viewMenu.addAction(self.paletteDockWdgt.toggleViewAction())

        self.myCharasPalWidget = CharasPalWidget(
            self.myMapWidget, self.myMap, self)
        self.charasDockWdgt = QtWidgets.QDockWidget("Charas", self)
        self.charasDockWdgt.setObjectName("Charas")
        self.charasDockWdgt.setWidget(self.myCharasPalWidget)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.charasDockWdgt)
        self.tabifyDockWidget(self.charasDockWdgt, self.paletteDockWdgt)

        self.viewMenu.addAction(self.charasDockWdgt.toggleViewAction())

        self.myLayerWidget = LayerWdgt.LayerWidget(self)
        self.layerDockWdgt = QtWidgets.QDockWidget("Layers", self)
        self.layerDockWdgt.setObjectName("Layers")
        self.layerDockWdgt.setWidget(self.myLayerWidget)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.layerDockWdgt)

        self.viewMenu.addAction(self.layerDockWdgt.toggleViewAction())

        self.myToolsWidget = ToolsWdgt.ToolsWidget(self)
        self.toolsDockWdgt = QtWidgets.QDockWidget("Tool", self)
        self.toolsDockWdgt.setObjectName("Tool")
        self.toolsDockWdgt.setWidget(self.myToolsWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.toolsDockWdgt)

        self.viewMenu.addAction(self.toolsDockWdgt.toggleViewAction())

        self.myEventsWidget = EventsWdgt.EventsWidget(self.myMap, self)
        self.eventsDockWdgt = QtWidgets.QDockWidget("Events", self)
        self.eventsDockWdgt.setObjectName("Events")
        self.eventsDockWdgt.setWidget(self.myEventsWidget)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.eventsDockWdgt)

        self.viewMenu.addAction(self.eventsDockWdgt.toggleViewAction())

        self.myMapExplorerWidget = MapExplorerWdgt.MapExplorerWidget(self)
        self.myMapExplorerWidget.mapOpened.connect(self.openFromExplorer)
        self.mapExplorerDockWdgt = QtWidgets.QDockWidget("Map Explorer", self)
        self.mapExplorerDockWdgt.setObjectName("MapExplorer")
        self.mapExplorerDockWdgt.setWidget(self.myMapExplorerWidget)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.mapExplorerDockWdgt)

        self.viewMenu.addAction(self.mapExplorerDockWdgt.toggleViewAction())

        self.viewMenu.addSeparator()

        self.zoom05xViewAction = QtWidgets.QAction(
            'Zoom 0.5x', self.viewMenu, checkable=True)
        self.viewMenu.addAction(self.zoom05xViewAction)
        self.zoom05xViewAction.triggered.connect(self.changeZoom05x)

        self.zoom1xViewAction = QtWidgets.QAction(
            'Zoom 1x', self.viewMenu, checkable=True)
        self.viewMenu.addAction(self.zoom1xViewAction)
        self.zoom1xViewAction.triggered.connect(self.changeZoom1x)

        self.zoom2xViewAction = QtWidgets.QAction(
            'Zoom 2x', self.viewMenu, checkable=True)
        self.viewMenu.addAction(self.zoom2xViewAction)
        self.zoom2xViewAction.setShortcut(
            QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_0))
        self.zoom2xViewAction.triggered.connect(self.changeZoom2x)

        self.zoom4xViewAction = QtWidgets.QAction(
            'Zoom 4x', self.viewMenu, checkable=True)
        self.viewMenu.addAction(self.zoom4xViewAction)
        self.zoom4xViewAction.triggered.connect(self.changeZoom4x)

        self.zoomInAction = QtWidgets.QAction(
            'Zoom In', self.viewMenu, checkable=False)
        self.zoomInAction.setShortcut(QtGui.QKeySequence.ZoomIn)
        self.viewMenu.addAction(self.zoomInAction)
        self.zoomInAction.triggered.connect(self.zoomIn)

        self.zoomOutAction = QtWidgets.QAction(
            'Zoom Out', self.viewMenu, checkable=False)
        self.zoomOutAction.setShortcut(QtGui.QKeySequence.ZoomOut)
        self.viewMenu.addAction(self.zoomOutAction)
        self.zoomOutAction.triggered.connect(self.zoomOut)

        self.viewMenu.addSeparator()

        self.gridViewAction = QtWidgets.QAction(
            'grid', self.viewMenu, checkable=True)
        self.viewMenu.addAction(self.gridViewAction)
        self.gridViewAction.changed.connect(self.changeGridMargin)

        self.myExitFSWidget = ExitFSWidget(self)
        self.exitFSDockWdgt = QtWidgets.QDockWidget("", self)
        self.exitFSDockWdgt.setObjectName("ExitFullScreen")
        self.exitFSDockWdgt.setWidget(self.myExitFSWidget)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.exitFSDockWdgt)
        self.exitFSDockWdgt.hide()

        self.fullscreenViewAction = QtWidgets.QAction(
            'Fullscreen', self.viewMenu, checkable=True)
        self.fullscreenViewAction.setShortcut('f11')
        self.viewMenu.addAction(self.fullscreenViewAction)
        self.fullscreenViewAction.changed.connect(self.changeToFullscreen)

        helpMenu = self.menubar.addMenu('&Help')
        helpMenu.addAction('About...', self.helpAbout)

        self.setMenuBar(self.menubar)


    def changeZoomValue(self, zoomvalue):
        self.changeZoomViewActionChecked(zoomvalue)
        self.myMapWidget.Rescale(zoomvalue)

    def zoomIn(self):
        if(self.myMapWidget.myScale == 2):
            self.myMapWidget.Rescale(4)
            self.changeZoomViewActionChecked(4)
        elif(self.myMapWidget.myScale == 1):
            self.myMapWidget.Rescale(2)
            self.changeZoomViewActionChecked(2)
        elif(self.myMapWidget.myScale == 0.5):
            self.myMapWidget.Rescale(1)
            self.changeZoomViewActionChecked(1)

    def zoomOut(self):
        if(self.myMapWidget.myScale == 1):
            self.myMapWidget.Rescale(0.5)
            self.changeZoomViewActionChecked(0.5)
        elif(self.myMapWidget.myScale == 2):
            self.myMapWidget.Rescale(1)
            self.changeZoomViewActionChecked(1)
        elif(self.myMapWidget.myScale == 4):
            self.myMapWidget.Rescale(2)
            self.changeZoomViewActionChecked(2)

    def changeZoomViewActionChecked(self, zoomname):
            if(zoomname==0.5):
                self.zoom05xViewAction.setChecked(True)
            else:
                self.zoom05xViewAction.setChecked(False)
            if(zoomname==1):
                self.zoom1xViewAction.setChecked(True)
            else:
                self.zoom1xViewAction.setChecked(False)
            if(zoomname==2):
                self.zoom2xViewAction.setChecked(True)
            else:
                self.zoom2xViewAction.setChecked(False)
            if(zoomname==4):
                self.zoom4xViewAction.setChecked(True)
            else:
                self.zoom4xViewAction.setChecked(False)


    def changeZoom05x(self, checked):
        self.changeZoomValue(0.5)

    def changeZoom1x(self, checked):
        self.changeZoomValue(1)

    def changeZoom2x(self, checked):
        self.changeZoomValue(2)

    def changeZoom4x(self, checked):
        self.changeZoomValue(4)

    def editCharasets(self):
        myCharasetEditor = TileCharaset.CharasetEditorWidget(
            self, current_project.settings)
        if myCharasetEditor.exec_() == QtWidgets.QDialog.Accepted:
            print(myCharasetEditor)

    def editCharas(self):
        myCharasEditor = Charas.CharaEditor(self, current_project.settings)
        if myCharasEditor.exec_() == QtWidgets.QDialog.Accepted:
            print(myCharasEditor)

    def changeToFullscreen(self):
        if self.fullscreenViewAction.isChecked():
            self.showFullScreen()
            self.exitFSDockWdgt.show()
        else:
            self.showNormal()
            self.exitFSDockWdgt.hide()

    def changeGridMargin(self):
        bxsz = self.myTileSet.boxsize
        if self.gridViewAction.isChecked() is True:
            self.myMapWidget.Grid.setHorizontalSpacing(1)
            self.myMapWidget.Grid.setVerticalSpacing(1)
            self.myMapWidget.resize(self.myMapWidget.TileWidth * (bxsz * self.myMapWidget.myScale + 1) - 1,
                                    self.myMapWidget.TileHeight * (bxsz * self.myMapWidget.myScale + 1) - 1)
        else:
            self.myMapWidget.Grid.setHorizontalSpacing(0)
            self.myMapWidget.Grid.setVerticalSpacing(0)
            self.myMapWidget.resize(self.myMapWidget.TileWidth * bxsz * self.myMapWidget.myScale,
                                    self.myMapWidget.TileHeight * bxsz * self.myMapWidget.myScale)
        self.myMapWidget.show()

    def openFromExplorer(self):
        testMap = mapfile.MapFormat()
        testMap.load(current_project.settings["workingFile"])
        acceptOpen = False
        if not self.myMap.isEqualMap(testMap):

            quit_msg = "Do you want to save changes?"
            reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)

            if reply == QtWidgets.QMessageBox.Yes:
                acceptOpen=True
                self.saveFile()
            elif reply == QtWidgets.QMessageBox.No:
                acceptOpen=True
            else:
                return
        else:
            acceptOpen = True

        if acceptOpen:
            mapfilename = self.myMapExplorerWidget.mapForOpen
            gamefolder = os.path.abspath(current_project.settings["gamefolder"])
            filetopen = os.path.join(str(gamefolder), fifl.LEVELS, mapfilename)
            self.openFileByName(filetopen)


    def runServer(self):
        game_server.servePage(os.path.abspath(current_project.settings["gamefolder"]))

    def newProject(self):
        myNewProjectDialog = Editor_MainWindow_Menus.newProject(self)
        if myNewProjectDialog.exec_() == QtWidgets.QDialog.Accepted:
            returnedNFD = myNewProjectDialog.getValue()
            self.__newProject(returnedNFD)

    def __newProject(self, returnedNFD):
        import shutil

        current_projectectPath = os.path.join(
            str(returnedNFD["baseFolder"]), str(returnedNFD["name"]))
        current_project.settings["basefolder"] = str(returnedNFD["baseFolder"])
        current_project.settings["gamefolder"] = current_projectectPath
        current_project.settings["gamename"] = str(returnedNFD["name"])
        os.mkdir(current_projectectPath)
        tar = tarfile.open(getdata.path("basegame.tar.gz"))
        tar.extractall(current_projectectPath)
        tar.close()
        initfile = gameInit.openInitFile(current_project.settings["gamefolder"])
        levellist = initfile["LevelsList"]
        startlevel = initfile['World']['initLevel']
        levelfile = levellist[startlevel]
        self.openFileByName(os.path.join(current_project.settings["gamefolder"],fifl.LEVELS,levelfile))

    def newFile(self):
        myNewFileDialog = Editor_MainWindow_Menus.newFile(self)
        if myNewFileDialog.exec_() == QtWidgets.QDialog.Accepted:
            returnedNFD = myNewFileDialog.getValue()
            self.__newFile(returnedNFD)

    def __newFile(self, returnedNFD):
        current_project.settings["gamefolder"] = str(returnedNFD["gameFolder"])
        self.levelName = str(returnedNFD["name"])
        current_project.settings["workingFile"] = os.path.join(
            current_project.settings["gamefolder"], fifl.LEVELS, self.levelName + ".map.json")
        self.setWindowTitle(current_project.settings["workingFile"])
        self.myMap.new(self.levelName, returnedNFD[
                       "width"], returnedNFD["height"])
        self.myTileSet = TileSet.TileSet(os.path.join(
            current_project.settings["gamefolder"], self.myMap.tileImage), self.myMap.palette)
        self.myMapWidget.DrawMap(self)
        self.gridViewAction.setChecked(False)  # gambiarra
        self.myPaletteWidget.drawPalette(self.myTileSet)
        self.myEventsWidget.updateEventsList()
        self.myCharasPalWidget.reinit()
        self.myMapExplorerWidget.reloadInitFile()
        self.undoStack.clear()

    def saveFile(self):
        filename = current_project.settings["workingFile"]

        if filename != "":
            self.myMap.save(filename)

            if gameInit.regenerateLevelList():
                self.myMapExplorerWidget.reloadInitFile()


    def saveFileAs(self):
        filename, extension = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save File', os.path.expanduser("~"), 'JSON Game Level (*.map.json)')

        if filename[0] != "":
            if filename[-9:] != '.map.json':
                filename += '.map.json'

            current_project.settings["workingFile"] = filename
            self.myMap.save(current_project.settings["workingFile"])

            if gameInit.regenerateLevelList():
                self.myMapExplorerWidget.reloadInitFile()

    def exportToJsAs(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save File', os.path.expanduser("~"), 'JS Game Level (*.js)')

        if filename[0] != "":
            if filename[-3:] != '.js':
                filename += '.js'

            current_project.settings["workingFile"] = filename
            self.myMap.exportJS(current_project.settings["workingFile"])

    def openFileByName(self, filename):
        if(filename=="newFile.map.json"):
            return

        if os.path.isfile(filename):
            current_project.settings["gamefolder"] = os.path.abspath(
                os.path.join(os.path.dirname(str(filename)), "../../"))
            current_project.settings["workingFile"] = filename
            self.setWindowTitle(current_project.settings["workingFile"])
            self.myMap.load(current_project.settings["workingFile"])
            self.myTileSet = TileSet.TileSet(os.path.join(
                current_project.settings["gamefolder"], self.myMap.tileImage), self.myMap.palette)
            self.myMapWidget.DrawMap(self)
            self.gridViewAction.setChecked(False)  # gambiarra
            self.undoStack.clear()
            self.myPaletteWidget.drawPalette(self.myTileSet)
            self.myEventsWidget.updateEventsList()
            self.myEventsWidget.deselectAll()
            self.myCharasPalWidget.reinit()
            gameInit.regenerateLevelList()
            self.myMapExplorerWidget.reloadInitFile()

    def openFile(self):
        if(current_project.settings["gamefolder"] == ""):
            current_project.settings["gamefolder"] = os.path.expanduser("~")
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', os.path.join(current_project.settings["gamefolder"], fifl.LEVELS), "JSON Level (*.map.json);;All Files (*)")[0]
        self.openFileByName(filename)

    def helpAbout(self):
        credits = "Made by Erico\nWith help from the internet.\nHigly based in Tsubasa's Redo, and inspired in Enterbrain's RPG Maker 2000.\nThanks Nintendo for making the SNES."
        QtWidgets.QMessageBox.about(self, "About...", credits)

    def closeEvent(self, event):
        if(os.path.isfile(current_project.settings["workingFile"])):
            testMap = mapfile.MapFormat()
            testMap.load(current_project.settings["workingFile"])
            if not self.myMap.isEqualMap(testMap):

                quit_msg = "Do you want to save changes?"
                reply = QtWidgets.QMessageBox.question(self, 'Message',
                                                       quit_msg, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)

                if reply == QtWidgets.QMessageBox.Yes:
                    event.accept()
                    self.saveFile()
                elif reply == QtWidgets.QMessageBox.No:
                    event.accept()
                else:
                    event.ignore()
        else:
            event.accept()

        self.saveSettings()

    def saveSettings(self):
        self.settings.beginGroup("MainWindow")
        self.settings.setValue("size", self.size());
        self.settings.setValue("pos", self.pos());
        self.settings.setValue("zoom", self.myMapWidget.myScale)
        self.settings.setValue("state", self.saveState())
        self.settings.endGroup();

        self.settings.beginGroup("Project")
        if(os.path.isfile(current_project.settings["workingFile"])):
            self.settings.setValue("workingFile", current_project.settings["workingFile"]);
        self.settings.endGroup();


    def loadSettings(self):
         self.settings.beginGroup("MainWindow");
         self.resize(self.settings.value("size", QtCore.QSize(1024, 768)));
         self.move(self.settings.value("pos", QtCore.QPoint(32,32)));
         self.changeZoomValue(float(self.settings.value("zoom", 2)))
         state = self.settings.value("state", QtCore.QByteArray(), type=QtCore.QByteArray)
         if state:
            self.restoreState(state)
         self.settings.endGroup();

         self.settings.beginGroup("Project")

         workingFile = self.settings.value("workingFile", self.levelName + ".map.json")
         if(os.path.isfile(workingFile)):
               self.openFileByName(workingFile)
         self.settings.endGroup();




def Icon():
    return QtGui.QPixmap(getdata.path('icon.png'))
