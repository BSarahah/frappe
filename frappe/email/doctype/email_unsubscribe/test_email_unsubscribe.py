# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('Email Unsubscribe')


class TestEmailUnsubscribe(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestEmailUnsubscribe(UnitTestCase):
	"""
	Unit tests for EmailUnsubscribe.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestEmailUnsubscribe(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
