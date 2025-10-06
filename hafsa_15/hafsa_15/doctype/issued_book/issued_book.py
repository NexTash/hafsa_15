# Copyright (c) 2025, Nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class IssuedBook(Document):
    def validate(self):
        book = frappe.get_doc("Library Book", self.book)

        # Check if the book is available for issuing
        if book.status != "Available":
            frappe.throw(f"Book '{book.title}' is not available for issuing. Current status: {book.status}")

        # Optional: double-check if status is already "Issued"
        if book.status == "Issued":
            frappe.throw(f"The book '{book.title}' is already issued.")