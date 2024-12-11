// Copyright (c) 2020, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Module Onboarding", {
	refresh: function (frm) {
		frappe.boot.developer_mode &&
			frm.set_intro(
				__(
					"Saving this will export this document as well as the steps linked here as json."
				),
				true
			);
		if (!frappe.boot.developer_mode) {
			frm.trigger("disable_form");
		}
<<<<<<< HEAD

		frm.add_custom_button(__("Reset"), () => {
			frm.call("reset_progress");
		});
=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	},

	disable_form: function (frm) {
		frm.set_read_only();
		frm.fields
			.filter((field) => field.has_input)
			.forEach((field) => {
				frm.set_df_property(field.df.fieldname, "read_only", "1");
			});
		frm.disable_save();
	},
});
