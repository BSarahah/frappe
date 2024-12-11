# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SystemHealthReportQueue(Document):
<<<<<<< HEAD
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		pending_jobs: DF.Int
		queue: DF.Data | None
	# end: auto-generated types

=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	def db_insert(self, *args, **kwargs):
		raise NotImplementedError

	def load_from_db(self):
		raise NotImplementedError

	def db_update(self):
		raise NotImplementedError

	def delete(self):
		raise NotImplementedError

	@staticmethod
	def get_list(filters=None, page_length=20, **kwargs):
		pass

	@staticmethod
	def get_count(filters=None, **kwargs):
		pass

	@staticmethod
	def get_stats(**kwargs):
		pass
