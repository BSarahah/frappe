# Copyright (c) 2019, Frappe Technologies and contributors
# License: MIT. See LICENSE

from frappe.model.document import Document


class WebsiteRouteMeta(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from frappe.website.doctype.website_meta_tag.website_meta_tag import WebsiteMetaTag

		meta_tags: DF.Table[WebsiteMetaTag]
<<<<<<< HEAD

	# end: auto-generated types
=======
	# end: auto-generated types

>>>>>>> 4509e75179 (fix: convert frappe.boot to JSON properly)
	def autoname(self):
		if self.name and self.name.startswith("/"):
			self.name = self.name[1:]
