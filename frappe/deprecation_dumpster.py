"""
Welcome to the Deprecation Dumpster: Where Old Code Goes to Party! 🎉🗑️

This file is the final resting place (or should we say, "retirement home"?) for all the deprecated functions and methods of the Frappe framework. It's like a code nursing home, but with more monkey-patching and less bingo.

Each function or method that checks in here comes with its own personalized decorator, complete with:
1. The date it was marked for deprecation (its "over the hill" birthday)
2. The Frappe version in which it will be removed (its "graduation" to the great codebase in the sky)
3. A user-facing note on alternative solutions (its "parting wisdom")

Warning: The global namespace herein is more patched up than a sailor's favorite pair of jeans. Proceed with caution and a sense of humor!

Remember, deprecated doesn't mean useless - it just means these functions are enjoying their golden years before their final bow. Treat them with respect, and maybe bring them some virtual prune juice.

Enjoy your stay in the Deprecation Dumpster, where every function gets a second chance to shine (or at least, to not break everything).
"""

import inspect
import os
import sys
import warnings


def is_tty():
	return sys.stdout.isatty()


def colorize(text, color_code):
	if is_tty():
		return f"\033[{color_code}m{text}\033[0m"
	return text


try:
	# since python 3.13, PEP 702
	from warnings import deprecated as _deprecated
except Exception:
	import functools
	import warnings
	from collections.abc import Callable
	from typing import Optional, TypeVar, Union, overload

	T = TypeVar("T", bound=Callable)

	def _deprecated(message: str, category=DeprecationWarning, stacklevel=1) -> Callable[[T], T]:
		def decorator(func: T) -> T:
			@functools.wraps(func)
			def wrapper(*args, **kwargs):
				if message:
					warning_msg = f"{func.__name__} is deprecated.\n{message}"
				else:
					warning_msg = f"{func.__name__} is deprecated."
				warnings.warn(warning_msg, category=category, stacklevel=stacklevel + 1)
				return func(*args, **kwargs)

			return wrapper
			wrapper.__deprecated__ = True  # hint for the type checker

		return decorator


def deprecated(original: str, marked: str, graduation: str, msg: str, stacklevel: int = 1):
	"""Decorator to wrap a function/method as deprecated.

	Arguments:
	        - original: frappe.utils.make_esc  (fully qualified)
	        - marked: 2024-09-13  (the date it has been marked)
	        - graduation: v17  (generally: current version + 2)
	"""

	def decorator(func):
		# Get the filename of the caller
		frame = inspect.currentframe()
		caller_filepath = frame.f_back.f_code.co_filename
		if os.path.basename(caller_filepath) != "deprecation_dumpster.py":
			raise RuntimeError(
				colorize("The deprecated function ", "93")
				+ colorize(func.__name__, "96")
				+ colorize(" can only be called from ", "93")
				+ colorize("frappe/deprecation_dumpster.py\n", "96")
				+ colorize("Move the entire function there and import it back via adding\n ", "93")  # yellow
				+ colorize(f"from frappe.deprecation_dumpster import {func.__name__}\n", "96")  # cyan
				+ colorize("to file\n ", "93")  # yellow
				+ colorize(caller_filepath, "96")  # cyan
			)

		return functools.wraps(func)(
			_deprecated(
				colorize(f"`{original}`", "96")
				+ colorize(
					f" was moved (DATE: {marked}) to frappe/deprecation_dumpster.py"
					f" for removal (from {graduation} onwards); note:\n ",
					"91",
				)  # red
				+ colorize(f"{msg}\n", "93"),  # yellow
				stacklevel=stacklevel,
			)
		)(func)

	return decorator


def deprecation_warning(marked: str, graduation: str, msg: str):
	"""Warn in-place from a deprecated code path, for objects use `@deprecated` decorator from the deprectation_dumpster"

	Arguments:
	        - marked: 2024-09-13  (the date it has been marked)
	        - graduation: v17  (generally: current version + 2)
	"""

	warnings.warn(
		colorize(
			f"This codepath was marked (DATE: {marked}) deprecated"
			f" for removal (from {graduation} onwards); note:\n ",
			"91",
		)  # red
		+ colorize(f"{msg}\n", "93"),  # yellow
		category=DeprecationWarning,
		stacklevel=2,
	)


### Party starts here


@deprecated(
	"frappe.init (old calling signature)",
	"2024-09-13",
	"v17",
	"Use the new calling signature: frappe.init(bench: frappe.bench.Bench, force: bool = False) 🎉🗑️",
	stacklevel=3,  # get past functools.dispatch
)
def old_init(site, sites_path, new_site, force) -> None:
	from pathlib import Path

	from frappe import _init
	from frappe.bench import Bench

	implied_bench_path = Path(sites_path).resolve().parent
	bench = Bench(implied_bench_path, site_name=site)

	return _init(bench, force)


def _old_deprecated(func):
	return deprecated(
		"frappe.deprecations.deprecated",
		"2024-09-13",
		"v17",
		"Make use of the frappe/deprecation_dumpster.py file, instead. 🎉🗑️",
	)(_deprecated("")(func))


def _old_deprecation_warning(msg):
	@deprecated(
		"frappe.deprecations.deprecation_warning",
		"2024-09-13",
		"v17",
		"Use frappe.deprecation_dumpster.deprecation_warning, instead. 🎉🗑️",
	)
	def deprecation_warning(message, category=DeprecationWarning, stacklevel=1):
		warnings.warn(message=message, category=category, stacklevel=stacklevel + 2)

	return deprecation_warning(msg)


@deprecated("frappe.utils.make_esc", "unknown", "v17", "Not used anymore.")
def make_esc(esc_chars):
	"""
	Function generator for Escaping special characters
	"""
	return lambda s: "".join("\\" + c if c in esc_chars else c for c in s)


@deprecated(
	"frappe.db.is_column_missing",
	"unknown",
	"v17",
	"Renamed to frappe.db.is_missing_column.",
)
def is_column_missing(e):
	import frappe

	return frappe.db.is_missing_column(e)


@deprecated(
	"frappe.desk.doctype.bulk_update.bulk_update",
	"unknown",
	"v17",
	"Unknown.",
)
def show_progress(docnames, message, i, description):
	import frappe

	n = len(docnames)
	frappe.publish_progress(float(i) * 100 / n, title=message, description=description)


@deprecated(
	"frappe.client.get_js",
	"unknown",
	"v17",
	"Unknown.",
)
def get_js(items):
	"""Load JS code files.  Will also append translations
	and extend `frappe._messages`

	:param items: JSON list of paths of the js files to be loaded."""
	import json

	import frappe
	from frappe import _

	items = json.loads(items)
	out = []
	for src in items:
		src = src.strip("/").split("/")

		if ".." in src or src[0] != "assets":
			frappe.throw(_("Invalid file path: {0}").format("/".join(src)))

		contentpath = os.path.join(frappe.local.sites_path, *src)
		with open(contentpath) as srcfile:
			code = frappe.utils.cstr(srcfile.read())

		out.append(code)

	return out


@deprecated(
	"frappe.utils.print_format.read_multi_pdf",
	"unknown",
	"v17",
	"Unknown.",
)
def read_multi_pdf(output) -> bytes:
	from io import BytesIO

	with BytesIO() as merged_pdf:
		output.write(merged_pdf)
		return merged_pdf.getvalue()


@deprecated("frappe.gzip_compress", "unknown", "v17", "Use py3 methods directly (this was compat for py2).")
def gzip_compress(data, compresslevel=9):
	"""Compress data in one shot and return the compressed string.
	Optional argument is the compression level, in range of 0-9.
	"""
	import io
	from gzip import GzipFile

	buf = io.BytesIO()
	with GzipFile(fileobj=buf, mode="wb", compresslevel=compresslevel) as f:
		f.write(data)
	return buf.getvalue()


@deprecated("frappe.gzip_decompress", "unknown", "v17", "Use py3 methods directly (this was compat for py2).")
def gzip_decompress(data):
	"""Decompress a gzip compressed string in one shot.
	Return the decompressed string.
	"""
	import io
	from gzip import GzipFile

	with GzipFile(fileobj=io.BytesIO(data)) as f:
		return f.read()


@deprecated(
	"frappe.email.doctype.email_queue.email_queue.send_mail",
	"unknown",
	"v17",
	"Unknown.",
)
def send_mail(email_queue_name, smtp_server_instance=None):
	"""This is equivalent to EmailQueue.send.

	This provides a way to make sending mail as a background job.
	"""
	from frappe.email.doctype.email_queue.email_queue import EmailQueue

	record = EmailQueue.find(email_queue_name)
	record.send(smtp_server_instance=smtp_server_instance)


@deprecated(
	"frappe.geo.country_info.get_translated_dict",
	"unknown",
	"v17",
	"Use frappe.geo.country_info.get_translated_countries, instead.",
)
def get_translated_dict():
	from frappe.geo.country_info import get_translated_countries

	return get_translated_countries()


@deprecated(
	"User.validate_roles",
	"unknown",
	"v17",
	"Use User.populate_role_profile_roles, instead.",
)
def validate_roles(self):
	self.populate_role_profile_roles()