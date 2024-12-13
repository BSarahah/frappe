"""
<<<<<<< HEAD
    Modify the Integer 10 Digits Value to BigInt 20 Digit value
    to generate long Naming Series

"""
=======
Modify the Integer 10 Digits Value to BigInt 20 Digit value
to generate long Naming Series

"""

>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
import frappe


def execute():
	frappe.db.sql(""" ALTER TABLE `tabSeries` MODIFY current BIGINT """)
