# Copyright (c) 2019, Frappe Technologies and Contributors
# License: MIT. See LICENSE
# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestScheduledJobLog(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestScheduledJobLog(UnitTestCase):
	"""
	Unit tests for ScheduledJobLog.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestScheduledJobLog(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
