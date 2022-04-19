gearIcon = QIcon(str('...'))
menuSettings: QMenu = self.menuBar().addMenu('&Tools')
actionSettings = menuSettings.addAction(gearIcon, '&Settings')
actionSettings.triggered.connect(self.showSettingsDialog)
