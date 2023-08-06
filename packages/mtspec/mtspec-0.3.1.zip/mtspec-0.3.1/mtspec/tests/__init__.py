#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de) and
    Moritz Beyreuther, 2010-2016
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import unittest

from . import test_multitaper, test_code_formatting


def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_multitaper.suite())
    suite.addTest(test_code_formatting.suite())
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
