# Copyright (c) 2017, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDomain(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDomain(UnitTestCase):
	"""
	Unit tests for Domain.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDomain(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
