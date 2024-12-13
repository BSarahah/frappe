# Copyright (c) 2015, Frappe Technologies and contributors
# License: MIT. See LICENSE

import json

import frappe
<<<<<<< HEAD
from frappe.integrations.utils import json_handler
=======
from frappe.integrations.utils import get_json, json_handler
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
from frappe.model.document import Document


class IntegrationRequest(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		data: DF.Code | None
		error: DF.Code | None
		integration_request_service: DF.Data | None
		is_remote_request: DF.Check
		output: DF.Code | None
		reference_docname: DF.DynamicLink | None
		reference_doctype: DF.Link | None
		request_description: DF.Data | None
		request_headers: DF.Code | None
		request_id: DF.Data | None
		status: DF.Literal["", "Queued", "Authorized", "Completed", "Cancelled", "Failed"]
		url: DF.SmallText | None
<<<<<<< HEAD

	# end: auto-generated types
=======
	# end: auto-generated types

>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	def autoname(self):
		if self.flags._name:
			self.name = self.flags._name

	def clear_old_logs(days=30):
		from frappe.query_builder import Interval
		from frappe.query_builder.functions import Now

		table = frappe.qb.DocType("Integration Request")
<<<<<<< HEAD
		frappe.db.delete(table, filters=(table.modified < (Now() - Interval(days=days))))
=======
		frappe.db.delete(table, filters=(table.creation < (Now() - Interval(days=days))))
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)

	def update_status(self, params, status):
		data = json.loads(self.data)
		data.update(params)

<<<<<<< HEAD
		self.data = json.dumps(data)
=======
		self.data = get_json(data)
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
		self.status = status
		self.save(ignore_permissions=True)
		frappe.db.commit()

	def handle_success(self, response):
		"""update the output field with the response along with the relevant status"""
		if isinstance(response, str):
			response = json.loads(response)
		self.db_set("status", "Completed")
		self.db_set("output", json.dumps(response, default=json_handler))

	def handle_failure(self, response):
		"""update the error field with the response along with the relevant status"""
		if isinstance(response, str):
			response = json.loads(response)
		self.db_set("status", "Failed")
		self.db_set("error", json.dumps(response, default=json_handler))
