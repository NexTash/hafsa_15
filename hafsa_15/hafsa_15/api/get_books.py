import frappe

# @frappe.whitelist(allow_guest=True)
# def create_book(title, author, isbn):
#     doc = frappe.get_doc({
#         "doctype": "Library Book",
#         "title": title,
#         "author": author,
#         "isbn": isbn,
#         "status": "Available"
#     })
#     doc.insert()
#     return doc.name


@frappe.whitelist(allow_guest=True)
def get_books():
    """Return all Library Book documents"""
    books = frappe.get_all(
        "Library Book",
        fields=["name", "title", "author", "isbn", "status"]
    )
    return books

@frappe.whitelist(allow_guest=True)
def get_books_raw_sql():
    books = frappe.db.sql(
        """
        SELECT name, title, author, isbn, status
        FROM `tabLibrary Book`
        WHERE status = 'Available'
        ORDER BY title ASC
        """,
        as_dict=True
    )
    return books
@frappe.whitelist(allow_guest=True)
def get_books_orm():
    return frappe.get_all(
        "Library Book",
        filters={"status": "Available"},
        fields=["name", "title", "author", "isbn", "status"],
        order_by="title asc"
    )
import frappe

@frappe.whitelist(allow_guest=True)
def create_book(title, author, isbn):
    doc = frappe.get_doc({
        "doctype": "Library Book",
        "title": title,
        "author": author,
        "isbn": isbn,
        "status": "Available"
    })
    doc.insert()
    return doc.name