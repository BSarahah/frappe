<<<<<<< HEAD
# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
=======
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
# License: MIT. See LICENSE
"""
	Utilities for using modules
"""
import json
import os
<<<<<<< HEAD
from textwrap import dedent, indent
from typing import TYPE_CHECKING, Union

import frappe
from frappe import _, get_module_path, scrub
from frappe.utils import cint, cstr, now_datetime

if TYPE_CHECKING:
	from types import ModuleType

	from frappe.model.document import Document


doctype_python_modules = {}


def export_module_json(doc: "Document", is_standard: bool, module: str) -> str | None:
	"""Make a folder for the given doc and add its json file (make it a standard
	object that will be synced)

	Returns the absolute file_path without the extension.
	Eg: For exporting a Print Format "_Test Print Format 1", the return value will be
	`/home/gavin/frappe-bench/apps/frappe/frappe/core/print_format/_test_print_format_1/_test_print_format_1`
	"""
	if not frappe.flags.in_import and is_standard and frappe.conf.developer_mode:
=======

import frappe
import frappe.utils
from frappe import _
from frappe.utils import cint


def export_module_json(doc, is_standard, module):
	"""Make a folder for the given doc and add its json file (make it a standard
	object that will be synced)"""
	if not frappe.flags.in_import and getattr(frappe.get_conf(), "developer_mode", 0) and is_standard:
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
		from frappe.modules.export_file import export_to_files

		# json
		export_to_files(record_list=[[doc.doctype, doc.name]], record_module=module, create_init=is_standard)

<<<<<<< HEAD
		return os.path.join(
			frappe.get_module_path(module), scrub(doc.doctype), scrub(doc.name), scrub(doc.name)
		)


def get_doc_module(module: str, doctype: str, name: str) -> "ModuleType":
=======
		path = os.path.join(
			frappe.get_module_path(module), scrub(doc.doctype), scrub(doc.name), scrub(doc.name)
		)

		return path


def get_doc_module(module, doctype, name):
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	"""Get custom module for given document"""
	module_name = "{app}.{module}.{doctype}.{name}.{name}".format(
		app=frappe.local.module_app[scrub(module)],
		doctype=scrub(doctype),
		module=scrub(module),
		name=scrub(name),
	)
	return frappe.get_module(module_name)


@frappe.whitelist()
<<<<<<< HEAD
def export_customizations(
	module: str, doctype: str, sync_on_migrate: bool = False, with_permissions: bool = False
):
=======
def export_customizations(module, doctype, sync_on_migrate=0, with_permissions=0):
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	"""Export Custom Field and Property Setter for the current document to the app folder.
	This will be synced with bench migrate"""

	sync_on_migrate = cint(sync_on_migrate)
	with_permissions = cint(with_permissions)

<<<<<<< HEAD
	if not frappe.conf.developer_mode:
		frappe.throw(_("Only allowed to export customizations in developer mode"))

	custom = {
		"custom_fields": frappe.get_all("Custom Field", fields="*", filters={"dt": doctype}, order_by="name"),
		"property_setters": frappe.get_all(
			"Property Setter", fields="*", filters={"doc_type": doctype}, order_by="name"
		),
		"custom_perms": [],
		"links": frappe.get_all("DocType Link", fields="*", filters={"parent": doctype}, order_by="name"),
=======
	if not frappe.get_conf().developer_mode:
		raise Exception("Not developer mode")

	custom = {
		"custom_fields": [],
		"property_setters": [],
		"custom_perms": [],
		"links": [],
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
		"doctype": doctype,
		"sync_on_migrate": sync_on_migrate,
	}

<<<<<<< HEAD
=======
	def add(_doctype):
		custom["custom_fields"] += frappe.get_all(
			"Custom Field", fields="*", filters={"dt": _doctype}, order_by="name"
		)
		custom["property_setters"] += frappe.get_all(
			"Property Setter", fields="*", filters={"doc_type": _doctype}, order_by="name"
		)
		custom["links"] += frappe.get_all(
			"DocType Link", fields="*", filters={"parent": _doctype}, order_by="name"
		)

	add(doctype)

>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	if with_permissions:
		custom["custom_perms"] = frappe.get_all(
			"Custom DocPerm", fields="*", filters={"parent": doctype}, order_by="name"
		)

	# also update the custom fields and property setters for all child tables
	for d in frappe.get_meta(doctype).get_table_fields():
		export_customizations(module, d.options, sync_on_migrate, with_permissions)

	if custom["custom_fields"] or custom["property_setters"] or custom["custom_perms"]:
		folder_path = os.path.join(get_module_path(module), "custom")
		if not os.path.exists(folder_path):
			os.makedirs(folder_path)

		path = os.path.join(folder_path, scrub(doctype) + ".json")
		with open(path, "w") as f:
			f.write(frappe.as_json(custom))

		frappe.msgprint(_("Customizations for <b>{0}</b> exported to:<br>{1}").format(doctype, path))
		return path


def sync_customizations(app=None):
	"""Sync custom fields and property setters from custom folder in each app module"""

	if app:
		apps = [app]
	else:
		apps = frappe.get_installed_apps()

	for app_name in apps:
		for module_name in frappe.local.app_modules.get(app_name) or []:
			folder = frappe.get_app_path(app_name, module_name, "custom")
			if os.path.exists(folder):
				for fname in os.listdir(folder):
					if fname.endswith(".json"):
						with open(os.path.join(folder, fname)) as f:
							data = json.loads(f.read())
						if data.get("sync_on_migrate"):
							sync_customizations_for_doctype(data, folder, fname)
						elif frappe.flags.in_install and app:
							sync_customizations_for_doctype(data, folder, fname)


<<<<<<< HEAD
def sync_customizations_for_doctype(data: dict, folder: str, filename: str = ""):
=======
def sync_customizations_for_doctype(data, folder, filename: str = ""):
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	"""Sync doctype customzations for a particular data set"""
	from frappe.core.doctype.doctype.doctype import validate_fields_for_doctype

	doctype = data["doctype"]
	update_schema = False

	def sync(key, custom_doctype, doctype_fieldname):
		doctypes = list(set(map(lambda row: row.get(doctype_fieldname), data[key])))

		# sync single doctype exculding the child doctype
		def sync_single_doctype(doc_type):
			def _insert(data):
				if data.get(doctype_fieldname) == doc_type:
					data["doctype"] = custom_doctype
					doc = frappe.get_doc(data)
					doc.db_insert()

			match custom_doctype:
				case "Custom Field":
					for d in data[key]:
						field = frappe.db.get_value(
							"Custom Field", {"dt": doc_type, "fieldname": d["fieldname"]}
						)
						if not field:
							d["owner"] = "Administrator"
							_insert(d)
						else:
							custom_field = frappe.get_doc("Custom Field", field)
							custom_field.flags.ignore_validate = True
							custom_field.update(d)
							custom_field.db_update()
				case "Property Setter":
					# Property setter implement their own deduplication, we can just sync them as is
					for d in data[key]:
						if d.get("doc_type") == doc_type:
							d["doctype"] = "Property Setter"
							doc = frappe.get_doc(d)
							doc.flags.validate_fields_for_doctype = False
							doc.insert()
				case "Custom DocPerm":
					# TODO/XXX: Docperm have no "sync" as of now. They get OVERRIDDEN on sync.
					frappe.db.delete("Custom DocPerm", {"parent": doc_type})

					for d in data[key]:
						_insert(d)

		for doc_type in doctypes:
			# only sync the parent doctype and child doctype if there isn't any other child table json file
<<<<<<< HEAD
			if doc_type == doctype or not os.path.exists(os.path.join(folder, scrub(doc_type) + ".json")):
=======
			if doc_type == doctype or not os.path.exists(
				os.path.join(folder, frappe.scrub(doc_type) + ".json")
			):
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
				sync_single_doctype(doc_type)

	if not frappe.db.exists("DocType", doctype):
		print(_("DocType {0} does not exist.").format(doctype))
<<<<<<< HEAD
		print(_("Skipping fixture syncing for doctype {0} from file {1}").format(doctype, filename))
=======
		print(_("Skipping fixture syncing for doctype {0} from file {1} ").format(doctype, filename))
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
		return

	if data["custom_fields"]:
		sync("custom_fields", "Custom Field", "dt")
		update_schema = True

	if data["property_setters"]:
		sync("property_setters", "Property Setter", "doc_type")

<<<<<<< HEAD
	print(f"Updating customizations for {doctype}")
	if data.get("custom_perms"):
		sync("custom_perms", "Custom DocPerm", "parent")

=======
	if data.get("custom_perms"):
		sync("custom_perms", "Custom DocPerm", "parent")

	print(f"Updating customizations for {doctype}")
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	validate_fields_for_doctype(doctype)

	if update_schema and not frappe.db.get_value("DocType", doctype, "issingle"):
		frappe.db.updatedb(doctype)


<<<<<<< HEAD
def scrub_dt_dn(dt: str, dn: str) -> tuple[str, str]:
=======
def scrub(txt):
	return frappe.scrub(txt)


def scrub_dt_dn(dt, dn):
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	"""Returns in lowercase and code friendly names of doctype and name for certain types"""
	return scrub(dt), scrub(dn)


<<<<<<< HEAD
def get_doc_path(module: str, doctype: str, name: str) -> str:
	"""Returns path of a doc in a module"""
	return os.path.join(get_module_path(module), *scrub_dt_dn(doctype, name))


def reload_doc(
	module: str,
	dt: str | None = None,
	dn: str | None = None,
	force: bool = False,
	reset_permissions: bool = False,
):
	"""Reload Document from model (`[module]/<doctype>/[name]/[name].json`) files"""
=======
def get_module_path(module):
	"""Returns path of the given module"""
	return frappe.get_module_path(module)


def get_doc_path(module, doctype, name):
	dt, dn = scrub_dt_dn(doctype, name)
	return os.path.join(get_module_path(module), dt, dn)


def reload_doc(module, dt=None, dn=None, force=False, reset_permissions=False):
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	from frappe.modules.import_file import import_files

	return import_files(module, dt, dn, force=force, reset_permissions=reset_permissions)


def export_doc(doctype, name, module=None):
	"""Write a doc to standard path."""
	from frappe.modules.export_file import write_document_file

<<<<<<< HEAD
	print(f"Exporting Document {doctype} {name}")
	module = module or frappe.db.get_value("DocType", name, "module")
	write_document_file(frappe.get_doc(doctype, name), module)


def get_doctype_module(doctype: str) -> str:
	"""Returns **Module Def** name of given doctype."""
	doctype_module_map = frappe.cache.get_value(
		"doctype_modules",
		generator=lambda: dict(frappe.qb.from_("DocType").select("name", "module").run()),
	)
=======
	print(doctype, name)

	if not module:
		module = frappe.db.get_value("DocType", name, "module")
	write_document_file(frappe.get_doc(doctype, name), module)


def get_doctype_module(doctype) -> str:
	"""Returns **Module Def** name of given doctype."""

	def make_modules_dict():
		return dict(frappe.db.sql("select name, module from tabDocType"))

	doctype_module_map = frappe.cache().get_value("doctype_modules", make_modules_dict)
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)

	if module_name := doctype_module_map.get(doctype):
		return module_name
	else:
		frappe.throw(_("DocType {} not found").format(doctype), exc=frappe.DoesNotExistError)


<<<<<<< HEAD
def load_doctype_module(doctype, module=None, prefix="", suffix=""):
	"""Returns the module object for given doctype.

	Note: This will return the standard defined module object for the doctype irrespective
	of the `override_doctype_class` hook.
	"""
	module = module or get_doctype_module(doctype)
	app = get_module_app(module)
	key = (app, doctype, prefix, suffix)
	module_name = get_module_name(doctype, module, prefix, suffix)

	if key not in doctype_python_modules:
		try:
			doctype_python_modules[key] = frappe.get_module(module_name)
		except ImportError as e:
			msg = f"Module import failed for {doctype}, the DocType you're trying to open might be deleted."
			msg += f"\nError: {e}"
			raise ImportError(msg) from e
=======
doctype_python_modules = {}


def load_doctype_module(doctype, module=None, prefix="", suffix=""):
	"""Returns the module object for given doctype."""
	if not module:
		module = get_doctype_module(doctype)

	app = get_module_app(module)

	key = (app, doctype, prefix, suffix)

	module_name = get_module_name(doctype, module, prefix, suffix)

	try:
		if key not in doctype_python_modules:
			doctype_python_modules[key] = frappe.get_module(module_name)
	except ImportError as e:
		msg = f"Module import failed for {doctype}, the DocType you're trying to open might be deleted."
		msg += f"\nError: {e}"
		raise ImportError(msg) from e
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)

	return doctype_python_modules[key]


<<<<<<< HEAD
def get_module_name(doctype: str, module: str, prefix: str = "", suffix: str = "", app: str | None = None):
	app = scrub(app or get_module_app(module))
	module = scrub(module)
	doctype = scrub(doctype)
	return f"{app}.{module}.doctype.{doctype}.{prefix}{doctype}{suffix}"
=======
def get_module_name(doctype, module, prefix="", suffix="", app=None):
	return "{app}.{module}.doctype.{doctype}.{prefix}{doctype}{suffix}".format(
		app=scrub(app or get_module_app(module)),
		module=scrub(module),
		doctype=scrub(doctype),
		prefix=prefix,
		suffix=suffix,
	)
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)


def get_module_app(module: str) -> str:
	app = frappe.local.module_app.get(scrub(module))
	if app is None:
		frappe.throw(_("Module {} not found").format(module), exc=frappe.DoesNotExistError)
	return app


def get_app_publisher(module: str) -> str:
	app = get_module_app(module)
	if not app:
<<<<<<< HEAD
		frappe.throw(_("App not found for module: {0}").format(module))
	return frappe.get_hooks(hook="app_publisher", app_name=app)[0]


def make_boilerplate(
	template: str, doc: Union["Document", "frappe._dict"], opts: Union[dict, "frappe._dict"] = None
):
=======
		frappe.throw(_("App not found"))
	app_publisher = frappe.get_hooks(hook="app_publisher", app_name=app)[0]
	return app_publisher


def make_boilerplate(template, doc, opts=None):
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	target_path = get_doc_path(doc.module, doc.doctype, doc.name)
	template_name = template.replace("controller", scrub(doc.name))
	if template_name.endswith("._py"):
		template_name = template_name[:-4] + ".py"
	target_file_path = os.path.join(target_path, template_name)
<<<<<<< HEAD
	template_file_path = os.path.join(
		get_module_path("core"), "doctype", scrub(doc.doctype), "boilerplate", template
	)

	if os.path.exists(target_file_path):
		print(f"{target_file_path} already exists, skipping...")
		return

	doc = doc or frappe._dict()
	opts = opts or frappe._dict()
	app_publisher = get_app_publisher(doc.module)
	base_class = "Document"
	base_class_import = "from frappe.model.document import Document"
	controller_body = "pass"

	if doc.get("is_tree"):
		base_class = "NestedSet"
		base_class_import = "from frappe.utils.nestedset import NestedSet"

	if doc.get("is_virtual"):
		controller_body = indent(
			dedent(
				"""
			def db_insert(self, *args, **kwargs):
				pass

			def load_from_db(self):
				pass

			def db_update(self):
				pass

			@staticmethod
			def get_list(args):
				pass

			@staticmethod
			def get_count(args):
				pass

			@staticmethod
			def get_stats(args):
				pass
			"""
			),
			"\t",
		)

	with open(target_file_path, "w") as target, open(template_file_path) as source:
		template = source.read()
		controller_file_content = cstr(template).format(
			app_publisher=app_publisher,
			year=now_datetime().year,
			classname=doc.name.replace(" ", "").replace("-", ""),
			base_class_import=base_class_import,
			base_class=base_class,
			doctype=doc.name,
			**opts,
			custom_controller=controller_body,
		)
		target.write(frappe.as_unicode(controller_file_content))
=======

	if not doc:
		doc = {}

	app_publisher = get_app_publisher(doc.module)

	if not os.path.exists(target_file_path):
		if not opts:
			opts = {}

		base_class = "Document"
		base_class_import = "from frappe.model.document import Document"
		if doc.get("is_tree"):
			base_class = "NestedSet"
			base_class_import = "from frappe.utils.nestedset import NestedSet"

		custom_controller = "pass"
		if doc.get("is_virtual"):
			custom_controller = """
	def db_insert(self, *args, **kwargs):
		pass

	def load_from_db(self):
		pass

	def db_update(self, *args, **kwargs):
		pass

	@staticmethod
	def get_list(args):
		pass

	@staticmethod
	def get_count(args):
		pass

	@staticmethod
	def get_stats(args):
		pass"""

		with open(target_file_path, "w") as target:
			with open(
				os.path.join(get_module_path("core"), "doctype", scrub(doc.doctype), "boilerplate", template),
			) as source:
				target.write(
					frappe.as_unicode(
						frappe.utils.cstr(source.read()).format(
							app_publisher=app_publisher,
							year=frappe.utils.nowdate()[:4],
							classname=doc.name.replace(" ", "").replace("-", ""),
							base_class_import=base_class_import,
							base_class=base_class,
							doctype=doc.name,
							**opts,
							custom_controller=custom_controller,
						)
					)
				)
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
