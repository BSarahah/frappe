# Copyright (c) 2021, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestUserGroup(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestUserGroup(UnitTestCase):
	"""
	Unit tests for UserGroup.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestUserGroup(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
