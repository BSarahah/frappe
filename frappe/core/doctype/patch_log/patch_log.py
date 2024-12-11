# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

# License: MIT. See LICENSE

import frappe
from frappe.model.document import Document


class PatchLog(Document):
<<<<<<< HEAD
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		patch: DF.Code | None
		skipped: DF.Check
		traceback: DF.Code | None
	# end: auto-generated types
=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	pass


def before_migrate():
	frappe.reload_doc("core", "doctype", "patch_log")
