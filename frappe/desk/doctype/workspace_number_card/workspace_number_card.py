# Copyright (c) 2023, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class WorkspaceNumberCard(Document):
<<<<<<< HEAD
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		label: DF.Data | None
		number_card_name: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types
=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	pass
