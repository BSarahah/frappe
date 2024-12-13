# Copyright (c) 2021, FOSS United and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDiscussionReply(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDiscussionReply(UnitTestCase):
	"""
	Unit tests for DiscussionReply.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDiscussionReply(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
