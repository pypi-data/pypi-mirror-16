``imshow`` is a command-line utility for visualizing matrices. It is
essentially a wrapper for the ``matplotlib`` / MATLAB command of the
same name.

Usage
-----
.. code:: bash

    $ python -e 'import numpy; numpy.savetxt("array.txt", numpy.random.normal(size=(60, 60)))'
    $ imshow array.txt

produces the file ``array.png`` containing an image of a random square
matrix with 60 entries per side.

.. figure:: https://terhorst.github.io/imshow/examples/array.png

    Example of default output.

The input file ``array.txt`` should readable by ``numpy.loadtxt()``, i.e. 
be a space-delimited square matrix.

The default output name ``array.png`` can be overridden by specifying
a second argument. The extension of the output file name controls the
output format.

.. code:: bash

    $ imshow array.txt array.jpg

.. figure:: https://terhorst.github.io/imshow/examples/array.jpg

    The same array in JPEG format.

Several options, detailed in ``imshow -h``, control the appearance of
the plot.

.. code:: bash

    $ imshow -g -b array.txt array.2.png

.. figure:: https://terhorst.github.io/imshow/examples/array.2.png

    The same array, with a grid and colormap added.

Requirements
------------
Numpy and ``matplotlib``.

Author
------
Jonathan Terhorst <terhorst@gmail.com>
