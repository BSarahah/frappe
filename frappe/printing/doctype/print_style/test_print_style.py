# Copyright (c) 2017, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestPrintStyle(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestPrintStyle(UnitTestCase):
	"""
	Unit tests for PrintStyle.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestPrintStyle(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
