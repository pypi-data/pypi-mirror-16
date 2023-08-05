=====
About
=====

This is a pure python implementation of FNV algorithm as specified in
http://isthe.com/chongo/tech/comp/fnv/.

Only works with Python 3.
And Python 2 is not planned to be supported.

Usage
=====

::

    $ pip install fnv

.. code:: python

    import fnv

    data = 'my data'
    fnv.hash(data, algorithm=fnv.fnv_1a, bits=64) # uses fnv.fnv_1a algorithm
    fnv.hash(data, bits=64) # fnv.fnv_1a is a default algorithm
    fnv.hash(data, algorithm=fnv.fnv, bits=64)
