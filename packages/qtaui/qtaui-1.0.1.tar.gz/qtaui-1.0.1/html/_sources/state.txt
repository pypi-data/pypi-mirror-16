
Saving and restoring state
==========================

So that the user does not have to rebuild his own UI each time he launches the application, the :py:class:`QAUIManager` class supports state saving and restoring. The :py:meth:`QAUIManager.saveState()` method returns a `QByteArray` that can be saved in a `QSettings` object. After adding your frames to the manager, you can call :py:meth:`QAUIManager.restoreState()` method to restore the UI setup. :py:meth:`QAUIManager.restoreState()` should typically be called after you have restored your geometry.


.. code-block:: python

   from PySide import QtGui, QtCore
   from qtaui import QAUIManager, QAUILeafFrame, QAUIPos

   class MainWindow(QtGui.QMainWindow):
       def __init__(self):
           super(MainWindow, self).__init__()
	   self.manager = QAUIManager()
	   self.setCentralWidget(self.manager)

	   tab1 = self.manager.addFrame(QAUILeafFrame(self.manager, title='Frame #1'))
	   tab1.addFrame(QAUILeafFrame(self.manager, title='Frame #2'), QAUIPos.BOTTOM)
	   tab2 = self.manager.addFrame(QAUILeafFrame(self.manager, title='Frame #3'))
	   tab2.addFrame(QAUILeafFrame(self.manager, title='Frame #4'), QAUIPos.LEFT)

	   settings = QtCore.QSettings('net.jeromelaheurte', 'qtaui test')
	   if settings.contains('Geometry'):
	       self.restoreGeometry(settings.value('Geometry'))
	       self.manager.restoreState(settings.value('State'))
	   else:
               self.resize(600, 300)

       def closeEvent(self, event):
	   settings = QtCore.QSettings('net.jeromelaheurte', 'qtaui test')
	   settings.setValue('Geometry', self.saveGeometry())
	   settings.setValue('State', self.manager.saveState())
	   self.manager.shutdown()
	   event.accept()

   if __name__ == '__main__':
       app = QtGui.QApplication([])
       win = MainWindow()
       win.show()
       win.raise_()
       app.exec_()

The state includes the geometry of undocked frames. Internally, frames are identified by their `objectName` property if they have one, or an automatically generated index that depends on the order they were added to the manager. Thus, if you don't set (unique) `objectName` for your frames, you cannot change the order in which you add them to the manager. Additional frames (frames added to the manager that are not known to the state) will show up undocked. Bottom line: set unique `objectName` for each of your frame if you don't want to run into trouble.
