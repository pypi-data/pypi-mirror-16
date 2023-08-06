Python/NumPy implementation of IDL's rebin function.

See http://www.harrisgeospatial.com/docs/rebin.html.

The ``rebin`` function defined in this module first groups the cells of
the input array in tiles of specified size. Then, a reduction function
is applied to each tile, which is replaced by a single value. The
resulting array is returned: its dimensions are the number of tiles in
the input array.

Rebin is released under a BSD 3-clause license.

Rationale
---------

The input array, ``a`` is assumed to be *strided*. In other words, if ::

    a.strides = (s0, s1, ...),

then ::

    a[i0, i1, ...] = a[[s0*i0 + s1*i1 + ...]],

where ``[[...]]`` denotes the offset operator. To compute the output
array, we first create a tiled version of ``a``. The number of
dimensions of ``tiled`` is twice that of ``a``: for each index in ``a``,
``tiled`` has one *slow* index and one *fast* index ::

    tiled[i0, i1, ..., j0, j1, ...] = a[f0*i0 + j0, f1*i1 + j1, ...],

where ``factor=(f0, f1, ...)`` is the binning factor (size of the
tiles). Upon using the strides of ``a`` ::

    tiled[i0, i1, ..., j0, j1, ...] = a[[s0*f0*i0 + s1*f1*i1 + ... +
                                         s0*j0 + s1*j1 + ...]],

which shows that the strides of ``tiled`` are ::

    tiled.strides = (s0*f0, s1*f1, ..., s0, s1, ...).

In other words, ``tiled`` is a *view* of ``a`` with modified
strides. Restriding an array can be done with the ``as_strided``
function from ``numpy.lib.stride_tricks``. Then, the output array is
readily computed as follows ::

    out = func(tiled, axis = tuple(range(-a.ndim, 0)))

where reduction is carried out on the fast indices.

Boundary cases
--------------

When the dimensions of the input array are not integer multiples of the
dimensions of the tiles, the remainding rows/columns are simply
discarded. For example ::

    +--------+--------+--------+--------+----+
    |  1   1 |  2   2 |  3   3 |  4   4 |  5 |
    |  1   1 |  2   2 |  3   3 |  4   4 |  5 |
    +--------+--------+--------+--------+----+
    |  6   6 |  7   7 |  8   8 |  9   9 | 10 |
    |  6   6 |  7   7 |  8   8 |  9   9 | 10 |
    +--------+--------+--------+--------+----+
    | 11  11 | 12  12 | 13  13 | 14  14 | 15 |
    +--------+--------+--------+--------+----+

will produce ::

    +----+----+----+----+
    |  4 |  8 | 12 | 16 |
    +----+----+----+----+
    | 24 | 28 | 32 | 36 |
    +----+----+----+----+

for (2, 2) tiles and a *sum* reduction.



