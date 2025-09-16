# Copyright (c) 2025, Nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryBook(Document):
    pass
#     def on_update(self):
#         if not self.isbn:
#             frappe.throw("ISBN is required")
#         if not self.status:
#             self.status = "Available"
#             frappe.throw("Status is always set 'Available' ")
