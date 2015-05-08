import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class SarPlotUi(QMainWindow):

    def __init__(self):
        super(SarPlotUi, self).__init__()

        self.toolbar = self.create_tool_bar()
        self._set_window_view()

    def create_tool_bar(self):
        open_log_action = QAction(QIcon('icons/open.png'), 'Open', self)
        open_log_action.setShortcut('Ctrl+O')
        open_log_action.triggered.connect(qApp.quit)

        save_plots_action = QAction(QIcon('icons/save.png'), 'Export', self)
        save_plots_action.setShortcut('Ctrl+S')
        save_plots_action.triggered.connect(qApp.quit)

        toolbar = self.addToolBar('Open')
        toolbar.addAction(open_log_action)
        toolbar.addAction(save_plots_action)

        return toolbar

    def _set_window_view(self):
        self.setGeometry(200, 100, 800, 640)
        self.setWindowTitle('pulsar visualizer')


def plot():
    app = QApplication(sys.argv)
    wnd = SarPlotUi()
    wnd.show()

    return app.exec_()


if __name__ == '__main__':
    sys.exit(plot())