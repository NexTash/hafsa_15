# Copyright (c) 2025, Nextash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    def validate(self):
       if frappe.db.exists("Customer", {"library_card_number": self.library_card_number, "name": ["!=", self.name]}):
        frappe.throw("Library Card Number must be unique")