frappe.listview_settings["Contact"] = {
	add_fields: ["image"],
<<<<<<< HEAD
=======
	onload: function (listview) {
		listview.page.add_action_item(__("Download vCards"), function () {
			const contacts = listview.get_checked_items();
			open_url_post("/api/method/frappe.contacts.doctype.contact.contact.download_vcards", {
				contacts: contacts.map((c) => c.name),
			});
		});
	},
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
};
