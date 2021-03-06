import sys

from PySide import QtGui
from qtodotxt.ui.services.dialogs_service import DialogsService
from qtodotxt.ui.services.task_editor_service import TaskEditorService
from qtodotxt.ui.views import MainView
from qtodotxt.ui.controllers import MainController
from qtodotxt.ui.resource_manager import getIcon

def run():
    app = QtGui.QApplication(sys.argv)
    controller = _createController()
    icon = TrayIcon(controller)
    controller.show()
    app.exec_()
    sys.exit()

def _createController():
    window = MainView()
    dialogs_service = DialogsService(window, 'QTodoTxt')
    task_editor_service = TaskEditorService(window)
    return MainController(window, dialogs_service, task_editor_service)

class TrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, main_controller):
        self._controller = main_controller
        self._initIcon()
        self.show()

    def _initIcon(self):
        view = self._controller.getView()
        icon = getIcon('qtodotxt.ico')
        QtGui.QSystemTrayIcon.__init__(self, icon, view)
        self.activated.connect(self._onActivated)
        self.setToolTip('QTodoTxt')
    
    def _onActivated(self):
        self._controller._tasks_list_controller.createTask()
    
if __name__ == "__main__":
    run()
