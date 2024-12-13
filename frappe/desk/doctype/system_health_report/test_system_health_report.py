# Copyright (c) 2024, Frappe Technologies and Contributors
# See license.txt

import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestSystemHealthReport(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestSystemHealthReport(UnitTestCase):
	"""
	Unit tests for SystemHealthReport.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestSystemHealthReport(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	def test_it_works(self):
		frappe.get_doc("System Health Report")
