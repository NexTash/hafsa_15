# Copyright (c) 2025, Nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

# class LibraryBook(Document):
#     def on_update(self):
#         if not self.isbn:
#             frappe.throw("ISBN is required")
#         if not self.status:
#             self.status = "Available"
#             frappe.throw("Status is always set 'Available' ")
class LibraryBook(Document):
    def validate(self):
        if not self.title:
            frappe.throw("Title is required")
        if not self.author:
            frappe.throw("Author is required")
        if not self.isbn:
            frappe.throw("ISBN is required")
        if self.status not in ["Available", "Issued"]:
            frappe.throw("Status must be either 'Available' or 'Issued'")
