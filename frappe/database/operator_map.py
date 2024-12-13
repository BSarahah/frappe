# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import operator
from collections.abc import Callable

import frappe
from frappe.database.utils import NestedSetHierarchy
from frappe.model.db_query import get_timespan_date_range
from frappe.query_builder import Field
<<<<<<< HEAD
=======
from frappe.query_builder.functions import Coalesce
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)


def like(key: Field, value: str) -> frappe.qb:
	"""Wrapper method for `LIKE`

	Args:
	        key (str): field
	        value (str): criterion

<<<<<<< HEAD
	Returns:
	        frappe.qb: `frappe.qb object with `LIKE`
=======
	Return:
	        frappe.qb: `frappe.qb` object with `LIKE`
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"""
	return key.like(value)


def func_in(key: Field, value: list | tuple) -> frappe.qb:
<<<<<<< HEAD
	"""Wrapper method for `IN`
=======
	"""Wrapper method for `IN`.
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)

	Args:
	        key (str): field
	        value (Union[int, str]): criterion

<<<<<<< HEAD
	Returns:
	        frappe.qb: `frappe.qb object with `IN`
=======
	Return:
	        frappe.qb: `frappe.qb` object with `IN`
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"""
	if isinstance(value, str):
		value = value.split(",")
	return key.isin(value)


def not_like(key: Field, value: str) -> frappe.qb:
<<<<<<< HEAD
	"""Wrapper method for `NOT LIKE`
=======
	"""Wrapper method for `NOT LIKE`.
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)

	Args:
	        key (str): field
	        value (str): criterion

<<<<<<< HEAD
	Returns:
	        frappe.qb: `frappe.qb object with `NOT LIKE`
=======
	Return:
	        frappe.qb: `frappe.qb` object with `NOT LIKE`
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"""
	return key.not_like(value)


def func_not_in(key: Field, value: list | tuple | str):
<<<<<<< HEAD
	"""Wrapper method for `NOT IN`
=======
	"""Wrapper method for `NOT IN`.
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)

	Args:
	        key (str): field
	        value (Union[int, str]): criterion

<<<<<<< HEAD
	Returns:
	        frappe.qb: `frappe.qb object with `NOT IN`
=======
	Return:
	        frappe.qb: `frappe.qb` object with `NOT IN`
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"""
	if isinstance(value, str):
		value = value.split(",")
	return key.notin(value)


def func_regex(key: Field, value: str) -> frappe.qb:
	"""Wrapper method for `REGEX`

	Args:
	        key (str): field
	        value (str): criterion

<<<<<<< HEAD
	Returns:
	        frappe.qb: `frappe.qb object with `REGEX`
=======
	Return:
	        frappe.qb: `frappe.qb` object with `REGEX`
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"""
	return key.regex(value)


def func_between(key: Field, value: list | tuple) -> frappe.qb:
<<<<<<< HEAD
	"""Wrapper method for `BETWEEN`
=======
	"""Wrapper method for `BETWEEN`.
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)

	Args:
	        key (str): field
	        value (Union[int, str]): criterion

<<<<<<< HEAD
	Returns:
	        frappe.qb: `frappe.qb object with `BETWEEN`
=======
	Return:
	        frappe.qb: `frappe.qb` object with `BETWEEN`
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"""
	return key[slice(*value)]


def func_is(key, value):
	"Wrapper for IS"
<<<<<<< HEAD
	return key.isnotnull() if value.lower() == "set" else key.isnull()


def func_timespan(key: Field, value: str) -> frappe.qb:
	"""Wrapper method for `TIMESPAN`
=======
	return Coalesce(key, "") != "" if value.lower() == "set" else Coalesce(key, "") == ""


def func_timespan(key: Field, value: str) -> frappe.qb:
	"""Wrapper method for `TIMESPAN`.
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)

	Args:
	        key (str): field
	        value (str): criterion

<<<<<<< HEAD
	Returns:
	        frappe.qb: `frappe.qb object with `TIMESPAN`
=======
	Return:
	        frappe.qb: `frappe.qb` object with `TIMESPAN`
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	"""

	return func_between(key, get_timespan_date_range(value))


# default operators
OPERATOR_MAP: dict[str, Callable] = {
	"+": operator.add,
	"=": operator.eq,
	"-": operator.sub,
	"!=": operator.ne,
	"<": operator.lt,
	">": operator.gt,
	"<=": operator.le,
	"=<": operator.le,
	">=": operator.ge,
	"=>": operator.ge,
	"/": operator.truediv,
	"*": operator.mul,
	"in": func_in,
	"not in": func_not_in,
	"like": like,
	"not like": not_like,
	"regex": func_regex,
	"between": func_between,
	"is": func_is,
	"timespan": func_timespan,
	"nested_set": NestedSetHierarchy,
	# TODO: Add support for custom operators (WIP) - via filters_config hooks
}
