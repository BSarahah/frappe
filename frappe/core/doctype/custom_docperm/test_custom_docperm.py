# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('Custom DocPerm')


class TestCustomDocPerm(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestCustomDocperm(UnitTestCase):
	"""
	Unit tests for CustomDocperm.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestCustomDocPerm(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
