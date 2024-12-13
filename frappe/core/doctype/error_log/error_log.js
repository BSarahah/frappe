// Copyright (c) 2022, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Error Log", {
	refresh: function (frm) {
		frm.disable_save();

		if (frm.doc.reference_doctype && frm.doc.reference_name) {
			frm.add_custom_button(__("Show Related Errors"), function () {
				frappe.set_route("List", "Error Log", {
					reference_doctype: frm.doc.reference_doctype,
					reference_name: frm.doc.reference_name,
				});
			});
<<<<<<< HEAD
=======
			frm.add_custom_button(__("Open reference document"), function () {
				frappe.set_route("Form", frm.doc.reference_doctype, frm.doc.reference_name);
			});
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
		}
	},
});
