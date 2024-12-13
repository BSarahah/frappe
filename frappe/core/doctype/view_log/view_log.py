# Copyright (c) 2018, Frappe Technologies and contributors
# License: MIT. See LICENSE

import frappe
from frappe.model.document import Document


class ViewLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		reference_doctype: DF.Link | None
		reference_name: DF.DynamicLink | None
		viewed_by: DF.Data | None
<<<<<<< HEAD

	# end: auto-generated types
=======
	# end: auto-generated types

>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	@staticmethod
	def clear_old_logs(days=180):
		from frappe.query_builder import Interval
		from frappe.query_builder.functions import Now

		table = frappe.qb.DocType("View Log")
<<<<<<< HEAD
		frappe.db.delete(table, filters=(table.modified < (Now() - Interval(days=days))))
=======
		frappe.db.delete(table, filters=(table.creation < (Now() - Interval(days=days))))
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
