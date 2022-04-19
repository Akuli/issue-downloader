from PyQt5 import QtCore

class DashboardB(QtCore.QObject):
    pass
class DashboardA(QtCore.QObject):
    pass

def f() -> DashboardA:
    return DashboardB()
