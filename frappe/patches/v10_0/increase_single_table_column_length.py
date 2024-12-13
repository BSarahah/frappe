"""
Run this after updating country_info.json and or
"""
<<<<<<< HEAD
=======

>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
import frappe


def execute():
	for col in ("field", "doctype"):
		frappe.db.sql_ddl(f"alter table `tabSingles` modify column `{col}` varchar(255)")
