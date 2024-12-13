# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import json

import frappe


def execute():
<<<<<<< HEAD
	"""Convert Query Report json to support other content"""
=======
	"""Convert Query Report json to support other content."""
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	records = frappe.get_all("Report", filters={"json": ["!=", ""]}, fields=["name", "json"])
	for record in records:
		jstr = record["json"]
		data = json.loads(jstr)
		if isinstance(data, list):
			# double escape braces
			jstr = f'{{"columns":{jstr}}}'
			frappe.db.set_value("Report", record["name"], "json", jstr)
