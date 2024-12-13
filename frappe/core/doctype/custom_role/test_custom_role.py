# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('Custom Role')


class TestCustomRole(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestCustomRole(UnitTestCase):
	"""
	Unit tests for CustomRole.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestCustomRole(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
