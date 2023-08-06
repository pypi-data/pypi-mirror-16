# -*- coding: utf-8 -*-
"""Test backwards compatibility with pre-release API.

.. note:: Because this sub-module works by monkey-patching the global
          ``datatest`` package, these tests should be run in a separate
          process.
"""
import unittest


class TestApiDev0(unittest.TestCase):
    def test_api_dev0(self):
        import datatest

        from datatest.__past__ import api_dev0  # <- MONKEY PATCH!!!

        self.assertTrue(hasattr(datatest, 'DataAssertionError'))

        # DataTest properties.
        self.assertTrue(hasattr(datatest.DataTestCase, 'subjectData'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'referenceData'))

        # DataTest allowances.
        self.assertTrue(hasattr(datatest.DataTestCase, 'allowSpecified'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'allowUnspecified'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'allowDeviationPercent'))

        # DataTest assertions.
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertColumnSet'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertColumnSubset'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertColumnSuperset'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertValueSet'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertValueSubset'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertValueSuperset'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertValueSum'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertValueCount'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertValueRegex'))
        self.assertTrue(hasattr(datatest.DataTestCase, 'assertValueNotRegex'))


if __name__ == '__main__':
    unittest.main()
else:
    raise Exception('This test must be run directly or as a subprocess.')
