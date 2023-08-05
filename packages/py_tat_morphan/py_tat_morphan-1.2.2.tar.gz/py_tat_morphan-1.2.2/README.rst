Morphological Analyser of Tatar language
========================================

Morphological Parser of Tatar language. Uses HFST-tool.


To install:
-----------

$ pip install py_tat_morphan


To use lookup:
--------------

$ tat_morphan_lookup


To process text:
----------------

$ tat_morphan_process_text filename


To use as python module:
------------------------

>>> from py_tat_morphan.morphan import Morphan
>>> morphan = Morphan
>>> print(morphan.analyse('урманнарга'))
>>> print(morphan.lemma('урманнарга'))
>>> print(morphan.pos('урманнарга'))
>>> print(morphan.process_text('Без урманга барабыз.'))

For feedback:
-------------

ramil.gata@gmail.com