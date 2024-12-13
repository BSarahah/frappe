# Copyright (c) 2024, Frappe Technologies and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestPushNotificationSettings(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestPushNotificationSettings(UnitTestCase):
	"""
	Unit tests for PushNotificationSettings.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestPushNotificationSettings(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
