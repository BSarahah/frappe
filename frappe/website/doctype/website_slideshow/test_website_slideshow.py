# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE
import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase

# test_records = frappe.get_test_records('Website Slideshow')


class TestWebsiteSlideshow(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestWebsiteSlideshow(UnitTestCase):
	"""
	Unit tests for WebsiteSlideshow.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestWebsiteSlideshow(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
