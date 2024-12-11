# Copyright (c) 2017, Frappe Technologies and contributors
# License: MIT. See LICENSE

# import frappe
from frappe.model.document import Document


class WebhookHeader(Document):
<<<<<<< HEAD
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		key: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		value: DF.Data | None
	# end: auto-generated types
=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	pass
