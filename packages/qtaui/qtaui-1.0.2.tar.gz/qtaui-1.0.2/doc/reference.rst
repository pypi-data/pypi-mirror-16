
.. _classref:

Class reference
===============

.. py:class:: QAUIPos

   This class is a placeholder for constants describing a position.

   .. py:attribute:: POS_CENTER

      Center position, meaning as a new tab

   .. py:attribute:: POS_LEFT

      Left position, meaning to the left of an horizontal splitter

   .. py:attribute:: POS_RIGHT

      Right position, meaning to the right of an horizontal splitter

   .. py:attribute:: POS_TOP

      Top position, meaning to the top of a vertical splitter

   .. py:attribute:: POS_BOTTOM

      Bottom position, meaning to the bottom of a vertical splitter

   .. py:attribute:: POS_FLOATING

      Floating position, meaning as a top-level widget


.. py:class:: QAUIManager

   This class acts as the common UI ancestor for frames. The constructor arguments are the same as for `QWidget`.

   .. py:staticmethod:: labelForTabs()

      Should return the label displayed to the user in drop mode for tabs frames. The string contains a 'title' format placeholder. The default value returned is "Tabs ({title})".

   .. py:staticmethod:: labelForSplitter(orientation)

      Should return the label displayed to the user in drop mode for splitter frames. The default value returned is "Horizontal splitter" if the `orientation` parameter is `QtCore.Qt.Horizontal`, and "Vertical splitter" if not.

   .. py:method:: shutdown()

      This method hides all undocked frames, so that the Qt main loop can exit after your main window closes. This is typically called from within an `onEvent` handler.

   .. py:method:: saveState()

      This returns a `QByteArray` containing an internal representation of the current UI state. Call `restoreState` with this value to restore the UI state.

   .. py:method:: restoreState(state)

      This restores a state returned by `saveState`.

   .. py:method:: addFrame(frame, position=QAUIPos.CENTER)

      Adds a frame as a child of the manager itself. See `QAUIPos` for possible values.

   .. py:method:: frameDocked(frame, parent, position)

      This is a Qt signal that is emitted when a frame has been docked by the user onto `parent` in position `position`.

   .. py:method:: frameUndocked(frame)

      This is a Qt signal that is emitted when a frame has been undocked by the user.

   .. py:method:: frameClosed(frame)

      This is a Qt signal that is emitted when a frame has been closed by the user.


.. py:class:: QAUILeafFrame

   This class is the one you should inherit from for your main UI child widgets, instead of `QWidget`. In addition to the regular `QWidget` arguments, the constructor may take a keyword argument 'title' of type Unicode string.

   .. py:method:: title()

      Returns the frame's title.

   .. py:method:: addFrame(frame, position=QAUIPos.CENTER)

      Adds a frame as a child of this frame. See `QAUIPos` for possible values.

   .. py:method:: undocked()

      This is a Qt signal that is emitted when the frame is undocked by the user.

   .. py:method:: docked(parent, position)

      This is a Qt signal that is emitted when the frame has been docked by the user onto `parent` into position `position`.

   .. py:method:: closed()

      This is a Qt signal that is emitted when the frame has been closed by the user.
