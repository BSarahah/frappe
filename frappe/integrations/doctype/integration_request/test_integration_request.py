# Copyright (c) 2015, Frappe Technologies and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('Integration Request')


class TestIntegrationRequest(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestIntegrationRequest(UnitTestCase):
	"""
	Unit tests for IntegrationRequest.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestIntegrationRequest(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
