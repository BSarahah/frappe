# Copyright (c) 2019, Frappe Technologies and Contributors
# License: MIT. See LICENSE
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDashboardChartSource(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestDashboardChartSource(UnitTestCase):
	"""
	Unit tests for DashboardChartSource.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestDashboardChartSource(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
