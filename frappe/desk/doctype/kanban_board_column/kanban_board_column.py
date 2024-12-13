# Copyright (c) 2015, Frappe Technologies and contributors
# License: MIT. See LICENSE

from frappe.model.document import Document


class KanbanBoardColumn(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		column_name: DF.Data | None
		indicator: DF.Literal[
<<<<<<< HEAD
			"Blue",
			"Cyan",
			"Gray",
			"Green",
			"Light Blue",
			"Orange",
			"Pink",
			"Purple",
			"Red",
			"Red",
			"Yellow",
=======
			"Blue", "Cyan", "Gray", "Green", "Light Blue", "Orange", "Pink", "Purple", "Red", "Yellow"
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
		]
		order: DF.Code | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		status: DF.Literal["Active", "Archived"]
	# end: auto-generated types
<<<<<<< HEAD
=======

>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	pass
