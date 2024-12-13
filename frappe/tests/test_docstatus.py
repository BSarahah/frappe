from frappe.model.docstatus import DocStatus
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestDocStatus(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase


class TestDocStatus(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	def test_draft(self):
		self.assertEqual(DocStatus(0), DocStatus.draft())

		self.assertTrue(DocStatus.draft().is_draft())
		self.assertFalse(DocStatus.draft().is_cancelled())
		self.assertFalse(DocStatus.draft().is_submitted())

	def test_submitted(self):
		self.assertEqual(DocStatus(1), DocStatus.submitted())

		self.assertFalse(DocStatus.submitted().is_draft())
		self.assertTrue(DocStatus.submitted().is_submitted())
		self.assertFalse(DocStatus.submitted().is_cancelled())

	def test_cancelled(self):
		self.assertEqual(DocStatus(2), DocStatus.cancelled())

		self.assertFalse(DocStatus.cancelled().is_draft())
		self.assertFalse(DocStatus.cancelled().is_submitted())
		self.assertTrue(DocStatus.cancelled().is_cancelled())
