# Copyright (c) 2017, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestGender(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestGender(UnitTestCase):
	"""
	Unit tests for Gender.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestGender(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
