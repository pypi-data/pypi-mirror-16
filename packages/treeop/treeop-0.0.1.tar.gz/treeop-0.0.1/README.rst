treeop
=========

collection of operations for nested dict, list and tuple.

Usage
-----

applyto
^^^^^^^
.. code:: python

    >>> apply(print, {"a": [1, 2], "b": [3, 4], level = 1)
    [1, 2]
    [3, 4]

    >>> apply(print, {"a": [1, 2], "b": [3, 4], level = 2)
    1
    2
    3
    4

mapto
^^^^^
.. code:: python

    >>> mapto(sum, {"a": [1, 2], "b": [3, 4], level = 1)
    {'a': 3, 'b': 7}

    >>> mapto(lambda x: 2 * x, {"a": [1, 2], "b": [3, 4], level = 2)
    {'a': [2, 4], 'b': [6, 8]}

transpose
^^^^^^^^^
.. code:: python

    >>> transpose({"a": [1, 2], "b": [3, 4], levels = [1, 0])
    [{"a": 1, "b": 3}, {"a": 2, "b", 4}]

License
-------

These codes are licensed under
`CC0 <https://creativecommons.org/publicdomain/zero/1.0/deed>`__.

Tips
----
