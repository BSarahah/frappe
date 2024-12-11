# Copyright (c) 2013, Frappe and contributors
# License: MIT. See LICENSE

import frappe
from frappe.website.doctype.help_article.help_article import clear_cache
from frappe.website.website_generator import WebsiteGenerator


class HelpCategory(WebsiteGenerator):
<<<<<<< HEAD
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		category_description: DF.Text | None
		category_name: DF.Data
		help_articles: DF.Int
		published: DF.Check
		route: DF.Data | None
	# end: auto-generated types
=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	website = frappe._dict(condition_field="published", page_title_field="category_name")

	def before_insert(self):
		self.published = 1

	def autoname(self):
		self.name = self.category_name

	def validate(self):
		self.set_route()

<<<<<<< HEAD
		# disable help articles of this category
		if not self.published:
			for d in frappe.get_all("Help Article", dict(category=self.name)):
				frappe.db.set_value("Help Article", d.name, "published", 0)

=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	def set_route(self):
		if not self.route:
			self.route = "kb/" + self.scrub(self.category_name)

	def on_update(self):
		clear_cache()
