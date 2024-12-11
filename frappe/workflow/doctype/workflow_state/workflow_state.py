# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe
from frappe.model.document import Document


class WorkflowState(Document):
<<<<<<< HEAD
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		icon: DF.Literal[
			"",
			"glass",
			"music",
			"search",
			"envelope",
			"heart",
			"star",
			"star-empty",
			"user",
			"film",
			"th-large",
			"th",
			"th-list",
			"ok",
			"remove",
			"zoom-in",
			"zoom-out",
			"off",
			"signal",
			"cog",
			"trash",
			"home",
			"file",
			"time",
			"road",
			"download-alt",
			"download",
			"upload",
			"inbox",
			"play-circle",
			"repeat",
			"refresh",
			"list-alt",
			"lock",
			"flag",
			"headphones",
			"volume-off",
			"volume-down",
			"volume-up",
			"qrcode",
			"barcode",
			"tag",
			"tags",
			"book",
			"bookmark",
			"print",
			"camera",
			"font",
			"bold",
			"italic",
			"text-height",
			"text-width",
			"align-left",
			"align-center",
			"align-right",
			"align-justify",
			"list",
			"indent-left",
			"indent-right",
			"facetime-video",
			"picture",
			"pencil",
			"map-marker",
			"adjust",
			"tint",
			"edit",
			"share",
			"check",
			"move",
			"step-backward",
			"fast-backward",
			"backward",
			"play",
			"pause",
			"stop",
			"forward",
			"fast-forward",
			"step-forward",
			"eject",
			"chevron-left",
			"chevron-right",
			"plus-sign",
			"minus-sign",
			"remove-sign",
			"ok-sign",
			"question-sign",
			"info-sign",
			"screenshot",
			"remove-circle",
			"ok-circle",
			"ban-circle",
			"arrow-left",
			"arrow-right",
			"arrow-up",
			"arrow-down",
			"share-alt",
			"resize-full",
			"resize-small",
			"plus",
			"minus",
			"asterisk",
			"exclamation-sign",
			"gift",
			"leaf",
			"fire",
			"eye-open",
			"eye-close",
			"warning-sign",
			"plane",
			"calendar",
			"random",
			"comment",
			"magnet",
			"chevron-up",
			"chevron-down",
			"retweet",
			"shopping-cart",
			"folder-close",
			"folder-open",
			"resize-vertical",
			"resize-horizontal",
			"hdd",
			"bullhorn",
			"bell",
			"certificate",
			"thumbs-up",
			"thumbs-down",
			"hand-right",
			"hand-left",
			"hand-up",
			"hand-down",
			"circle-arrow-right",
			"circle-arrow-left",
			"circle-arrow-up",
			"circle-arrow-down",
			"globe",
			"wrench",
			"tasks",
			"filter",
			"briefcase",
			"fullscreen",
		]
		style: DF.Literal["", "Primary", "Info", "Success", "Warning", "Danger", "Inverse"]
		workflow_state_name: DF.Data
	# end: auto-generated types
=======
>>>>>>> c3bd8892e6 (fix: in case of owner, always include owner in count data)
	pass
