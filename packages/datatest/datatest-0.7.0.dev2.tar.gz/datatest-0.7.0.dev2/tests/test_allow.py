# -*- coding: utf-8 -*-
import inspect
from . import _unittest as unittest

from datatest import DataError
from datatest import Missing
from datatest import Extra
from datatest import Deviation
from datatest.allow import allow_iter
from datatest.allow import allow_each
from datatest.allow import allow_any
from datatest.allow import allow_extra
from datatest.allow import allow_missing
from datatest.allow import allow_only
from datatest.allow import allow_limit
from datatest.allow import allow_deviation
from datatest.allow import allow_percent_deviation


class TestAllowIter(unittest.TestCase):
    def test_function_all_bad(self):
        function = lambda iterable: iterable  # <- Rejects everything.
        in_diffs = [
            Extra('foo'),
            Extra('bar'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_iter(function, 'example allowance'):
                raise DataError('example error', in_diffs)

        rejected = cm.exception.differences
        self.assertEqual(rejected, in_diffs)

    def test_function_all_ok(self):
        function = lambda iterable: list()  # <- Accepts everything.

        with allow_iter(function, 'example allowance'):
            raise DataError('example error', [Missing('foo'), Missing('bar')])

    def test_function_some_ok(self):
        function = lambda iterable: (x for x in iterable if x.value != 'bar')
        in_diffs = [
            Missing('foo'),
            Missing('bar'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_iter(function, 'example allowance'):
                raise DataError('example error', in_diffs)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, [Missing('foo')])

    def test_kwds_all_bad(self):
        function = lambda iterable: list()  # <- Accepts everything.
        in_diffs = [
            Missing('foo', aaa='x', bbb='y'),
            Missing('bar', aaa='x', bbb='z'),
        ]
        with self.assertRaises(DataError) as cm:
            # Using keyword bbb='j' should reject all in_diffs.
            with allow_iter(function, 'example allowance', bbb='j'):
                raise DataError('example error', in_diffs)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, in_diffs)

    def test_kwds_all_ok(self):
        function = lambda iterable: list()  # <- Accepts everything.
        in_diffs = [
            Missing('foo', aaa='x', bbb='y'),
            Missing('bar', aaa='x', bbb='z'),
        ]
        # Using keyword aaa='x' should accept all in_diffs.
        with allow_iter(function, 'example allowance', aaa='x'):
            raise DataError('example error', in_diffs)

        # Using keyword bbb=['y', 'z'] should also accept all in_diffs.
        with allow_iter(function, 'example allowance', bbb=['y', 'z']):
            raise DataError('example error', in_diffs)

    def test_kwds_some_ok(self):
        function = lambda iterable: list()  # <- Accepts everything.
        in_diffs = [
            Missing('foo', aaa='x', bbb='y'),
            Missing('bar', aaa='x', bbb='z'),
        ]
        with self.assertRaises(DataError) as cm:
            # Keyword bbb='y' should reject second in_diffs element.
            with allow_iter(function, 'example allowance', bbb='y'):
                raise DataError('example error', in_diffs)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, [Missing('bar', aaa='x', bbb='z')])

    def test_no_exception(self):
        function = lambda iterable: list()  # <- Accepts everything.

        with self.assertRaises(AssertionError) as cm:
            with allow_iter(function):
                pass  # No exceptions raised

        exc = cm.exception
        self.assertEqual('No differences found: <lambda>', str(exc))


class TestAllowEach(unittest.TestCase):
    """Using allow_each() requires an element-wise function."""
    def test_allow_some(self):
        function = lambda x: x.value == 'bar'
        in_diffs = [
            Missing('foo'),
            Missing('bar'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_each(function, 'example allowance'):
                raise DataError('example error', in_diffs)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, [Missing('foo')])

    def test_allow_all(self):
        function = lambda x: isinstance(x, Missing)  # <- Allow only missing.

        with allow_each(function, 'example allowance'):
            raise DataError('example error', [Missing('xxx'), Missing('yyy')])

    def test_kwds(self):
        function = lambda x: True  # <- Accepts everything.
        in_diffs = [
            Missing('foo', aaa='x', bbb='y'),
            Missing('bar', aaa='x', bbb='z'),
        ]
        with self.assertRaises(DataError) as cm:
            # Keyword bbb='y' should reject second in_diffs element.
            with allow_each(function, 'example allowance', bbb='y'):
                raise DataError('example error', in_diffs)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, [Missing('bar', aaa='x', bbb='z')])

    def test_no_exception(self):
        function = lambda x: False  # <- Rejects everything.

        with self.assertRaises(AssertionError) as cm:
            with allow_each(function):
                pass  # No exceptions raised

        exc = cm.exception
        self.assertEqual('No differences found: <lambda>', str(exc))


class TestAllowAny(unittest.TestCase):
    """Test allow_any() behavior."""
    def test_kwds(self):
        in_diffs = [
            Extra('xxx', aaa='foo'),
            Extra('yyy', aaa='bar'),
            Missing('zzz', aaa='foo'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_any('example allowance', aaa='foo'):
                raise DataError('example error', in_diffs)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, [Extra('yyy', aaa='bar')])

    def test_no_kwds(self):
        in_diffs = [
            Extra('xxx', aaa='foo'),
            Extra('yyy', aaa='bar'),
        ]
        with self.assertRaises(TypeError) as cm:
            with allow_any('example allowance'):  # <- Missing keyword argument!
                raise DataError('example error', in_diffs)

        result = cm.exception
        expected = 'requires 1 or more keyword arguments (0 given)'
        self.assertEqual(expected, str(result))

    def test_no_exception(self):
        with self.assertRaises(AssertionError) as cm:
            with allow_any(foo='bar'):
                pass  # No exceptions raised

        exc = cm.exception
        self.assertEqual('No differences found: allow_any', str(exc))


class TestAllowExtra(unittest.TestCase):
    """Test allow_extra() behavior."""
    def test_allow_some(self):
        differences = [Extra('xxx'), Missing('yyy')]

        with self.assertRaises(DataError) as cm:
            with allow_extra():
                raise DataError('example error', differences)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, [Missing('yyy')])

    def test_allow_all(self):
        with allow_extra():
            raise DataError('example error', [Extra('xxx'), Extra('yyy')])

    def test_kwds(self):
        in_diffs = [
            Extra('xxx', aaa='foo'),
            Extra('yyy', aaa='bar'),
            Missing('zzz', aaa='foo'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_extra('example allowance', aaa='foo'):
                raise DataError('example error', in_diffs)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, [Extra('yyy', aaa='bar'), Missing('zzz', aaa='foo')])

    def test_no_exception(self):
        with self.assertRaises(AssertionError) as cm:
            with allow_extra():
                pass  # No exceptions raised

        exc = cm.exception
        self.assertEqual('No differences found: allow_extra', str(exc))


class TestAllowMissing(unittest.TestCase):
    """Test allow_missing() behavior."""
    def test_allow_some(self):
        differences = [Extra('xxx'), Missing('yyy')]

        with self.assertRaises(DataError) as cm:
            with allow_missing():
                raise DataError('example error', differences)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, [Extra('xxx')])

    def test_allow_all(self):
        with allow_missing():
            raise DataError('example error', [Missing('xxx'), Missing('yyy')])

    def test_kwds(self):
        in_diffs = [
            Missing('xxx', aaa='foo'),
            Missing('yyy', aaa='bar'),
            Extra('zzz', aaa='foo'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_missing('example allowance', aaa='foo'):
                raise DataError('example error', in_diffs)

        rejected = list(cm.exception.differences)
        self.assertEqual(rejected, [Missing('yyy', aaa='bar'), Extra('zzz', aaa='foo')])

    def test_no_exception(self):
        with self.assertRaises(AssertionError) as cm:
            with allow_missing():
                pass  # No exceptions raised

        exc = cm.exception
        self.assertEqual('No differences found: allow_missing', str(exc))


class TestAllowOnly(unittest.TestCase):
    """Test allow_only() behavior."""
    def test_allow_some(self):
        with self.assertRaises(DataError) as cm:
            with allow_only(Extra('xxx'), 'example allowance'):
                raise DataError('example error', [Extra('xxx'), Missing('yyy')])

        result_str = str(cm.exception)
        self.assertEqual("example allowance: example error:\n Missing('yyy')", result_str)

        result_diffs = list(cm.exception.differences)
        self.assertEqual([Missing('yyy')], result_diffs)

    def test_not_found(self):
        with self.assertRaises(DataError) as cm:
            with allow_only([Extra('xxx'), Missing('yyy')]):
                raise DataError('example error', [Extra('xxx')])

        result_str = str(cm.exception)
        self.assertTrue(result_str.startswith('Allowed difference not found'))

        result_diffs = list(cm.exception.differences)
        self.assertEqual([Missing('yyy')], result_diffs)

    def test_allow_all(self):
        differences = [Missing('xxx'), Extra('yyy')]
        with allow_only(differences):
            raise DataError('example error', [Missing('xxx'), Extra('yyy')])

        # Order of differences should not matter!
        differences = [Extra('yyy'), Missing('xxx')]
        with allow_only(differences):
            raise DataError('example error', reversed(differences))

    def test_allow_one_but_find_duplicate(self):
        with self.assertRaises(DataError) as cm:
            with allow_only(Extra('xxx')):
                raise DataError('example error', [Extra('xxx'), Extra('xxx')])

        result_string = str(cm.exception)
        self.assertEqual("example error:\n Extra('xxx')", result_string)

    def test_allow_duplicate_but_find_only_one(self):
        with self.assertRaises(DataError) as cm:
            with allow_only([Extra('xxx'), Extra('xxx')]):
                raise DataError('example error', [Extra('xxx')])

        result_string = str(cm.exception)
        self.assertEqual("Allowed difference not found:\n Extra('xxx')", result_string)

    def test_no_exception(self):
        with self.assertRaises(AssertionError) as cm:
            with allow_only([Missing('xxx')]):
                pass  # No exceptions raised

        exc = cm.exception
        self.assertEqual('No differences found: allow_only', str(exc))

    def test_walk_list(self):
        flat_list = [Missing('val1'), Missing('val2')]
        nested_list = [[Missing('val1')], [Missing('val2')]]
        irregular_list = [[[Missing('val1')]], [Missing('val2')]]

        result = allow_only._walk_diff(flat_list)
        self.assertEqual(flat_list, list(result))

        result = allow_only._walk_diff(nested_list)
        self.assertEqual(flat_list, list(result))

        result = allow_only._walk_diff(irregular_list)
        self.assertEqual(flat_list, list(result))

    def test_walk_dict(self):
        values_set = set([
            Missing('xxx'),
            Missing('yyy'),
        ])
        flat_dict = {
            'key1': Missing('xxx'),
            'key2': Missing('yyy'),
        }
        nested_dict = {
            'key1': {
                'key2': Missing('xxx'),
            },
            'key3': {
                'key4': Missing('yyy'),
            },
        }
        irregular_dict = {
            'key1': Missing('xxx'),
            'key2': {
                'key3': {
                    'key4': Missing('yyy'),
                },
            },
        }

        result = allow_only._walk_diff(flat_dict)
        self.assertEqual(values_set, set(result))

        result = allow_only._walk_diff(nested_dict)
        self.assertEqual(values_set, set(result))

        result = allow_only._walk_diff(irregular_dict)
        self.assertEqual(values_set, set(result))

    def test_walk_single_element(self):
        result = allow_only._walk_diff(Missing('xxx'))  # <- Not wrapped in container.
        self.assertEqual([Missing('xxx')], list(result))

    def test_walk_mixed_types(self):
        values_set = set([
            Missing('alpha'),
            Missing('bravo'),
            Missing('charlie'),
            Missing('delta'),
        ])
        irregular_collection = {
            'key1': Missing('alpha'),
            'key2': [
                Missing('bravo'),
                [
                    Missing('charlie'),
                    Missing('delta'),
                ],
            ],
        }
        result = allow_only._walk_diff(irregular_collection)
        self.assertEqual(values_set, set(result))

    def test_walk_nondiff_items(self):
        flat_list = ['xxx', 'yyy']
        with self.assertRaises(TypeError):
            list(allow_only._walk_diff(flat_list))

        flat_dict = {'key1': 'xxx', 'key2': 'yyy'}
        with self.assertRaises(TypeError):
            list(allow_only._walk_diff(flat_dict))

        nested_list = [Missing('xxx'), ['yyy']]
        with self.assertRaises(TypeError):
            list(allow_only._walk_diff(nested_list))

        irregular_collection = {
            'key1': Missing('xxx'),
            'key2': [
                Missing('yyy'),
                [
                    Missing('zzz'),
                    'qux',
                ],
            ],
        }
        with self.assertRaises(TypeError):
            list(allow_only._walk_diff(irregular_collection))


class TestAllowLimit(unittest.TestCase):
    """Test allow_limit() behavior."""
    def test_allow_some(self):
        differences = [Extra('xxx'), Missing('yyy')]

        with self.assertRaises(DataError) as cm:
            with allow_limit(1):  # <- Allows only 1 but there are 2!
                raise DataError('example error', differences)

        rejected = list(cm.exception.differences)
        self.assertEqual(differences, rejected)

    def test_allow_all(self):
        with allow_limit(2):  # <- Allows 2 and there are only 2.
            raise DataError('example error', [Missing('xxx'), Missing('yyy')])

        with allow_limit(3):  # <- Allows 3 and there are only 2.
            raise DataError('example error', [Missing('xxx'), Missing('yyy')])

    def test_kwds(self):
        diff_set = set([
            Missing('xxx', aaa='foo'),
            Missing('yyy', aaa='bar'),
            Extra('zzz', aaa='foo'),
        ])

        with self.assertRaises(DataError) as cm:
            # Allows 2 with aaa='foo' and there are two (only aaa='bar' is rejected).
            with allow_limit(2, 'example allowance', aaa='foo'):
                raise DataError('example error', diff_set)
        rejected = set(cm.exception.differences)
        self.assertEqual(rejected, set([Missing('yyy', aaa='bar')]))

        with self.assertRaises(DataError) as cm:
            # Allows 1 with aaa='foo' but there are 2 (all are rejected)!
            with allow_limit(1, 'example allowance', aaa='foo'):
                raise DataError('example error', diff_set)
        rejected = set(cm.exception.differences)
        self.assertEqual(rejected, diff_set)

    def test_no_exception(self):
        with self.assertRaises(AssertionError) as cm:
            with allow_limit(2):
                pass  # No exceptions raised

        exc = cm.exception
        self.assertEqual('No differences found: expected at most 2 matching differences', str(exc))


class TestAllowDeviation(unittest.TestCase):
    """Test allow_deviation() behavior."""
    def test_method_signature(self):
        """Check for prettified default signature in Python 3.3 and later."""
        try:
            sig = inspect.signature(allow_deviation)
            parameters = list(sig.parameters)
            self.assertEqual(parameters, ['tolerance', 'msg', 'kwds'])
        except AttributeError:
            pass  # Python 3.2 and older use ugly signature as default.

    def test_tolerance_syntax(self):
        differences = [
            Deviation(-1, 10, label='aaa'),
            Deviation(+3, 10, label='bbb'),  # <- Not in allowed range.
        ]
        with self.assertRaises(DataError) as cm:
            with allow_deviation(2, 'example allowance'):  # <- Allows +/- 2.
                raise DataError('example error', differences)

        result_string = str(cm.exception)
        self.assertTrue(result_string.startswith('example allowance: example error'))

        result_diffs = list(cm.exception.differences)
        self.assertEqual([Deviation(+3, 10, label='bbb')], result_diffs)

    def test_lowerupper_syntax(self):
        differences = [
            Deviation(-1, 10, label='aaa'),  # <- Not in allowed range.
            Deviation(+3, 10, label='bbb'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_deviation(0, 3, 'example allowance'):  # <- Allows from 0 to 3.
                raise DataError('example error', differences)

        result_string = str(cm.exception)
        self.assertTrue(result_string.startswith('example allowance: example error'))

        result_diffs = list(cm.exception.differences)
        self.assertEqual([Deviation(-1, 10, label='aaa')], result_diffs)

    def test_single_value_allowance(self):
        differences = [
            Deviation(+2.9, 10, label='aaa'),  # <- Not allowed.
            Deviation(+3.0, 10, label='bbb'),
            Deviation(+3.0, 5, label='ccc'),
            Deviation(+3.1, 10, label='ddd'),  # <- Not allowed.
        ]
        with self.assertRaises(DataError) as cm:
            with allow_deviation(3, 3):  # <- Allows +3 only.
                raise DataError('example error', differences)

        result_diffs = set(cm.exception.differences)
        expected_diffs = set([
            Deviation(+2.9, 10, label='aaa'),
            Deviation(+3.1, 10, label='ddd'),
        ])
        self.assertEqual(expected_diffs, result_diffs)

    def test_kwds_handling(self):
        differences = [
            Deviation(-1, 10, label='aaa'),
            Deviation(+2, 10, label='aaa'),
            Deviation(+2, 10, label='bbb'),
            Deviation(+3, 10, label='aaa'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_deviation(2, 'example allowance', label='aaa'):  # <- Allows +/- 2.
                raise DataError('example error', differences)

        result_set = set(cm.exception.differences)
        expected_set = set([
            Deviation(+2, 10, label='bbb'),  # <- Keyword value not 'aaa'.
            Deviation(+3, 10, label='aaa'),  # <- Not in allowed range.
        ])
        self.assertEqual(expected_set, result_set)

    def test_invalid_tolerance(self):
        with self.assertRaises(AssertionError) as cm:
            with allow_deviation(-5):  # <- invalid
                pass
        exc = str(cm.exception)
        self.assertTrue(exc.startswith('tolerance should not be negative'))

    def test_empty_value_handling(self):
        # Test NoneType.
        with allow_deviation(0):  # <- Pass without failure.
            raise DataError('example error', [Deviation(None, 0)])

        with allow_deviation(0):  # <- Pass without failure.
            raise DataError('example error', [Deviation(0, None)])

        # Test empty string.
        with allow_deviation(0):  # <- Pass without failure.
            raise DataError('example error', [Deviation('', 0)])

        with allow_deviation(0):  # <- Pass without failure.
            raise DataError('example error', [Deviation(0, '')])

        # Test NaN (not a number) values.
        with self.assertRaises(DataError):  # <- NaN values should not be caught!
            with allow_deviation(0):
                raise DataError('example error', [Deviation(float('nan'), 0)])

        with self.assertRaises(DataError):  # <- NaN values should not be caught!
            with allow_deviation(0):
                raise DataError('example error', [Deviation(0, float('nan'))])

    # QUESTION: Should deviation allowances raise an error if the
    # maximum oberved deviation is _less_ than the given tolerance?


class TestAllowPercentDeviation(unittest.TestCase):
    """Test allow_percent_deviation() behavior."""
    def test_method_signature(self):
        """Check for prettified default signature in Python 3.3 and later."""
        try:
            sig = inspect.signature(allow_percent_deviation)
            parameters = list(sig.parameters)
            self.assertEqual(parameters, ['tolerance', 'msg', 'kwds'])
        except AttributeError:
            pass  # Python 3.2 and older use ugly signature as default.

    def test_tolerance_syntax(self):
        differences = [
            Deviation(-1, 10, label='aaa'),
            Deviation(+3, 10, label='bbb'),  # <- Not in allowed range.
        ]
        with self.assertRaises(DataError) as cm:
            with allow_percent_deviation(0.2, 'example allowance'):  # <- Allows +/- 20%.
                raise DataError('example error', differences)

        result_string = str(cm.exception)
        self.assertTrue(result_string.startswith('example allowance: example error'))

        result_diffs = list(cm.exception.differences)
        self.assertEqual([Deviation(+3, 10, label='bbb')], result_diffs)

    def test_lowerupper_syntax(self):
        differences = [
            Deviation(-1, 10, label='aaa'),  # <- Not in allowed range.
            Deviation(+3, 10, label='bbb'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_percent_deviation(0.0, 0.3, 'example allowance'):  # <- Allows from 0 to 30%.
                raise DataError('example error', differences)

        result_string = str(cm.exception)
        self.assertTrue(result_string.startswith('example allowance: example error'))

        result_diffs = list(cm.exception.differences)
        self.assertEqual([Deviation(-1, 10, label='aaa')], result_diffs)

    def test_single_value_allowance(self):
        differences = [
            Deviation(+2.9, 10, label='aaa'),  # <- Not allowed.
            Deviation(+3.0, 10, label='bbb'),
            Deviation(+6.0, 20, label='ccc'),
            Deviation(+3.1, 10, label='ddd'),  # <- Not allowed.
        ]
        with self.assertRaises(DataError) as cm:
            with allow_percent_deviation(0.3, 0.3):  # <- Allows +30% only.
                raise DataError('example error', differences)

        result_diffs = set(cm.exception.differences)
        expected_diffs = set([
            Deviation(+2.9, 10, label='aaa'),
            Deviation(+3.1, 10, label='ddd'),
        ])
        self.assertEqual(expected_diffs, result_diffs)

    def test_kwds_handling(self):
        differences = [
            Deviation(-1, 10, label='aaa'),
            Deviation(+2, 10, label='aaa'),
            Deviation(+2, 10, label='bbb'),
            Deviation(+3, 10, label='aaa'),
        ]
        with self.assertRaises(DataError) as cm:
            with allow_percent_deviation(0.2, 'example allowance', label='aaa'):  # <- Allows +/- 20%.
                raise DataError('example error', differences)

        result_set = set(cm.exception.differences)
        expected_set = set([
            Deviation(+2, 10, label='bbb'),  # <- Keyword value not 'aaa'.
            Deviation(+3, 10, label='aaa'),  # <- Not in allowed range.
        ])
        self.assertEqual(expected_set, result_set)

    def test_invalid_tolerance(self):
        with self.assertRaises(AssertionError) as cm:
            with allow_percent_deviation(-0.5):  # <- invalid
                pass
        exc = str(cm.exception)
        self.assertTrue(exc.startswith('tolerance should not be negative'))

    def test_empty_value_handling(self):
        # Test NoneType.
        with allow_percent_deviation(0):  # <- Pass without failure.
            raise DataError('example error', [Deviation(None, 0)])

        with allow_percent_deviation(0):  # <- Pass without failure.
            raise DataError('example error', [Deviation(0, None)])

        # Test empty string.
        with allow_percent_deviation(0):  # <- Pass without failure.
            raise DataError('example error', [Deviation('', 0)])

        with allow_percent_deviation(0):  # <- Pass without failure.
            raise DataError('example error', [Deviation(0, '')])

        # Test NaN (not a number) values.
        with self.assertRaises(DataError):  # <- NaN values should not be caught!
            with allow_percent_deviation(0):
                raise DataError('example error', [Deviation(float('nan'), 0)])

        with self.assertRaises(DataError):  # <- NaN values should not be caught!
            with allow_percent_deviation(0):
                raise DataError('example error', [Deviation(0, float('nan'))])


class TestNestedAllowances(unittest.TestCase):
    def test_nested_allowances(self):
        """A quick integration test to make sure allowances nest as
        required.
        """
        with allow_only(Deviation(-4,  70, label1='b')):  # <- specified diff only
            with allow_deviation(3):                      # <- tolerance of +/- 3
                with allow_percent_deviation(0.02):       # <- tolerance of +/- 2%
                    differences = [
                        Deviation(+3,  65, label1='a'),
                        Deviation(-4,  70, label1='b'),
                        Deviation(+5, 250, label1='c'),
                    ]
                    raise DataError('example error', differences)
