# Copyright (c) 2021, FOSS United and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDiscussionTopic(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDiscussionTopic(UnitTestCase):
	"""
	Unit tests for DiscussionTopic.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDiscussionTopic(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
