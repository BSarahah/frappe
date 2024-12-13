import frappe


def execute():
	# patch for all Email Account with the flag use_imap
	for email_account in frappe.get_list("Email Account", filters={"enable_incoming": 1, "use_imap": 1}):
		# get all data from Email Account
		doc = frappe.get_doc("Email Account", email_account.name)

		imap_list = [folder.folder_name for folder in doc.imap_folder]
		# and append the old data to the child table
<<<<<<< HEAD
		if doc.uidvalidity or doc.uidnext and "INBOX" not in imap_list:
=======
		if doc.uidvalidity or (doc.uidnext and "INBOX" not in imap_list):
>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
			doc.append(
				"imap_folder",
				{
					"folder_name": "INBOX",
					"append_to": doc.append_to,
					"uid_validity": doc.uidvalidity,
					"uidnext": doc.uidnext,
				},
			)

			doc.save()
