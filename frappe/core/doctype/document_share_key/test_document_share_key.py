# Copyright (c) 2021, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDocumentShareKey(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDocumentShareKey(UnitTestCase):
	"""
	Unit tests for DocumentShareKey.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDocumentShareKey(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
