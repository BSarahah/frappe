# Copyright (c) 2020, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestAboutUsSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestAboutUsSettings(UnitTestCase):
	"""
	Unit tests for AboutUsSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestAboutUsSettings(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
