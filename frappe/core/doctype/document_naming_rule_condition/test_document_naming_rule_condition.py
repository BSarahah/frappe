# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDocumentNamingRuleCondition(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDocumentNamingRuleCondition(UnitTestCase):
	"""
	Unit tests for DocumentNamingRuleCondition.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDocumentNamingRuleCondition(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
