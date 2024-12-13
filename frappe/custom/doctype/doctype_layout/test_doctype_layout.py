# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDocTypeLayout(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDoctypeLayout(UnitTestCase):
	"""
	Unit tests for DoctypeLayout.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDocTypeLayout(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
