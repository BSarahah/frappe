# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

# pre loaded

import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestUser(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestCurrency(UnitTestCase):
	"""
	Unit tests for Currency.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestUser(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	def test_default_currency_on_setup(self):
		usd = frappe.get_doc("Currency", "USD")
		self.assertDocumentEqual({"enabled": 1, "fraction": "Cent"}, usd)
