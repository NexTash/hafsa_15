import frappe
from frappe.utils import nowdate

def send_overdue_reminders():
    overdue_books = frappe.get_all(
        "Library Book",
        filters={"status": "Issued", "due_date": ("<", nowdate())},
        fields=["name", "title", "author"]
    )

    for book in overdue_books:
        # Example: Log reminder (in real case, send email)
        frappe.logger().info(f"Reminder: Book {book.title} is overdue!")

@frappe.whitelist(allow_guest=True)
def enqueue_overdue_reminders():
    frappe.enqueue("hafsa_15.reminders.send_overdue_reminders")
    return "Job enqueued to send overdue reminders."
