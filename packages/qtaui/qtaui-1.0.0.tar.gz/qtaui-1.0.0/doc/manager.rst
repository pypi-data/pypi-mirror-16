
Frames and manager
==================

The basic building blocks of a qtaui based UI are frames, which are instances of :py:class:`QAUILeafFrame` (a QWidget really). The application must also hold an instance of :class:`QAUIManager`, which acts as a common ancestor and repository for frames. So the skeleton of a qtaui based application would be:

.. code-block:: python

   from PySide import QtGui
   from qtaui import QAUIManager, QAUILeafFrame

   class MainWindow(QtGui.QMainWindow):
       def __init__(self):
           super(MainWindow, self).__init__()
	   self.manager = QAUIManager()
	   self.setCentralWidget(self.manager)

	   # Let's add a simple empty frame
	   self.manager.addFrame(QAUILeafFrame(self.manager, title='I am a frame'))

   if __name__ == '__main__':
       app = QtGui.QApplication([])
       win = MainWindow()
       win.show()
       win.raise_()
       app.exec_()

Which will look pretty uninteresting:

.. image:: _static/singleframe.png
   :align: center

Frame position
--------------

the :py:meth:`QAUIManager.addFrame()` method takes an optional position argument, which value must be one of the constants defined in the :py:class:`QAUIPos` class. The default value is :py:attr:`QAUIPos.CENTER`, which means to add the frame as a new tab. Other values are:

:py:attr:`QAUIPos.LEFT`
    Add the frame as a new column in an horizontal splitter, to the left.

:py:attr:`QAUIPos.RIGHT`
    Add the frame as a new column in an horizontal splitter, to the right.

:py:attr:`QAUIPos.TOP`
    Add the frame as a new row in a vertical splitter, to the top.

:py:attr:`QAUIPos.BOTTOM`
    Add the frame as a new row in a vertical splitter, to the bottom.

:py:attr:`QAUIPos.FLOATING`
    Add the frame as a top-level widget.

The frame that will be replaced in the hierarchy by a splitter/tabbed interface is the one the :py:meth:`QAUILeafFrame.addFrame()` method is called on. So we can already build a not so simple interface:

  * Tab #1

    * Vertical splitter with frames 1 and 2

  * Tab #2

    * Horizontal splitter with frames 3 and 4

With the following code:

.. code-block:: python

   from PySide import QtGui
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

	   self.resize(600, 300)

   if __name__ == '__main__':
       app = QtGui.QApplication([])
       win = MainWindow()
       win.show()
       win.raise_()
       app.exec_()

.. image:: _static/tabsandsplitters.png
   :align: center

Undocking a frame
-----------------

Leaf frames and tabs have a title bar. The user can drag the frame from this titlebar in order to undock it, i.e. to make it into a top-level widget. The parent container of the undocked widget will be replaced by the appropriate one if this leads to it containing only one or zero frames; for instance a tabbed container will be replaced by a plain one, thus removing the tabs. Undocking the frame #4 in the previous example will lead to this:

.. image:: _static/undocked.png
   :align: center

When a frame is undocked, the frame itself emits a :py:meth:`QAUILeafFrame.undocked` signal and the manager emits a :py:meth:`QAUIManager.frameUndocked` signal. There are also :py:meth:`QAUILeafFrame.docked` and :py:meth:`QAUIManager.frameDocked` signals. See the :ref:`classref` for more information.

.. note::
  Since Qt does not exit the main event loop as long as there are visible top-level widgets, a convenience method of the :py:class:`QAUIManager` class allows you to hide all undocked frames at once; this must typically be called on program termination, from your main window:

  .. code-block:: python

         def closeEvent(self, event):
	     self.manager.shutdown()
	     event.accept()

Docking a frame
---------------

When the user is dragging an undocked frame around, the :py:class:`QAUIManager` goes into "drop" mode, which is a graphical representation of the UI hierarchy, with hints as to where the frame can be dropped in order to dock it:

.. image:: _static/drop.png
   :align: center

Each part of the hierarchy has five drop targets, each mapping to one of the positions defined in :py:class:`QAUIPos`.
