# -*- coding: utf-8-unix; -*-

# Copyright 2016 Dana Scott

# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved. This file is offered as-is,
# without any warranty.

Description
"""""""""""

A Python library to parse command line options.

Installation
""""""""""""

::

    pip install clops

Usage
"""""

::

    #! /usr/bin/env python3
    """Sample module docstring.

    Args:
        foo: The number of foos.
        bar: The number of bars.
        baz: The number of bazs.

    """
    from clops import cli


    _defaults = {
        foo: 1,
        bar: 2,
        baz: 3,
    }

    @cli.UpdateDict(_defaults, __doc__)
    def main():
        pass


    if __name__ == '__main__':
        main()
