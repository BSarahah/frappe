# Copyright (c) 2020, Frappe Technologies and contributors
# License: MIT. See LICENSE

# import frappe
from frappe.model.document import Document


class InstalledApplication(Document):
<<<<<<< HEAD
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		app_name: DF.Data
		app_version: DF.Data
		git_branch: DF.Data
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types
=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	pass
