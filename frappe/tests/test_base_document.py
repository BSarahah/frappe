from frappe.model.base_document import BaseDocument
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestBaseDocument(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase


class TestBaseDocument(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	def test_docstatus(self):
		doc = BaseDocument({"docstatus": 0, "doctype": "ToDo"})
		self.assertTrue(doc.docstatus.is_draft())
		self.assertEqual(doc.docstatus, 0)

		doc.docstatus = 1
		self.assertTrue(doc.docstatus.is_submitted())
		self.assertEqual(doc.docstatus, 1)

		doc.docstatus = 2
		self.assertTrue(doc.docstatus.is_cancelled())
		self.assertEqual(doc.docstatus, 2)
