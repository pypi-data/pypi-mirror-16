tktextext
==========

Module ``tktextext`` provides classes ``EnhancedText`` and ``TextFrame``.

``EnhancedText`` is subclass of ``tkinter.Text`` and adds

* possibility to make text read-only but keep text selectable
* several movement and editing aids (smart-tab, smart-home, etc)
* several useful helper methods.

``TextFrame`` is subclass of ``tkinter.ttk.Frame`` and can decorate ``TextFrame`` 
(or ``tkinter.Text``) with scrollbars and line numbers margin.

The module was initially developed for `Thonny, 
Python IDE for beginners <https://thonny.cs.ut.ee>`_ 