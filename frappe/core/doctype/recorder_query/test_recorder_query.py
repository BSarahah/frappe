# Copyright (c) 2023, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestRecorderQuery(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestRecorderQuery(UnitTestCase):
	"""
	Unit tests for RecorderQuery.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestRecorderQuery(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
