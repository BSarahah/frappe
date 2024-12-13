"""
Run this after updating country_info.json and or
"""
<<<<<<< HEAD
=======

>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
from frappe.utils.install import import_country_and_currency


def execute():
	import_country_and_currency()
