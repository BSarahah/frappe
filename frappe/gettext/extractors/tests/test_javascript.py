from frappe.gettext.extractors.javascript import extract_javascript
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestJavaScript(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase


class TestJavaScript(IntegrationTestCase):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	def test_extract_javascript(self):
		code = "let test = `<p>${__('Test')}</p>`;"
		self.assertEqual(
			next(extract_javascript(code)),
			(1, "__", "Test"),
		)

		code = "let test = `<p>${__('Test', null, 'Context')}</p>`;"
		self.assertEqual(
			next(extract_javascript(code)),
			(1, "__", ("Test", None, "Context")),
		)
