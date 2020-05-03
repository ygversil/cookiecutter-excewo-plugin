"""Tests tasks for {{ cookiecutter.package_name }}."""


import unittest

from {{ cookiecutter.package_name }}.tasks import add


class AddTest(unittest.TestCase):
    """Test for ``add`` task."""

    def test_add_integers(self):
        """Check that ``add`` task can add integers."""
        self.assertEqual(add(1, 2), 3)

    def test_add_floats(self):
        """Check that ``add`` task can add floats."""
        self.assertEqual(add(1.2, 3.4), 4.6)

    def test_add_strings(self):
        """Check that ``add`` task can add strings."""
        self.assertEqual(add('foo ', 'bar'), 'foo bar')

    def test_add_lists(self):
        """Check that ``add`` task can add lists."""
        self.assertEqual(add([1, 2], [3, 4]), [1, 2, 3, 4])
