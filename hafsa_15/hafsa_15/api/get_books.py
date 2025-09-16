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


@frappe.whitelist(allow_guest=True)
def get_books():
    """Return all Library Book documents"""
    books = frappe.get_all(
        "Library Book",
        fields=["name", "title", "author", "isbn", "status"]
    )
    return books